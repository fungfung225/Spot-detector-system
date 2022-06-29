import ctypes
import queue
import typing
from typing import Callable

import ContinuousLearner
from Yolov5TRT import Yolov5TRT
from libs.FunctionPipeline import FunctionPipeline
from libs.ImageProcessingFunctions import *
from libs.Log import *
from libs.TCPHandler import *
from libs.ThreadRunnable import *
from libs.utils import *


class BufferPackedResult:
    def __init__(self, buffer_size=2):
        self.buffer = queue.Queue(buffer_size)

    def put(self, packed_result: dict):
        try:
            self.buffer.put_nowait(packed_result)
        except queue.Full:
            self.buffer.get_nowait()
            self.buffer.put_nowait(packed_result)

    def get(self) -> typing.Tuple[bool, dict]:
        try:
            packed_result = self.buffer.get_nowait()
            self.buffer.task_done()
            return True, packed_result
        except queue.Empty:
            return False, {}


class RecordFPS:
    def __init__(self):
        self.fps = -1
        self.timer = time.time()

    def get_fps(self):
        return self.fps

    def _FPSStartPoint_(self):
        self.timer = time.time()

    def _FPSUpdateFPS_(self):
        self.fps = 1 / (time.time() - self.timer)


_DETECTOR_CONFIG_FILE_ = f'config/{platform.node()}_detector_config.dict'


class DetectSettings:
    def save_config_to_file(self):
        with open(self.config_file, 'wb') as configs:
            pickle.dump(self.config_dict, configs)

    def read_config_from_file(self):
        try:
            with open(self.config_file, 'rb') as configs:
                config_dict_in = pickle.load(configs)
                for item in config_dict_in:
                    self.config_dict[item] = config_dict_in[item]
        except FileNotFoundError:
            pass

    def subscribe_to_value_change(self, setting_name: str, call_back_func: Callable):
        if setting_name in self.config_on_change_dict:
            self.config_on_change_dict[setting_name].append(call_back_func)
        else:
            self.config_on_change_dict[setting_name] = [call_back_func]

    def get_setting_value(self, setting_name: str):
        return self.config_dict[setting_name]

    def get_or_set_setting_value(self, setting_name: str, value):
        if setting_name in self.config_dict:
            return self.get_setting_value(setting_name)
        else:
            self.config_dict[setting_name] = value
            return value

    def set_setting_value(self, setting_name: str, value):
        Log.info(f"Setting change. {setting_name}: {value}")
        self.config_dict[setting_name] = value
        if setting_name in self.config_on_change_dict:
            for func in self.config_on_change_dict[setting_name]:
                func(value)
        self.save_config_to_file()

    def __init__(self, config_file: str):
        self.config_file = config_file
        self.require_init = False
        self.config_dict = {}  # setting_name: setting_value
        self.read_config_from_file()
        Log.info(f"Initial Settings: {self.config_dict}")
        self.config_on_change_dict = {}  # setting_name: [list of call back function]


# Frame pre-processor: read frame from gstreamer and preprocess the frame
class FramePreProcessor(ThreadRunnable, BufferPackedResult, RecordFPS):
    def __init__(self, settings: DetectSettings):
        ThreadRunnable.__init__(self)
        BufferPackedResult.__init__(self)
        RecordFPS.__init__(self)
        if 'Win' in platform.platform() or ('Linux' in platform.platform() and 'x86' in platform.platform()):
            self.cap = cv.VideoCapture(0)
            self.cap_width = self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap_height = self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        else:
            self.cap = cv.VideoCapture(gstreamer_pipeline())
        self.cap_width = self.cap.get(cv.CAP_PROP_FRAME_WIDTH)
        self.cap_height = self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)

        self.pre_process = True
        self.offsetLeft = settings.get_or_set_setting_value('offsetLeft', 0)
        self.offsetRight = settings.get_or_set_setting_value('offsetRight', 0)
        self.offsetUp = settings.get_or_set_setting_value('offsetUp', 0)
        self.offsetDown = settings.get_or_set_setting_value('offsetDown', 0)
        self._1_norm_min = settings.get_or_set_setting_value("_1_norm_min", 0)
        self._1_norm_max = settings.get_or_set_setting_value("_1_norm_max", 256)
        self._2_contrast = settings.get_or_set_setting_value("_2_contrast", 1.3)

        settings.subscribe_to_value_change('offsetUp', self.set_offset_up)
        settings.subscribe_to_value_change('offsetDown', self.set_offset_down)
        settings.subscribe_to_value_change('offsetLeft', self.set_offset_left)
        settings.subscribe_to_value_change('offsetRight', self.set_offset_right)
        settings.subscribe_to_value_change("_1_norm_min", self.set_1_norm_min)
        settings.subscribe_to_value_change("_1_norm_max", self.set_1_norm_max)
        settings.subscribe_to_value_change("_2_contrast", self.set_2_contrast)
        self.settings = settings

        self.processing_pipe = FunctionPipeline()
        self.init_processing_pipe()

    def init_processing_pipe(self):
        # 0
        self.processing_pipe.add_func(color2gray, {})
        # 1
        self.processing_pipe.add_func(minmax_normalize, {'norm_min': self._1_norm_min, 'norm_max': self._1_norm_max})
        # 2
        self.processing_pipe.add_func(adjust_contrast, {'contrast': self._2_contrast})

    # ------------- Setters
    def set_offset_up(self, v):
        self.offsetUp = v

    def set_offset_down(self, v):
        self.offsetDown = v

    def set_offset_left(self, v):
        self.offsetLeft = v

    def set_offset_right(self, v):
        self.offsetRight = v

    def set_1_norm_min(self, v):
        self._1_norm_min = v
        self.processing_pipe.update_func_param(1, 'norm_min', self._1_norm_min)

    def set_1_norm_max(self, v):
        self._1_norm_max = v
        self.processing_pipe.update_func_param(1, 'norm_max', self._1_norm_max)

    def set_2_contrast(self, v):
        self._2_contrast = v
        self.processing_pipe.update_func_param(2, 'contrast', self._2_contrast)

    def exit_nicely(self, *args):
        self.thread_stop()
        self.cap.release()
        Log.info("FramePreProcessor terminated nicely.")

    def on_start(self):
        Log.info("FramePreProcessor started...")

    def set_pre_process(self, v: bool):
        self.pre_process = v

    def main_body(self):
        ret, frame = self.cap.read()
        if ret:
            self._FPSStartPoint_()
            packed_result = {'creation_time': time.time()}
            # pre-processing frame
            frame_cropped = frame[int(self.offsetUp):int(self.cap_height - self.offsetDown),
                            int(self.offsetLeft):int(self.cap_width - self.offsetRight)]
            if self.pre_process:
                processed_frame = self.processing_pipe.execute_pipeline(frame_cropped)
                packed_result['processed'] = processed_frame
            self._FPSUpdateFPS_()
            packed_result['raw'] = frame_cropped
            packed_result['fps_fpp'] = self.fps
            self.put(packed_result)

    def on_end(self):
        self.thread_stop()
        self.cap.release()
        Log.info("FramePreProcessor terminated.")


class CVSpotDetector(ThreadRunnable, BufferPackedResult, RecordFPS):
    def __init__(self, pre_processor: FramePreProcessor, settings: DetectSettings):
        ThreadRunnable.__init__(self)
        BufferPackedResult.__init__(self)
        RecordFPS.__init__(self)
        self.detectorParam = None
        self.detector = None
        self.pre_processor = pre_processor

        self.settings = settings
        self.prepare_blob_detector_params()
        self.update_detector()
        settings.subscribe_to_value_change('minArea', self.set_min_area)
        settings.subscribe_to_value_change('maxArea', self.set_max_area)
        settings.subscribe_to_value_change('minThreshold', self.set_min_threshold)
        settings.subscribe_to_value_change('maxThreshold', self.set_max_threshold)
        self.settings.subscribe_to_value_change('sensitivity', self.set_sensitivity)
        self.set_sensitivity(self.settings.get_or_set_setting_value('sensitivity', 500))

    def set_sensitivity(self, v):
        self.set_max_threshold(int((v / 1000) * 255))

    # setter
    def set_min_area(self, value):
        self.detectorParam.minArea = value
        self.update_detector()

    def set_max_area(self, value):
        self.detectorParam.maxArea = value
        self.update_detector()

    def set_min_threshold(self, value):
        self.detectorParam.minThreshold = value
        self.update_detector()

    def set_max_threshold(self, value):
        self.detectorParam.maxThreshold = value
        self.update_detector()

    def update_detector(self):
        self.detector = cv.SimpleBlobDetector_create(self.detectorParam)

    def prepare_blob_detector_params(self):
        if self.detectorParam is None:
            self.detectorParam = cv.SimpleBlobDetector_Params()
        params = self.detectorParam

        # Filter by brightness
        params.minThreshold = self.settings.get_or_set_setting_value('minThreshold', 0)
        params.maxThreshold = self.settings.get_or_set_setting_value('maxThreshold', 255)

        # Filter by Area.
        params.filterByArea = True
        params.minArea = self.settings.get_or_set_setting_value("minArea", 0)
        params.maxArea = self.settings.get_or_set_setting_value("maxArea", 10000)
        # params.minArea = 0
        # params.maxArea = 10000

        # Set true if detecting black regions
        params.filterByColor = False
        # Filter by Color (black=0)
        params.blobColor = 0

        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0  # 0.3
        params.maxCircularity = 1

        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0  # 0.2
        params.maxConvexity = 1

        # Filter by InertiaRatio
        params.filterByInertia = True
        params.minInertiaRatio = 0
        params.maxInertiaRatio = 1

        # Distance Between Blobs
        params.minDistBetweenBlobs = 0

    def exit_nicely(self, *args):
        self.thread_stop()
        Log.info("CVSpotDetector terminated nicely!")

    def on_start(self):
        Log.info("CVSpotDetector started...")

    @staticmethod
    def convert_keypoints_to_labels(keypoints, frame):
        h, w, _ = frame.shape
        labels = []
        for kp in keypoints:
            x = kp.pt[0]
            y = kp.pt[1]
            size = kp.size / 2 + 2
            labels.append(f"{x / w} {y / h} {size / w} {size / y}")
        return labels

    def main_body(self):
        ret, packed_result = self.pre_processor.get()
        if ret:
            self._FPSStartPoint_()
            keypoints = self.detector.detect(packed_result['processed'])
            self._FPSUpdateFPS_()
            packed_result['keypoints'] = keypoints
            packed_result['labels'] = self.convert_keypoints_to_labels(keypoints, packed_result['raw'])
            packed_result['processed'] = draw_cv_keypoints_on_frame(keypoints, packed_result['processed'])
            packed_result['num_spots'] = len(keypoints)
            packed_result['detector_fps'] = self.fps
            self.put(packed_result)

    def on_end(self):
        self.thread_stop()
        Log.info("CVSpotDetector terminated!")


class YoloV5Detector(ThreadRunnable, BufferPackedResult, RecordFPS):
    categories = ["NG"]

    def __init__(self, pre_processor: FramePreProcessor, settings: DetectSettings):
        ThreadRunnable.__init__(self)
        BufferPackedResult.__init__(self)
        RecordFPS.__init__(self)
        plugin_library = "./res/Jetson_nano/libmyplugins.so"
        # TODO: check updated engine file
        dl_engines = get_all_files(ContinuousLearner.LOCAL_WEIGHTS_PATH)
        if len(dl_engines) > 0:
            for engine_file in dl_engines:
                engine_file_path = ContinuousLearner.LOCAL_WEIGHTS_PATH + f'/{engine_file}'
                if 'general' not in engine_file:
                    break
        else:
            if psutil.virtual_memory().total / 2 ** 30 > 3:
                engine_file_path = "./res/Jetson_nano/general_4gb.engine"
            else:
                engine_file_path = "./res/Jetson_nano/general_2gb.engine"
        if 'Win' in platform.platform() or ('Linux' in platform.platform() and 'x86' in platform.platform()):
            plugin_library = "./res/Linux_x86_RTX3090/libmyplugins.so"
            engine_file_path = "./res/Linux_x86_RTX3090/mixed_nb811.engine"
        ctypes.CDLL(plugin_library)
        self.pre_processor = pre_processor
        self.settings = settings
        # noinspection PyUnboundLocalVariable
        self.yolov5_wrapper = Yolov5TRT(engine_file_path=engine_file_path, categories=self.categories)

        self.settings.subscribe_to_value_change('sensitivity', self.set_sensitivity)
        self.set_sensitivity(self.settings.get_or_set_setting_value('sensitivity', 500))

    def set_sensitivity(self, v):
        """
        More sensitive -> less confidence threshold
        """
        self.yolov5_wrapper.set_conf_thresh(1 - v / 1000)

    def exit_nicely(self, *args):
        self.thread_stop()
        Log.info("YoloV5Detector terminated nicely!")

    def on_start(self):
        Log.info("YoloV5Detector started...")

    @staticmethod
    def convert_keypoints_to_labels(keypoints, frame):
        labels = []
        h, w, _ = frame.shape
        for kp in keypoints:
            kw = kp[2] - kp[0]
            kh = kp[3] - kp[1]
            x = kp[0] + kw / 2
            y = kp[1] + kh / 2
            labels.append(f"{x / w} {y / h} {kw / w} {kh / h}")
        return labels

    def main_body(self):
        ret, packed_result = self.pre_processor.get()
        if ret:
            self._FPSStartPoint_()
            packed_result['processed'] = packed_result['raw'].copy()
            packed_result['processed'], packed_result['inference_time'], packed_result['num_spots'], packed_result[
                'keypoints'] = self.yolov5_wrapper.inference(packed_result['processed'])
            packed_result['labels'] = self.convert_keypoints_to_labels(packed_result['keypoints'], packed_result['raw'])
            self._FPSUpdateFPS_()
            packed_result['detector_fps'] = self.fps
            self.put(packed_result)

    def on_end(self):
        self.thread_stop()
        self.yolov5_wrapper.destroy()
        Log.info("YoloV5Detector terminated!")

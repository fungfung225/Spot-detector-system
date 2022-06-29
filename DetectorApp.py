import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox

import DetectorUI as UI
from AlarmHandler import AlarmHandler
from ContinuousLearner import ContinuousLearner
from CustomUI import DataCollectionDialog
from Detector import DetectSettings, BufferPackedResult, FramePreProcessor, YoloV5Detector, CVSpotDetector
from GPIOHandler import GPIOHandler
from GoogleDriveResultHandler import *
# Adapt 4k Monitor
from PowerManager import PowerManager

_IS_JETSON_NANO = 'Win' in platform.platform() or ('Linux' in platform.platform() and 'x86' in platform.platform())
if _IS_JETSON_NANO:
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons

_ENABLE_DETECTION_TIME = 180

# _sufficient_ram_for_ai = psutil.virtual_memory().total / 2 ** 30 > 3  # Limit 2GB nano?
_sufficient_ram_for_ai = True  # Limit 2GB nano?


class FrameProcessingEngine(QThread, BufferPackedResult):
    sig_source = pyqtSignal(QImage)

    def __init__(self, settings: DetectSettings):
        QThread.__init__(self)
        BufferPackedResult.__init__(self)
        self.thread_run = True
        self.settings = settings
        self.frame_processor = FramePreProcessor(self.settings)
        self.cv_detector = CVSpotDetector(self.frame_processor, self.settings)
        if _sufficient_ram_for_ai:
            self.yolo_detector = YoloV5Detector(self.frame_processor, self.settings)
        else:
            self.yolo_detector = None
        self.cv_detector.thread_stop()
        self.yolo_detector.thread_stop()
        self.detector = self.cv_detector
        self.update_timer = time.time()

    def use_yolo(self):
        if _sufficient_ram_for_ai:
            self.detector = self.yolo_detector
            self.frame_processor.set_pre_process(False)

    def use_cv(self):
        self.detector = self.cv_detector
        self.frame_processor.set_pre_process(True)

    def run(self) -> None:
        while self.thread_run:
            # capturing frame must be done in QThread or fps will drop significantly
            self.frame_processor.main_body()

            self.detector.main_body()
            ret, result = self.detector.get()

            if ret:
                frame = result['processed']
                # info_str = f"DFPS: {round(result['detector_fps'])}, UFPS: {round(1 / (time.time() - result['creation_time']), 2)};"
                # info_str += f'NumSpots: {result["num_spots"]};'
                # info_str += f'ComT: {round((time.time() - result["creation_time"]) * 1000, 2)} ms;'
                # frame = add_text_to_frame(frame, info_str)
                self.sig_source.emit(cvt_cv_to_qt(frame))
                self.put(result)
                self.update_timer = time.time()

    def stop(self):
        self.thread_run = False
        self.frame_processor.thread_stop()
        self.frame_processor.on_end()

        self.cv_detector.thread_stop()
        self.cv_detector.on_end()

        if _sufficient_ram_for_ai:
            self.yolo_detector.thread_stop()
            self.yolo_detector.on_end()
        self.quit()


class DetectorApp(UI.Ui_MainWindow, BufferPackedResult):
    _CONFIG_DIR = 'config'
    _DETECTOR_CONFIG_FILE = f'{_CONFIG_DIR}/{platform.node()}_detector_config.dict'

    def __init__(self):
        BufferPackedResult.__init__(self)
        self.qt_app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        # --- additional ui settings
        self.MainWindow.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.tabWidget_liveView.setCurrentIndex(0)
        self.pushButton_enableAlarm.setChecked(False)
        self.horizontalScrollBar_sensitivity.setMinimum(1)

        # Create necessary dirs
        create_dir_if_not_exists(self._CONFIG_DIR)
        create_dir_if_not_exists('logs')

        self.settings = DetectSettings(self._DETECTOR_CONFIG_FILE)

        self.spot_frame_cnt = 0
        self.spot_frame_timer = 0
        self.gpio = GPIOHandler()
        self.rs845_alarm = AlarmHandler()  # legacy alarm

        self.gd_result_handler = GoogleDriveResultHandler()
        self.gd_data_handler = ContinuousLearner()
        self.raw_target = self.gd_data_handler.get_raw_target_today()
        self.fpe = FrameProcessingEngine(self.settings)
        # noinspection PyBroadException
        try:
            self.power_manager = PowerManager(self.on_power_disconnected)
        except Exception:
            pass
        self.spot_img_paths = []
        self.spot_img_path_idx = 0
        self.enable_detection_timer = time.time()
        self.update_timer = time.time()
        self.alarm_timer = 0

        self.set_ui_actions()
        self.init_ui_values()

    def on_power_disconnected(self):
        Log.warning(f"Power disconnected!")
        self.qt_app.exit(999)
        try:
            self.exit_procedure()
        except Exception as e:
            Log.error(f'{e}')
        # finally:
        #     os.system('poweroff')

    def init_ui_values(self):
        self.update_left_offset_label()
        self.update_right_offset_label()
        self.update_up_offset_label()
        self.update_down_offset_label()
        self.update_contrast_label()
        self.comboBox_mode.setCurrentIndex(self.settings.get_or_set_setting_value('mode', 0))
        self.update_sensitivity_label()
        self.action_collectData.setStatusTip("Collect raw data manually.")
        self.menu_otherFunctions.setEnabled(True)

    def on_sensitivity_change(self):
        self.settings.set_setting_value('sensitivity', self.horizontalScrollBar_sensitivity.value())
        self.update_sensitivity_label()

    def update_sensitivity_label(self):
        self.horizontalScrollBar_sensitivity.setValue(int(self.settings.get_setting_value('sensitivity')))
        self.label_sensitivity.setText(f"{round(self.settings.get_setting_value('sensitivity') / 1000, 2)}")

    def on_left_offset_change(self):
        self.settings.set_setting_value('offsetLeft', self.horizontalScrollBar_offsetLeft.value())
        self.update_left_offset_label()

    def update_left_offset_label(self):
        self.horizontalScrollBar_offsetLeft.setValue(int(self.settings.get_setting_value('offsetLeft')))
        self.label_offsetLeft.setText(f"{self.settings.get_setting_value('offsetLeft')}")

    def on_right_offset_change(self):
        self.settings.set_setting_value('offsetRight', self.horizontalScrollBar_offsetRight.value())
        self.update_right_offset_label()

    def update_right_offset_label(self):
        self.horizontalScrollBar_offsetRight.setValue(int(self.settings.get_setting_value('offsetRight')))
        self.label_offsetRight.setText(f"{self.settings.get_setting_value('offsetRight')}")

    def on_up_offset_change(self):
        self.settings.set_setting_value('offsetUp', self.horizontalScrollBar_offsetUp.value())
        self.update_up_offset_label()

    def update_up_offset_label(self):
        self.horizontalScrollBar_offsetUp.setValue(int(self.settings.get_setting_value('offsetUp')))
        self.label_offsetUp.setText(f"{self.settings.get_setting_value('offsetUp')}")

    def on_down_offset_change(self):
        self.settings.set_setting_value('offsetDown', self.horizontalScrollBar_offsetDown.value())
        self.update_down_offset_label()

    def update_down_offset_label(self):
        self.horizontalScrollBar_offsetDown.setValue(int(self.settings.get_setting_value('offsetDown')))
        self.label_offsetDown.setText(f"{self.settings.get_setting_value('offsetDown')}")

    def on_contrast_change(self):
        self.settings.set_setting_value('_2_contrast', self.horizontalScrollBar_contrast.value() / 100.0)
        self.update_contrast_label()

    def update_contrast_label(self):
        self.horizontalScrollBar_contrast.setValue(int(self.settings.get_setting_value('_2_contrast') * 100))
        self.label_contrast.setText(f"{self.settings.get_setting_value('_2_contrast')}")

    def on_first_button_clicked(self):
        self.update_img_viewer(0)

    def on_last_button_clicked(self):
        self.update_img_viewer(len(self.spot_img_paths) - 1)

    def on_prev_button_clicked(self):
        self.update_img_viewer(max(0, self.spot_img_path_idx - 1))

    def on_next_button_clicked(self):
        self.update_img_viewer(min(len(self.spot_img_paths) - 1, self.spot_img_path_idx + 1))

    def set_ui_actions(self):
        self.MainWindow.closeEvent = self.ask_stopApp
        self.pushButton_exit.clicked.connect(lambda: self.MainWindow.close())
        self.pushButton_reboot.clicked.connect(self.ask_reboot)
        self.pushButton_poweroff.clicked.connect(self.ask_poweroff)

        self.fpe.sig_source.connect(self.update_pp_to_ui)
        self.comboBox_mode.currentIndexChanged.connect(self.on_mode_change)

        self.horizontalScrollBar_offsetLeft.valueChanged.connect(self.on_left_offset_change)
        self.horizontalScrollBar_offsetRight.valueChanged.connect(self.on_right_offset_change)
        self.horizontalScrollBar_offsetUp.valueChanged.connect(self.on_up_offset_change)
        self.horizontalScrollBar_offsetDown.valueChanged.connect(self.on_down_offset_change)
        self.horizontalScrollBar_contrast.valueChanged.connect(self.on_contrast_change)

        self.horizontalScrollBar_sensitivity.valueChanged.connect(self.on_sensitivity_change)

        self.pushButton_first.clicked.connect(self.on_first_button_clicked)
        self.pushButton_last.clicked.connect(self.on_last_button_clicked)
        self.pushButton_prev.clicked.connect(self.on_prev_button_clicked)
        self.pushButton_next.clicked.connect(self.on_next_button_clicked)

        self.pushButton_enableAlarm.clicked.connect(self.on_enable_alarm_change)
        self.pushButton_stopAlarm.clicked.connect(self.on_stop_alarm_clicked)

        self.action_collectData.triggered.connect(self.on_collect_data_triggered)

    def on_collect_data_triggered(self):
        dlg = DataCollectionDialog(self, self.gd_data_handler)
        dlg.exec_()

    def on_stop_alarm_clicked(self):
        self.gpio.alarm_low()
        self.rs845_alarm.turn_off_alarm()

    def on_enable_alarm_change(self):
        if not self.pushButton_enableAlarm.isChecked():
            self.gpio.alarm_low()
            self.rs845_alarm.turn_off_alarm()
            self.gpio.signal_low()
            self.enable_detection_timer = time.time()
        else:
            self.spot_frame_cnt = 0
            self.spot_frame_timer = time.time()

    def on_mode_change(self):
        if self.comboBox_mode.currentIndex() == 0:
            self.fpe.use_cv()
            self.horizontalScrollBar_contrast.setEnabled(True)
            self.update_contrast_label()
        elif self.comboBox_mode.currentIndex() == 1:
            self.fpe.use_yolo()
            self.horizontalScrollBar_contrast.setEnabled(False)
            self.label_contrast.setText("禁用 Disabled")
        self.settings.set_setting_value('mode', self.comboBox_mode.currentIndex())

    def update_pp_to_ui(self, img):
        # noinspection PyArgumentList
        self.label_camViewer.setPixmap(QPixmap.fromImage(img))
        self.process_result()

    def process_result(self):
        ret, result = self.fpe.get()
        img_dir = self.gd_result_handler.result_dir + f"/{get_date_today()}"
        if ret:
            pad_size = 35
            info_str = f"檢測(Detect) FPS: {round(result['detector_fps'])},".ljust(pad_size)
            info_str += f'運算時間(Compute Time):{round((time.time() - result["creation_time"]) * 1000, 2)} ms,'.ljust(
                pad_size)
            info_str += f'畫面更新(Frame update) FPS：{round(1 / (time.time() - self.update_timer), 2)},'.ljust(pad_size)
            info_str += f'異物數量(Number of defects)：{result["num_spots"]}.'.ljust(pad_size)
            self.statusbar.showMessage(info_str)
            if result['num_spots'] > 0 and self.pushButton_enableAlarm.isChecked():
                self.spot_frame_cnt += 1
                if self.spot_frame_cnt > 2:  # TODO Filter accident detection. If there are 2(?) frames within 0.5 sec that num_spot > 1
                    self.gpio.alarm_high()
                    self.rs845_alarm.turn_on_alarm()
                    self.alarm_timer = time.time()
                    self.gpio.signal_high()
                    spot_out = np.concatenate((result['raw'], result['processed']))
                    create_dir_if_not_exists(img_dir)
                    out_path = img_dir + f"/{platform.node()}_SpotImg" + get_current_time_filename() + f"_{int(time.time() * 10) % 3}"
                    img_path = out_path + ".jpg"
                    label_path = out_path + ".txt"
                    cv.imwrite(img_path, spot_out)
                    with open(label_path, "w") as f:
                        for label in result["labels"]:
                            f.write(f"0 {label}\n")
                        f.close()
                    if img_path not in self.spot_img_paths:
                        self.spot_img_paths.append(img_path)
                    Log.info(f"Image saved to: {img_path}")
                    Log.warning(f"Number of spots detected: {result['num_spots']}")
                    self.tabWidget_liveView.setCurrentIndex(1)
                    self.update_img_viewer(len(self.spot_img_paths) - 1)
                    self.spot_frame_cnt = 0
            else:
                if time.time() - self.spot_frame_timer > 0.5:  # TODO Filter accident detection. If there are 2 frames within 0.5(?) sec that num_spot > 1
                    self.spot_frame_cnt = 0
                    self.spot_frame_timer = time.time()
                if self.alarm_timer > 0 and time.time() - self.alarm_timer > 0.5:
                    self.gpio.signal_low()
                    if time.time() - self.alarm_timer > 6:
                        self.gpio.alarm_low()
                        self.rs845_alarm.turn_off_alarm()

            # Collect training data
            self.raw_target = self.gd_data_handler.get_raw_target_today()
            if self.pushButton_enableAlarm.isChecked() and result['num_spots'] == 0 and self.raw_target > 0:
                img_out = self.gd_data_handler.get_local_raw_img_dir_today() + f"/{platform.node()}_raw_{get_current_time_filename()}_{self.raw_target}.jpg"
                cv.imwrite(img_out, result['raw'])
                self.gd_data_handler.record_new_raw_timestamp()
                Log.info(f"Raw image{self.raw_target} has been saved to{img_out}")

            if not self.pushButton_enableAlarm.isChecked() and time.time() - self.enable_detection_timer > _ENABLE_DETECTION_TIME:
                self.pushButton_enableAlarm.setChecked(True)
                self.pushButton_enableAlarm.setText(f"檢測中(Working)")
            elif not self.pushButton_enableAlarm.isChecked():
                self.pushButton_enableAlarm.setText(
                    f"啓動檢測(Start) {round(_ENABLE_DETECTION_TIME - time.time() + self.enable_detection_timer)} s")
                self.alarm_timer = -1
            else:
                self.pushButton_enableAlarm.setText(f"檢測中(Working)")
            self.put(result)
            self.update_timer = time.time()

    def update_img_viewer(self, idx: int):
        existing_imgs = []
        for img in self.spot_img_paths:
            if os.path.exists(img):
                existing_imgs.append(img)
        existing_imgs = sorted(list(set(existing_imgs)))
        if len(self.spot_img_paths) > 0 and self.spot_img_paths[idx] in existing_imgs:
            idx = existing_imgs.index(self.spot_img_paths[idx])
        else:
            idx = len(existing_imgs) - 1
        self.spot_img_paths = existing_imgs
        if idx >= 0 and len(self.spot_img_paths) > 0:
            self.label_resultInfobox.setText(
                f"檢測圖像(Result Frame)[{idx + 1} / {len(self.spot_img_paths)}]: {self.spot_img_paths[idx].split('/')[-1]}")
            img = QPixmap(self.spot_img_paths[idx])
            img_scaled = img.scaled(int(img.width() * 720 / img.height()), 720)
            self.label_resultViewer.setPixmap(img_scaled)
            self.spot_img_path_idx = idx

    def ask_reboot(self):
        msg = QMessageBox()
        msg.setWindowTitle("重新啓動(Reboot)")
        msg.setText(
            "確認重新啓動？\n將會在上傳檢測結果後自動重新啓動。\nConfirm reboot the computer?\nThe computer will reboot after uploading the results.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setIcon(QMessageBox.Warning)
        ret = msg.exec_()
        if ret == QMessageBox.Ok:
            Log.info("System Reboot...")
            self.exit_procedure()
            self.qt_app.exit(888)
            # os.system('reboot')

    def ask_poweroff(self):
        msg = QMessageBox()
        msg.setWindowTitle("關機(Shutdown)")
        msg.setText(
            "確認關機？\n將會在上傳檢測結果後自動關機。\nConfirm shutdown the computer?\nThe computer wil shutdown after uploading the results.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setIcon(QMessageBox.Warning)
        ret = msg.exec_()
        if ret == QMessageBox.Ok:
            Log.info("System power off...")
            self.exit_procedure()
            self.qt_app.exit(999)
            # os.system('poweroff')

    # def ask_stopApp(self, event):
    #     msg = QMessageBox()
    #     msg.setWindowTitle("退出(Exit Program)")
    #     msg.setText("確認退出？\n異物檢測程式將會在上傳檢測結果後自動退出。\nConfirm Exit?\nThe program will exit after uploading the results.")
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.setIcon(QMessageBox.Warning)
    #     ret = msg.exec_()
    #     if ret == QMessageBox.Ok:
    #         Log.info("Program exit.")
    #         self.exit_procedure()
    #         self.qt_app.closeAllWindows()
    #         event.accept()
    #     else:
    #         event.ignore()

    def exit_procedure(self):
        Log.info(f"Exiting procedure in progress...")
        self.gd_result_handler.thread_stop()
        self.gd_data_handler.thread_stop()
        self.tabWidget_liveView.setCurrentIndex(0)
        self.statusbar.showMessage(f"退出中, 請稍等... Exiting, please wait...  [關閉探測器引擎(Frame Processing Engine)]")
        self.label_infobox.setText(f"退出中, 請稍等... Exiting, please wait...  [關閉探測器引擎(Frame Processing Engine)]")
        self.fpe.stop()
        self.statusbar.showMessage(f"退出中, 請稍等... Exiting, please wait...  [保存配置(Saving Configuration)]")
        self.label_infobox.setText(f"退出中, 請稍等... Exiting, please wait...  [保存配置(Saving Configuration)]")
        self.settings.save_config_to_file()
        self.statusbar.showMessage(f"退出中, 請稍等... Exiting, please wait...  [同步結果(Synchronizing results)]")
        self.label_infobox.setText(f"退出中, 請稍等... Exiting, please wait...  [同步結果(Synchronizing results)]")
        self.gd_result_handler.thread_join()
        self.gd_data_handler.thread_join()
        Log.info(f"Exiting procedure done.")

    def ask_stopApp(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("退出(Exit)?")
        msg.setText("確認退出？\n異物檢測程式將會在上傳檢測結果後自動退出。\nConfirm Exit?\nThe program will exit after uploading the results.")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setIcon(QMessageBox.Warning)
        ret = msg.exec_()
        if ret == QMessageBox.Ok:
            Log.info("Program exit.")
            self.exit_procedure()
            self.qt_app.closeAllWindows()
            event.accept()
        else:
            event.ignore()

    def launch(self):
        self.MainWindow.show()
        self.gd_result_handler.thread_start()
        self.gd_data_handler.thread_start()
        self.fpe.start()
        _exit_code = self.qt_app.exec_()
        self.gpio.cleanup()
        return _exit_code


if __name__ == '__main__':
    print(f"Start")
    app = DetectorApp()
    _ENABLE_DETECTION_TIME = 72000
    exit_code = app.launch()
    print(f"End {exit_code}")
    sys.exit(exit_code)

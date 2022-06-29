import platform
import threading

import cv2 as cv
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog

from ContinuousLearner import ContinuousLearner
from Detector import BufferPackedResult
from libs.Log import Log
from libs.utils import get_current_time_filename


class DataCollectionDialog(QDialog):
    def __init__(self, buffer: BufferPackedResult, gd_data_handler: ContinuousLearner, parent=None):
        super().__init__(parent)
        self.buffer = buffer
        self.data_handler = gd_data_handler
        self.setWindowTitle("數據採集(Data Collection)")

        msg = QtWidgets.QLabel("Please set the number of samples:")

        self.dc_num_slider = QtWidgets.QSlider()
        self.dc_num_slider.setOrientation(QtCore.Qt.Horizontal)
        self.dc_num_slider.setMinimum(10)
        self.dc_num_slider.setMaximum(5000)
        self.dc_num_slider.setValue(2000)
        self.dc_num_slider.valueChanged.connect(self.on_slider_changed)
        self.label_dc_num = QtWidgets.QLabel(f"{self.dc_num_slider.value()}")

        self.progress_bar = QtWidgets.QProgressBar()

        self.btn_capture = QtWidgets.QPushButton("Capture")
        self.btn_capture.clicked.connect(self.on_capture_clicked)

        self.btn_stop = QtWidgets.QPushButton("Stop")
        self.stop_cap = False
        self.btn_stop.clicked.connect(self.on_stop_clicked)

        self.btn_exit = QtWidgets.QPushButton("Exit")
        # self.btn_exit.clicked.connect(lambda: self.done(0))
        self.btn_exit.clicked.connect(self.on_exit_clicked)

        dc_layout_v = QtWidgets.QVBoxLayout()
        dc_layout_v.addWidget(msg)

        dc_layout_h = QtWidgets.QHBoxLayout()
        dc_layout_h.addWidget(self.dc_num_slider)
        dc_layout_h.addWidget(self.label_dc_num)
        dc_layout_v.addLayout(dc_layout_h)

        dc_layout_v.addWidget(self.progress_bar)

        dc_layout_h = QtWidgets.QHBoxLayout()
        dc_layout_h.addWidget(self.btn_capture)
        dc_layout_h.addWidget(self.btn_stop)
        dc_layout_h.addWidget(self.btn_exit)
        dc_layout_v.addLayout(dc_layout_h)

        self.setLayout(dc_layout_v)

    def on_exit_clicked(self):
        self.stop_cap = True
        self.done(0)

    def on_stop_clicked(self):
        self.stop_cap = True

    def on_capture_clicked(self):
        self.progress_bar.setMaximum(self.dc_num_slider.value())
        cap_thread = threading.Thread(target=self.capture_sample)
        cap_thread.setDaemon(True)
        cap_thread.start()

    def capture_sample(self):
        target = self.progress_bar.maximum()
        cap_cnt = 0
        self.btn_capture.setEnabled(False)
        while cap_cnt < target and not self.stop_cap:
            ret, result = self.buffer.get()
            if ret and result['num_spots'] == 0:
                cap_cnt += 1
                img_out = self.data_handler.get_local_raw_img_dir_today() + f"/{platform.node()}_raw_{get_current_time_filename()}_{cap_cnt}.jpg"
                cv.imwrite(img_out, result['raw'])
                self.data_handler.record_new_raw_timestamp()
                Log.info(f"Raw image{cap_cnt} has been saved to{img_out}")
                self.progress_bar.setValue(cap_cnt)
                self.progress_bar.setFormat(f"{cap_cnt}/{target}")
        self.btn_capture.setEnabled(True)
        self.stop_cap = False
        self.data_handler.sync_raw_to_gd_now()

    def on_slider_changed(self):
        self.label_dc_num.setText(f"{self.dc_num_slider.value()}")

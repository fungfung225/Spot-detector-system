# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2022.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1030)
        # MainWindow.setMinimumSize(QtCore.QSize(1920, 1030))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1030))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./logo/Asset 8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1310, 125, 171, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_34.setObjectName("label_34")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1290, 270, 602, 92))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_offsetRight = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_offsetRight.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_offsetRight.setFont(font)
        self.label_offsetRight.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_offsetRight.setLineWidth(0)
        self.label_offsetRight.setObjectName("label_offsetRight")
        self.gridLayout_2.addWidget(self.label_offsetRight, 0, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setMinimumSize(QtCore.QSize(80, 0))
        self.label_30.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 0, 1, 1)
        self.horizontalScrollBar_offsetRight = QtWidgets.QScrollBar(self.layoutWidget_3)
        self.horizontalScrollBar_offsetRight.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_offsetRight.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_offsetRight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_offsetRight.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_offsetRight.setMaximum(600)
        self.horizontalScrollBar_offsetRight.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_offsetRight.setObjectName("horizontalScrollBar_offsetRight")
        self.gridLayout_2.addWidget(self.horizontalScrollBar_offsetRight, 1, 0, 1, 2)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(1290, 370, 602, 92))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_offsetUp = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_offsetUp.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_offsetUp.setFont(font)
        self.label_offsetUp.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_offsetUp.setLineWidth(0)
        self.label_offsetUp.setObjectName("label_offsetUp")
        self.gridLayout_4.addWidget(self.label_offsetUp, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_33.setMinimumSize(QtCore.QSize(80, 0))
        self.label_33.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 0, 0, 1, 1)
        self.horizontalScrollBar_offsetUp = QtWidgets.QScrollBar(self.layoutWidget_4)
        self.horizontalScrollBar_offsetUp.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_offsetUp.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_offsetUp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_offsetUp.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_offsetUp.setMaximum(600)
        self.horizontalScrollBar_offsetUp.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_offsetUp.setObjectName("horizontalScrollBar_offsetUp")
        self.gridLayout_4.addWidget(self.horizontalScrollBar_offsetUp, 1, 0, 1, 2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(1290, 470, 602, 92))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_offsetDown = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_offsetDown.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_offsetDown.setFont(font)
        self.label_offsetDown.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_offsetDown.setLineWidth(0)
        self.label_offsetDown.setObjectName("label_offsetDown")
        self.gridLayout_5.addWidget(self.label_offsetDown, 0, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_37.setMinimumSize(QtCore.QSize(80, 0))
        self.label_37.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_37.setObjectName("label_37")
        self.gridLayout_5.addWidget(self.label_37, 0, 0, 1, 1)
        self.horizontalScrollBar_offsetDown = QtWidgets.QScrollBar(self.layoutWidget_5)
        self.horizontalScrollBar_offsetDown.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_offsetDown.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_offsetDown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_offsetDown.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_offsetDown.setMaximum(600)
        self.horizontalScrollBar_offsetDown.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_offsetDown.setObjectName("horizontalScrollBar_offsetDown")
        self.gridLayout_5.addWidget(self.horizontalScrollBar_offsetDown, 1, 0, 1, 2)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(1290, 570, 602, 92))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_contrast = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.gridLayout_contrast.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_contrast.setSpacing(0)
        self.gridLayout_contrast.setObjectName("gridLayout_contrast")
        self.label_contrast = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_contrast.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_contrast.setFont(font)
        self.label_contrast.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_contrast.setLineWidth(0)
        self.label_contrast.setObjectName("label_contrast")
        self.gridLayout_contrast.addWidget(self.label_contrast, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_38.setMinimumSize(QtCore.QSize(80, 0))
        self.label_38.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_38.setObjectName("label_38")
        self.gridLayout_contrast.addWidget(self.label_38, 0, 0, 1, 1)
        self.horizontalScrollBar_contrast = QtWidgets.QScrollBar(self.layoutWidget_7)
        self.horizontalScrollBar_contrast.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_contrast.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_contrast.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_contrast.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_contrast.setMaximum(200)
        self.horizontalScrollBar_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_contrast.setObjectName("horizontalScrollBar_contrast")
        self.gridLayout_contrast.addWidget(self.horizontalScrollBar_contrast, 1, 0, 1, 2)
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(1310, 700, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_39.setObjectName("label_39")
        self.layoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(1290, 740, 602, 112))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_8)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_41 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_41.setMinimumSize(QtCore.QSize(80, 0))
        self.label_41.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_41.setObjectName("label_41")
        self.gridLayout_7.addWidget(self.label_41, 0, 0, 1, 1)
        self.horizontalScrollBar_sensitivity = QtWidgets.QScrollBar(self.layoutWidget_8)
        self.horizontalScrollBar_sensitivity.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_sensitivity.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_sensitivity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_sensitivity.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_sensitivity.setMaximum(1000)
        self.horizontalScrollBar_sensitivity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_sensitivity.setObjectName("horizontalScrollBar_sensitivity")
        self.gridLayout_7.addWidget(self.horizontalScrollBar_sensitivity, 1, 0, 1, 2)
        self.label_sensitivity = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_sensitivity.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_sensitivity.setFont(font)
        self.label_sensitivity.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_sensitivity.setLineWidth(0)
        self.label_sensitivity.setObjectName("label_sensitivity")
        self.gridLayout_7.addWidget(self.label_sensitivity, 0, 1, 1, 1)
        self.layoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(1300, 890, 601, 81))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(39)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_stopAlarm = QtWidgets.QPushButton(self.layoutWidget_9)
        self.pushButton_stopAlarm.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_stopAlarm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stopAlarm.setFont(font)
        self.pushButton_stopAlarm.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.528409, y2:0.971591, stop:0 rgba(255, 0, 0, 22), stop:1 rgba(255, 0, 0, 157));\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(255, 70, 73);\n"
"     border-radius: 12px;\n"
"}\n"
"QPushButton:checked {\n"
"     background-color: rgb(203, 0, 0);\n"
"}")
        self.pushButton_stopAlarm.setCheckable(False)
        self.pushButton_stopAlarm.setObjectName("pushButton_stopAlarm")
        self.horizontalLayout_21.addWidget(self.pushButton_stopAlarm)
        self.pushButton_enableAlarm = QtWidgets.QPushButton(self.layoutWidget_9)
        self.pushButton_enableAlarm.setEnabled(True)
        self.pushButton_enableAlarm.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_enableAlarm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_enableAlarm.setFont(font)
        self.pushButton_enableAlarm.setStyleSheet("QPushButton:checked{\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 253, 114, 255), stop:1 rgba(76, 255, 114, 100));\n"
"     border-radius: 20px;\n"
"    \n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(184, 184, 184);\n"
"     border-radius: 20px;\n"
"}")
        self.pushButton_enableAlarm.setCheckable(True)
        self.pushButton_enableAlarm.setChecked(False)
        self.pushButton_enableAlarm.setObjectName("pushButton_enableAlarm")
        self.horizontalLayout_21.addWidget(self.pushButton_enableAlarm)
        self.tabWidget_liveView = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_liveView.setGeometry(QtCore.QRect(10, 140, 1283, 760))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget_liveView.setFont(font)
        self.tabWidget_liveView.setStyleSheet("\n"
"border-color: rgba(191, 64, 64, 0);")
        self.tabWidget_liveView.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.HongKong))
        self.tabWidget_liveView.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_liveView.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_liveView.setUsesScrollButtons(False)
        self.tabWidget_liveView.setTabBarAutoHide(False)
        self.tabWidget_liveView.setObjectName("tabWidget_liveView")
        self.tab_camViewer = QtWidgets.QWidget()
        self.tab_camViewer.setMinimumSize(QtCore.QSize(1280, 720))
        self.tab_camViewer.setMaximumSize(QtCore.QSize(840, 470))
        self.tab_camViewer.setAutoFillBackground(False)
        self.tab_camViewer.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.tab_camViewer.setObjectName("tab_camViewer")
        self.label_camViewer = QtWidgets.QLabel(self.tab_camViewer)
        self.label_camViewer.setGeometry(QtCore.QRect(3, 3, 1280, 720))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_camViewer.setFont(font)
        self.label_camViewer.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label_camViewer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camViewer.setObjectName("label_camViewer")
        self.label_infobox = QtWidgets.QLabel(self.tab_camViewer)
        self.label_infobox.setGeometry(QtCore.QRect(10, 10, 1261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_infobox.setFont(font)
        self.label_infobox.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_infobox.setText("")
        self.label_infobox.setObjectName("label_infobox")
        self.tabWidget_liveView.addTab(self.tab_camViewer, "")
        self.tab_resultViewer = QtWidgets.QWidget()
        self.tab_resultViewer.setMinimumSize(QtCore.QSize(1280, 720))
        self.tab_resultViewer.setMaximumSize(QtCore.QSize(840, 470))
        self.tab_resultViewer.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.tab_resultViewer.setObjectName("tab_resultViewer")
        self.label_resultViewer = QtWidgets.QLabel(self.tab_resultViewer)
        self.label_resultViewer.setGeometry(QtCore.QRect(3, 3, 1280, 720))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_resultViewer.setFont(font)
        self.label_resultViewer.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"color: rgb(255, 255, 255);")
        self.label_resultViewer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultViewer.setObjectName("label_resultViewer")
        self.pushButton_first = QtWidgets.QPushButton(self.tab_resultViewer)
        self.pushButton_first.setGeometry(QtCore.QRect(12, 280, 40, 180))
        self.pushButton_first.setMinimumSize(QtCore.QSize(40, 180))
        self.pushButton_first.setMaximumSize(QtCore.QSize(30, 180))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_first.setFont(font)
        self.pushButton_first.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}\n"
"QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0.495, y1:1, x2:0.488636, y2:0, stop:0 rgba(255, 255, 255, 224), stop:1 rgba(255, 255, 255, 255));\n"
"     border-radius: 5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_first.setObjectName("pushButton_first")
        self.pushButton_prev = QtWidgets.QPushButton(self.tab_resultViewer)
        self.pushButton_prev.setGeometry(QtCore.QRect(57, 280, 40, 180))
        self.pushButton_prev.setMinimumSize(QtCore.QSize(40, 180))
        self.pushButton_prev.setMaximumSize(QtCore.QSize(30, 180))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_prev.setFont(font)
        self.pushButton_prev.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}\n"
"QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0.495, y1:1, x2:0.488636, y2:0, stop:0 rgba(255, 255, 255, 224), stop:1 rgba(255, 255, 255, 255));\n"
"     border-radius: 5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.pushButton_next = QtWidgets.QPushButton(self.tab_resultViewer)
        self.pushButton_next.setGeometry(QtCore.QRect(1185, 280, 40, 180))
        self.pushButton_next.setMinimumSize(QtCore.QSize(40, 180))
        self.pushButton_next.setMaximumSize(QtCore.QSize(30, 180))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}\n"
"QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0.495, y1:1, x2:0.488636, y2:0, stop:0 rgba(255, 255, 255, 224), stop:1 rgba(255, 255, 255, 255));\n"
"     border-radius: 5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_resultInfobox = QtWidgets.QLabel(self.tab_resultViewer)
        self.label_resultInfobox.setGeometry(QtCore.QRect(20, 13, 1241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_resultInfobox.setFont(font)
        self.label_resultInfobox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(170, 0, 0);")
        self.label_resultInfobox.setText("")
        self.label_resultInfobox.setObjectName("label_resultInfobox")
        self.pushButton_last = QtWidgets.QPushButton(self.tab_resultViewer)
        self.pushButton_last.setGeometry(QtCore.QRect(1230, 280, 40, 180))
        self.pushButton_last.setMinimumSize(QtCore.QSize(40, 180))
        self.pushButton_last.setMaximumSize(QtCore.QSize(30, 180))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_last.setFont(font)
        self.pushButton_last.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}\n"
"QPushButton {\n"
"     background-color: qlineargradient(spread:pad, x1:0.495, y1:1, x2:0.488636, y2:0, stop:0 rgba(255, 255, 255, 224), stop:1 rgba(255, 255, 255, 255));\n"
"     border-radius: 5px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_last.setObjectName("pushButton_last")
        self.tabWidget_liveView.addTab(self.tab_resultViewer, "")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1307, 860, 581, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1310, 660, 581, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1310, 90, 581, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1290, 170, 602, 92))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_offsetLeft = QtWidgets.QLabel(self.layoutWidget)
        self.label_offsetLeft.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_offsetLeft.setFont(font)
        self.label_offsetLeft.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_offsetLeft.setLineWidth(0)
        self.label_offsetLeft.setObjectName("label_offsetLeft")
        self.gridLayout.addWidget(self.label_offsetLeft, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setMinimumSize(QtCore.QSize(80, 0))
        self.label_29.setMaximumSize(QtCore.QSize(205, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 0, 1, 1)
        self.horizontalScrollBar_offsetLeft = QtWidgets.QScrollBar(self.layoutWidget)
        self.horizontalScrollBar_offsetLeft.setMinimumSize(QtCore.QSize(500, 50))
        self.horizontalScrollBar_offsetLeft.setMaximumSize(QtCore.QSize(600, 16777215))
        self.horizontalScrollBar_offsetLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalScrollBar_offsetLeft.setStyleSheet("QScrollBar:horizontal {\n"
"    border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"    width: 5px;\n"
"    margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgba(16, 104, 106,200);\n"
"    min-height: 30px;\n"
"    min-width: 30px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"  background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(76, 178, 158);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_offsetLeft.setMaximum(600)
        self.horizontalScrollBar_offsetLeft.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_offsetLeft.setObjectName("horizontalScrollBar_offsetLeft")
        self.gridLayout.addWidget(self.horizontalScrollBar_offsetLeft, 1, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1320, 20, 541, 82))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_36 = QtWidgets.QLabel(self.widget)
        self.label_36.setMaximumSize(QtCore.QSize(231, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_2.addWidget(self.label_36)
        self.comboBox_mode = QtWidgets.QComboBox(self.widget)
        self.comboBox_mode.setMinimumSize(QtCore.QSize(200, 60))
        self.comboBox_mode.setMaximumSize(QtCore.QSize(256, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_mode.setFont(font)
        self.comboBox_mode.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 178, 158, 100));\n"
"border-radius: 5px;\n"
"color: rgb(243, 243, 243);")
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_mode)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Savewo_logo = QtWidgets.QLabel(self.widget1)
        self.label_Savewo_logo.setMinimumSize(QtCore.QSize(100, 76))
        self.label_Savewo_logo.setMaximumSize(QtCore.QSize(350, 94))
        self.label_Savewo_logo.setText("")
        self.label_Savewo_logo.setPixmap(QtGui.QPixmap("./logo/Asset 5.png"))
        self.label_Savewo_logo.setScaledContents(True)
        self.label_Savewo_logo.setObjectName("label_Savewo_logo")
        self.horizontalLayout_4.addWidget(self.label_Savewo_logo)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(50, 898, 1141, 73))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_reboot = QtWidgets.QPushButton(self.widget2)
        self.pushButton_reboot.setEnabled(True)
        self.pushButton_reboot.setMinimumSize(QtCore.QSize(180, 50))
        self.pushButton_reboot.setMaximumSize(QtCore.QSize(230, 55))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 92, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_reboot.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_reboot.setFont(font)
        self.pushButton_reboot.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(206, 92, 0);\n"
"     border-radius: 20px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_reboot.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_reboot.setCheckable(False)
        self.pushButton_reboot.setObjectName("pushButton_reboot")
        self.horizontalLayout.addWidget(self.pushButton_reboot)
        self.pushButton_poweroff = QtWidgets.QPushButton(self.widget2)
        self.pushButton_poweroff.setEnabled(True)
        self.pushButton_poweroff.setMinimumSize(QtCore.QSize(180, 50))
        self.pushButton_poweroff.setMaximumSize(QtCore.QSize(230, 55))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_poweroff.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_poweroff.setFont(font)
        self.pushButton_poweroff.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(164, 0, 0);\n"
"     border-radius: 20px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_poweroff.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_poweroff.setCheckable(False)
        self.pushButton_poweroff.setObjectName("pushButton_poweroff")
        self.horizontalLayout.addWidget(self.pushButton_poweroff)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.widget2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget2)
        self.pushButton_exit.setEnabled(True)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(170, 50))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(200, 55))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 162, 162, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_exit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(46, 52, 54);\n"
"    color: rgb(255, 162, 162);\n"
"     border-radius: 20px;\n"
"    border:none;\n"
"}\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0))\n"
"}")
        self.pushButton_exit.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_exit.setCheckable(False)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_5.addWidget(self.pushButton_exit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1294, 0, 620, 978))
        self.label_3.setMinimumSize(QtCore.QSize(0, 800))
        self.label_3.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"border-radius: 15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 699, 109))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 80, 700, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(1440, 128, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_35.setObjectName("label_35")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(1440, 703, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_40.setObjectName("label_40")
        self.label_3.raise_()
        self.label_34.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()
        self.layoutWidget_5.raise_()
        self.layoutWidget_7.raise_()
        self.label_39.raise_()
        self.layoutWidget_8.raise_()
        self.layoutWidget_9.raise_()
        self.tabWidget_liveView.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.layoutWidget.raise_()
        self.widget.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_35.raise_()
        self.label_40.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_otherFunctions = QtWidgets.QMenu(self.menubar)
        self.menu_otherFunctions.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.menu_otherFunctions.setFont(font)
        self.menu_otherFunctions.setObjectName("menu_otherFunctions")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.menu_Help.setFont(font)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_collectData = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.action_collectData.setFont(font)
        self.action_collectData.setObjectName("action_collectData")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_otherFunctions.addAction(self.action_collectData)
        self.menu_Help.addAction(self.action)
        self.menubar.addAction(self.menu_otherFunctions.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_liveView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Savewo Fabric Defects Detection System"))
        self.label_34.setText(_translate("MainWindow", "畫面調整"))
        self.label_offsetRight.setText(_translate("MainWindow", "123"))
        self.label_30.setText(_translate("MainWindow", "右邊界(Right):"))
        self.label_offsetUp.setText(_translate("MainWindow", "123"))
        self.label_33.setText(_translate("MainWindow", "上邊界(Top):"))
        self.label_offsetDown.setText(_translate("MainWindow", "123"))
        self.label_37.setText(_translate("MainWindow", "下邊界(Bottom):"))
        self.label_contrast.setText(_translate("MainWindow", "123"))
        self.label_38.setText(_translate("MainWindow", "對比度(Contrast):"))
        self.label_39.setText(_translate("MainWindow", "檢測參數"))
        self.label_41.setText(_translate("MainWindow", "靈敏度(Sensitivity):"))
        self.label_sensitivity.setText(_translate("MainWindow", "123"))
        self.pushButton_stopAlarm.setText(_translate("MainWindow", "停止警報(Mute)"))
        self.pushButton_enableAlarm.setText(_translate("MainWindow", "啟動檢測(Start) 180s"))
        self.label_camViewer.setText(_translate("MainWindow", "相機畫面(Camera View)"))
        self.tabWidget_liveView.setTabText(self.tabWidget_liveView.indexOf(self.tab_camViewer), _translate("MainWindow", " 相機畫面(Live View) "))
        self.label_resultViewer.setText(_translate("MainWindow", " 檢測圖像(Detection result) "))
        self.pushButton_first.setText(_translate("MainWindow", "|<"))
        self.pushButton_prev.setText(_translate("MainWindow", "<"))
        self.pushButton_next.setText(_translate("MainWindow", ">"))
        self.pushButton_last.setText(_translate("MainWindow", ">|"))
        self.tabWidget_liveView.setTabText(self.tabWidget_liveView.indexOf(self.tab_resultViewer), _translate("MainWindow", " 檢測圖像(Detection Result) "))
        self.label_offsetLeft.setText(_translate("MainWindow", "123"))
        self.label_29.setText(_translate("MainWindow", "左邊界(Left):"))
        self.label_36.setText(_translate("MainWindow", " 模式(Mode):"))
        self.comboBox_mode.setCurrentText(_translate("MainWindow", " 機器視覺（CV）"))
        self.comboBox_mode.setItemText(0, _translate("MainWindow", " 機器視覺（CV）"))
        self.comboBox_mode.setItemText(1, _translate("MainWindow", "  AI-Yolo5 (Beta)"))
        self.pushButton_reboot.setText(_translate("MainWindow", "重啓(Reboot)"))
        self.pushButton_poweroff.setText(_translate("MainWindow", "關機(Power off)"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出(Exit)"))
        self.label.setText(_translate("MainWindow", "   救世布料檢測系統"))
        self.label_4.setText(_translate("MainWindow", "Savewo Fabric Defects Detection System"))
        self.label_35.setText(_translate("MainWindow", "Frame Adjustment"))
        self.label_40.setText(_translate("MainWindow", "Detection Parameter"))
        self.menu_otherFunctions.setTitle(_translate("MainWindow", "其他功能(Other)"))
        self.menu_Help.setTitle(_translate("MainWindow", "幫助(Help)"))
        self.action_collectData.setText(_translate("MainWindow", "數據採集(Data Collection)"))
        self.action.setText(_translate("MainWindow", "使用說明(User Instruction)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


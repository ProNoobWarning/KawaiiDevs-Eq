# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.OpenFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.verticalLayout_3.addWidget(self.OpenFileButton)
        self.PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlayButton.setObjectName("PlayButton")
        self.verticalLayout_3.addWidget(self.PlayButton)
        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setObjectName("PauseButton")
        self.verticalLayout_3.addWidget(self.PauseButton)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.verticalLayout_3.addWidget(self.SaveButton)
        self.CompareButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompareButton.setObjectName("CompareButton")
        self.verticalLayout_3.addWidget(self.CompareButton)
        self.ClearComparedButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearComparedButton.setObjectName("ClearComparedButton")
        self.verticalLayout_3.addWidget(self.ClearComparedButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.OnOff = QtWidgets.QPushButton(self.centralwidget)
        self.OnOff.setObjectName("OnOff")
        self.verticalLayout_4.addWidget(self.OnOff)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setStyleSheet("margin:auto;")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalLayout_5.addWidget(self.verticalSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setStyleSheet("margin:auto;")
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalLayout_9.addWidget(self.verticalSlider_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setStyleSheet("margin:auto;")
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.verticalLayout_10.addWidget(self.verticalSlider_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_12.addWidget(self.label_8)
        self.verticalSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_8.setStyleSheet("margin:auto;")
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.verticalLayout_12.addWidget(self.verticalSlider_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.verticalSlider_11 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_11.setStyleSheet("margin:auto;")
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.verticalLayout_15.addWidget(self.verticalSlider_11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.verticalSlider_10 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_10.setStyleSheet("margin:auto;")
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.verticalLayout_14.addWidget(self.verticalSlider_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.verticalSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_9.setStyleSheet("margin:auto;")
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.verticalLayout_13.addWidget(self.verticalSlider_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setStyleSheet("margin:auto;")
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalLayout_8.addWidget(self.verticalSlider_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.verticalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_7.setStyleSheet("margin:auto;")
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.verticalLayout_11.addWidget(self.verticalSlider_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setStyleSheet("margin:auto;")
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_7.addWidget(self.verticalSlider_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.verticalSlider_12 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_12.setStyleSheet("margin:auto;")
        self.verticalSlider_12.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_12.setObjectName("verticalSlider_12")
        self.verticalLayout_16.addWidget(self.verticalSlider_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_17.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFileButton.setText(_translate("MainWindow", "Open File"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.CompareButton.setText(_translate("MainWindow", "Compare To"))
        self.ClearComparedButton.setText(_translate("MainWindow", "Clear Compared"))
        self.OnOff.setText(_translate("MainWindow", "ON/OFF"))
        self.label.setText(_translate("MainWindow", "25 Hz"))
        self.label_5.setText(_translate("MainWindow", "2 KHz"))
        self.label_6.setText(_translate("MainWindow", "4 KHz"))
        self.label_8.setText(_translate("MainWindow", "6 KHz"))
        self.label_11.setText(_translate("MainWindow", "8 KHz"))
        self.label_10.setText(_translate("MainWindow", "10 KHz"))
        self.label_9.setText(_translate("MainWindow", "12 KHz"))
        self.label_4.setText(_translate("MainWindow", "14 KHz"))
        self.label_7.setText(_translate("MainWindow", "16 KHz"))
        self.label_3.setText(_translate("MainWindow", "18 KHz"))
        self.label_12.setText(_translate("MainWindow", "20 KHz"))

from pyqtgraph import PlotWidget

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\khura\Desktop\QtGUI\Frequency to Delay Calculator\UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os.path
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import uic as uic

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimedia,QtLocation, QtPositioning

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 70)
        Dialog.setMinimumSize(QtCore.QSize(524, 70))
        Dialog.setMaximumSize(QtCore.QSize(524, 70))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd()+"\FreqToDelayCalculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 12, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 40, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 51, 16))
        self.label_5.setObjectName("label_5")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        """     
        mapp = QtLocation.QGeoRoute
        place = QtLocation.QPlace
        place.setName("A sample")
        location = QtPositioning.QGeoLocation
        location.setCoordinate(QtPositioning.QGeoLocation(12.34, 56.78))
        address = QtPositioning.QGeoAddress
        address.setStreet("111 Norther Street")
        location.setAddress(address)
        place.setLocation(location)
        """


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delay to Frequency Calculator"))
        self.lineEdit.setText(_translate("Dialog", "1000"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "ms"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.label.setText(_translate("Dialog", "="))
        self.label_2.setText(_translate("Dialog", "Hz"))
        self.label_3.setText(_translate("Dialog", "Value"))
        self.label_4.setText(_translate("Dialog", "Unit"))
        self.label_5.setText(_translate("Dialog", "Frequency"))
        self.pushButton.clicked.connect(self.calculate_value)
        
    def calculate_value(self):
        valuestring = "0"
        try:
            prescalerstring = self.plainTextEdit.toPlainText()
        except ValueError:
            self.lcdNumber.display("Error")

        try:
            prescaler = 0;
            if (prescalerstring == "ms"):
              prescaler = 1000
            elif (prescalerstring == "us"):
                prescaler = 1000000

            elif (prescalerstring == "ns"):
                prescaler = 1000000000
            elif (prescalerstring == "s"):
                prescaler = 1
            value = prescaler / (float(self.lineEdit.text()))
            if(value>=1000):
                valuestring = (str(value/1000)+"K")
            self.lcdNumber.display(value)
        except ValueError:
            self.lcdNumber.display("Error")


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
#ui.lcdNumber.display(ui.verticalSlider.value())
ui.setupUi(window)

window.show()
sys.exit(app.exec_())

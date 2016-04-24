# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Fri Apr  8 23:31:42 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Mosaic(object):
    def setupUi(self, Mosaic):
        Mosaic.setObjectName(_fromUtf8("Mosaic"))
        Mosaic.resize(393, 178)
        Mosaic.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.startButton = QtGui.QPushButton(Mosaic)
        self.startButton.setGeometry(QtCore.QRect(270, 130, 98, 27))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.editDirPath = QtGui.QLineEdit(Mosaic)
        self.editDirPath.setGeometry(QtCore.QRect(30, 60, 221, 31))
        self.editDirPath.setReadOnly(True)
        self.editDirPath.setObjectName(_fromUtf8("editDirPath"))
        self.dirPickLabel = QtGui.QLabel(Mosaic)
        self.dirPickLabel.setGeometry(QtCore.QRect(30, 40, 131, 16))
        self.dirPickLabel.setObjectName(_fromUtf8("dirPickLabel"))
        self.openButton = QtGui.QPushButton(Mosaic)
        self.openButton.setGeometry(QtCore.QRect(270, 60, 98, 27))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.widthSpinBox = QtGui.QSpinBox(Mosaic)
        self.widthSpinBox.setGeometry(QtCore.QRect(30, 120, 60, 27))
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.heightSpinBox = QtGui.QSpinBox(Mosaic)
        self.heightSpinBox.setGeometry(QtCore.QRect(130, 120, 60, 27))
        self.heightSpinBox.setObjectName(_fromUtf8("heightSpinBox"))
        self.widthLabel = QtGui.QLabel(Mosaic)
        self.widthLabel.setGeometry(QtCore.QRect(30, 100, 66, 17))
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.heightLabel = QtGui.QLabel(Mosaic)
        self.heightLabel.setGeometry(QtCore.QRect(130, 100, 66, 17))
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))

        self.retranslateUi(Mosaic)
        QtCore.QMetaObject.connectSlotsByName(Mosaic)

    def retranslateUi(self, Mosaic):
        Mosaic.setWindowTitle(_translate("Mosaic", "Mosaic", None))
        self.startButton.setText(_translate("Mosaic", "Start", None))
        self.dirPickLabel.setText(_translate("Mosaic", "Choose directory", None))
        self.openButton.setText(_translate("Mosaic", "Open", None))
        self.widthLabel.setText(_translate("Mosaic", "Width", None))
        self.heightLabel.setText(_translate("Mosaic", "Height", None))


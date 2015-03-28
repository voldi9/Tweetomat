# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updating.ui'
#
# Created: Wed Feb  5 19:34:06 2014
#      by: PyQt4 UI code generator 4.10
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

#Class represents the dialog informing about database updating in progress
class Ui_updating(object):
    def setupUi(self, updating):
        updating.setObjectName(_fromUtf8("updating"))
        updating.resize(338, 160)
        updating.setMinimumSize(QtCore.QSize(338, 160))
        updating.setMaximumSize(QtCore.QSize(338, 160))
        self.label = QtGui.QLabel(updating)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(updating)
        QtCore.QMetaObject.connectSlotsByName(updating)

    def retranslateUi(self, updating):
        updating.setWindowTitle(_translate("updating", "Aktualizacja bazy", None))
        self.label.setText(_translate("updating", "Czekaj, aktualizuję bazę tweetów...", None))


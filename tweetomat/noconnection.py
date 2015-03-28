# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noconnection.ui'
#
# Created: Wed Feb  5 19:49:15 2014
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

#Class represents dialog informing about twitter connection problems
class Ui_noConnection(object):
    def setupUi(self, noConnection):
        noConnection.setObjectName(_fromUtf8("noConnection"))
        noConnection.resize(338, 160)
        noConnection.setMinimumSize(QtCore.QSize(338, 160))
        noConnection.setMaximumSize(QtCore.QSize(338, 160))
        self.noConnectionClose = QtGui.QPushButton(noConnection)
        self.noConnectionClose.setGeometry(QtCore.QRect(120, 110, 98, 27))
        self.noConnectionClose.setObjectName(_fromUtf8("noConnectionClose"))
        self.label = QtGui.QLabel(noConnection)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(noConnection)
        QtCore.QMetaObject.connectSlotsByName(noConnection)

    def retranslateUi(self, noConnection):
        noConnection.setWindowTitle(_translate("noConnection", "Brak połączenia z Internetem", None))
        self.noConnectionClose.setText(_translate("noConnection", "Close", None))
        self.label.setText(_translate("noConnection", "Nie mogę połączyć się         z serwerami Twittera!", None))


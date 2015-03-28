# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created: Thu Feb  6 04:00:24 2014
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

#Class represents user-managing window
class Ui_manager(object):
    def setupUi(self, manager):
        manager.setObjectName(_fromUtf8("manager"))
        manager.resize(472, 418)
        self.acceptButton = QtGui.QPushButton(manager)
        self.acceptButton.setGeometry(QtCore.QRect(190, 360, 98, 27))
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.usersList = QtGui.QListView(manager)
        self.usersList.setGeometry(QtCore.QRect(35, 20, 411, 192))
        self.usersList.setObjectName(_fromUtf8("usersList"))
        self.lineEdit = QtGui.QLineEdit(manager)
        self.lineEdit.setGeometry(QtCore.QRect(120, 230, 221, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.addRemove = QtGui.QPushButton(manager)
        self.addRemove.setGeometry(QtCore.QRect(130, 260, 201, 31))
        self.addRemove.setObjectName(_fromUtf8("addRemove"))

        self.retranslateUi(manager)
        QtCore.QMetaObject.connectSlotsByName(manager)

    def retranslateUi(self, manager):
        manager.setWindowTitle(_translate("manager", "Zarządzaj obserwowanymi użytkownikami", None))
        self.acceptButton.setText(_translate("manager", "OK", None))
        self.addRemove.setText(_translate("manager", "Dodaj / usuń użytkownika", None))


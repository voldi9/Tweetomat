# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created: Thu Feb  6 17:26:51 2014
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

#Class represents application's main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(773, 490)
        MainWindow.setMinimumSize(QtCore.QSize(773, 490))
        MainWindow.setMaximumSize(QtCore.QSize(773, 490))
        #MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.manageButton = QtGui.QPushButton(self.centralwidget)
        self.manageButton.setGeometry(QtCore.QRect(240, 380, 311, 61))
        self.manageButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.manageButton.setObjectName(_fromUtf8("manageButton"))
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(240, 310, 311, 61))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.topTags = QtGui.QListView(self.centralwidget)
        self.topTags.setGeometry(QtCore.QRect(20, 90, 361, 192))
        self.topTags.setObjectName(_fromUtf8("topTags"))
        self.topUsrmen = QtGui.QListView(self.centralwidget)
        self.topUsrmen.setGeometry(QtCore.QRect(410, 90, 341, 192))
        self.topUsrmen.setObjectName(_fromUtf8("topUsrmen"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Enhance your tweets", None))
        self.manageButton.setText(_translate("MainWindow", "Zarządzaj obserwowanymi użytkownikami", None))
        self.refreshButton.setText(_translate("MainWindow", "Odśwież bazę", None))
        self.label.setText(_translate("MainWindow", " Popularne hashtagi (ocena):", None))
        self.label_2.setText(_translate("MainWindow", "Popularni użytkownicy (ocena):", None))


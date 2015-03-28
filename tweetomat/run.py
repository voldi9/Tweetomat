# -*- coding: utf-8 -*-
import sys

import PyQt4 
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from twython import Twython, TwythonError
from project import Ui_MainWindow
from time import sleep
import psycopg2, globalvals, updater
import updating, noconnection, manager

#
# Defining each dialog's and main window's instances
#

class UpWindow(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
		self.ui = updating.Ui_updating()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self, QtCore.SIGNAL("finished(int)"), self.show)

class NoConnection(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
		self.ui = noconnection.Ui_noConnection()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.noConnectionClose, QtCore.SIGNAL("clicked()"), self.close)

class Manager(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
		self.ui = manager.Ui_manager()
		self.ui.setupUi(self)
		self.ui.usersList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.model = QStandardItemModel()
		QtCore.QObject.connect(self.ui.addRemove, QtCore.SIGNAL("clicked()"), self.addrem)
		QtCore.QObject.connect(self.ui.acceptButton, QtCore.SIGNAL("clicked()"), self.tide)

	#pops out the user-managing dialog
	def manage(self):
		self.model = QStandardItemModel()
		conn = psycopg2.connect(globalvals.dbcommand)
		cur = conn.cursor()

		cur.execute("SELECT login, active FROM Users;")
		logins = cur.fetchall()
		cur.close()
		conn.close()
		self.buildmodel(logins)
		self.show()

	#build the model to list the users from databes in dialog
	def buildmodel(self, logins):
		self.model.clear()
		for login in logins:
			item = QStandardItem(login[0])
			check = Qt.Checked if login[1] == True else Qt.Unchecked
			item.setCheckState(check)
			item.setCheckable(True)
			self.model.appendRow(item)
		self.ui.usersList.setModel(self.model)

	#responses to add/remove button in user-managing dialog
	def addrem(self):
		login = str(self.ui.lineEdit.text())
		if login == '':
			return None

		was = False
		for i in range(self.model.rowCount()): 
			if str(self.model.item(i).text()) == login:
				self.model.removeRow(i)
				was = True
				break
		
		if not was:
			item = QStandardItem(login)
			item.setCheckState(Qt.Unchecked)
			item.setCheckable(True)
			self.model.appendRow(item)

	#responses to OK button in user-managing dialog
	def tide(self):
		logins = ()
		onlylogins = ()
		for i in range(self.model.rowCount()): 
			logins += ([str(self.model.item(i).text()), True if self.model.item(i).checkState() \
			== Qt.Checked else False],)
			onlylogins += (self.model.item(i).text(),)

		conn = psycopg2.connect(globalvals.dbcommand)
		cur = conn.cursor()
		cur.execute("SELECT login from Users;")
		users = cur.fetchall()

		for user in users:
			if not user[0] in onlylogins: #delete removed users
				updater.deleteuser(user[0])
				cur.execute("DELETE FROM Users WHERE login = %s;", (user[0],))

		conn.commit()
		cur.execute("SELECT login from Users;")
		users = cur.fetchall()

		for login in logins:
			if not (login[0],) in users: #add new users
				cur.execute("INSERT INTO Users VALUES (%s, %s, current_timestamp, 0, 1);", (login[0], login[1]))
			else:
				cur.execute("SELECT active FROM Users WHERE login = %s;", (login[0],))
				if login[1] == True: #disable no longer active users
					if cur.fetchone()[0] == False:
						updater.addrates(login[0])
						cur.execute("UPDATE Users SET active = true WHERE login = %s;", (login[0],))
				else:
					if cur.fetchone()[0] == True: #enable activated users
						updater.lowerrates(login[0])
						cur.execute("UPDATE Users SET active = false WHERE login = %s;", (login[0],))

		self.parent().upcontent()

		conn.commit()
		cur.close()
		conn.close()
		self.close()
		

class MyCounter(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.noConn = NoConnection(self)
		self.upWin = UpWindow(self)
		self.manager = Manager(self)
		self.ui.topTags.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.ui.topUsrmen.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

		QtCore.QObject.connect(self.ui.refreshButton,QtCore.SIGNAL("clicked()"), self.refresh)
		QtCore.QObject.connect(self.ui.manageButton,QtCore.SIGNAL("clicked()"), self.manager.manage)
		
	#responses to the database refresh button
	def refresh(self):
		self.upWin.show()
		self.setEnabled(False)
		self.upWin.setEnabled(True)
		app.processEvents()
		
		conn = psycopg2.connect(globalvals.dbcommand)
		cur = conn.cursor()
		cur.execute("SELECT login FROM Users")	
		users = cur.fetchall()

		cur.close()
		conn.close()
		try:
			twitter = Twython(globalvals.APP_KEY, access_token = globalvals.ACCESS_TOKEN)
		except TwythonError as e:
			print e

		try:
			#check if we can connect to the internet
			user_timeline = twitter.get_user_timeline(screen_name = 'katyperry', count = 1)
			
			for user in users:
				updater.updateuser(user[0])
		
			self.upcontent()	
			self.upWin.setVisible(False)
			app.processEvents()

		except TwythonError as e:
			#not connected to the internet!
			self.upWin.setVisible(False)
			self.noConn.exec_()
			print e
		
		self.setEnabled(True)
		app.processEvents()

	#updates the rankings listed in main window based on 
	#database rows
	def upcontent(self):
		conn = psycopg2.connect(globalvals.dbcommand)
		cur = conn.cursor()

		#update tags' listed ranking
		cur.execute("""SELECT content, rate from Keyword WHERE content LIKE '#%'
		ORDER BY rate DESC;""")
		tops = cur.fetchall()
		tlist = QtCore.QStringList()
		for single in tops:
			tlist.append(single[0] + '   (' + "%.2f" % (single[1]/1000000.0) + ')')
		model = QtGui.QStringListModel()
		model.setStringList(tlist)
		self.ui.topTags.setModel(model)		
		
		#update user mentions' listed ranking
		cur.execute("""SELECT content, rate from Keyword WHERE content LIKE '@%'
		ORDER BY rate DESC;""")
		tops = cur.fetchall()
		tlist = QtCore.QStringList()
		for single in tops:
			tlist.append(single[0] + '   (' + "%.2f" % (single[1]/1000000.0) + ')')
		model = QtGui.QStringListModel()
		model.setStringList(tlist)
		self.ui.topUsrmen.setModel(model)

		cur.close()
		conn.close()
	
#starts the app's main window
def start():
	global app
	app = QtGui.QApplication(sys.argv)
	myapp = MyCounter()
	myapp.upcontent()
	myapp.show()
	sys.exit(app.exec_())
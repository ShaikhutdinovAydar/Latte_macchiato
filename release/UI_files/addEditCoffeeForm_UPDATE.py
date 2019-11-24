# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm_UPDATE.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_up(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 510)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 220, 191, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 340, 191, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 180, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 140, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.up_btn.setGeometry(QtCore.QRect(90, 390, 131, 31))
        self.up_btn.setObjectName("up_btn")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 260, 191, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 300, 191, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 100, 191, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 21))
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
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "молотый/в зернах"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "объем упаковки"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "степень обжарки"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "название сорта"))
        self.up_btn.setText(_translate("MainWindow", "Изменить"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "описание вкуса"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "цена"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "ID"))
        self.label.setText(_translate("MainWindow", "Изменить"))

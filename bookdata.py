# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookdata.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setMaximumSize(QtCore.QSize(600, 300))
        Dialog.setMinimumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Book_Data.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.booktable = QtWidgets.QTableWidget(Dialog)
        self.booktable.setRowCount(5)
        self.booktable.setColumnCount(2)
        self.booktable.setEnabled(True)
        self.booktable.setColumnWidth(0,400)
        self.booktable.setObjectName("booktable")
        self.verticalLayout.addWidget(self.booktable)
        font1 = QtGui.QFont()
        font1.setFamily("Arial")
        font1.setPointSize(12)
        self.booktable.setFont(font1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        col_head = ['Book Name', 'Quantity']
        self.booktable.setHorizontalHeaderLabels(col_head)
        self.show_book()

    def show_book(self):
        bk = sqlite3.connect('studentdatabase.db')
        sql = 'select * from Books;'
        result = bk.execute(sql)
        self.booktable.setRowCount(0)
        for row, row_data in enumerate(result):
            self.booktable.insertRow(row)
            for column, data in enumerate(row_data):
                self.booktable.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        
        bk.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Book Data"))

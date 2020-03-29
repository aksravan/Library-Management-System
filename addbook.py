# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addbook.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 432)
        Dialog.setMinimumSize(QtCore.QSize(592, 432))
        Dialog.setMaximumSize(QtCore.QSize(592, 432))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Book_Data.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        # enterbookname
        self.enterbookname = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.enterbookname.setFont(font)
        self.enterbookname.setObjectName("enterbookname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enterbookname)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        # enternoofbook
        self.enternoofbook = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enternoofbook.setFont(font)
        self.enternoofbook.setObjectName("enternoofbook")
        self.enternoofbook.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enternoofbook)
        # addbook --> button for adding the book
        self.addbook = QtWidgets.QPushButton(Dialog)
        self.addbook.setFlat(True)
        self.addbook.setObjectName("addbook")
        self.addbook.clicked.connect(self.addingBook)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.addbook)
        # errormessage
        self.errormessage = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.errormessage.setFont(font)
        self.errormessage.setText("")
        self.errormessage.setObjectName("errormessage")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.errormessage)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        # booknamedelete --> enter book name for deleting the book
        self.booknamedelete = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.booknamedelete.setFont(font)
        self.booknamedelete.setObjectName("booknamedelete")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.booknamedelete)
        # deletebook --> button to dlt the book
        self.deletebook = QtWidgets.QPushButton(Dialog)
        self.deletebook.setFlat(True)
        self.deletebook.setObjectName("deletebook")
        self.deletebook.clicked.connect(self.deletingBook)
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.deletebook)
        # addbookmsg --> a message will appear after clicking the add book button --> showing result
        self.addbookmsg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.addbookmsg.setFont(font)
        self.addbookmsg.setObjectName("addbookmsg")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addbookmsg)
        # dltbookmsg --> a message will appear after clicking the delete book button --> showing result
        self.dltbookmsg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.dltbookmsg.setFont(font)
        self.dltbookmsg.setObjectName("dltbookmsg")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.dltbookmsg)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # addingBook function
    def addingBook(self):
        if self.enterbookname.text() != '' and self.enternoofbook.text() != '':
            bk = sqlite3.connect('studentdatabase.db')
            curbk = bk.cursor()
            sql = "select * from Books where BookName='" + self.enterbookname.text().title() + "';"
            curbk.execute(sql)
            res = curbk.fetchone()
            if res == None:
                #   INSERT INTO table_name VALUES (value1, value2, value3, ...);
                sql = "insert into Books values('" + self.enterbookname.text().title() + "' , " + self.enternoofbook.text() + ");"
                curbk.execute(sql)
                self.addbookmsg.setText('Book is successfully added.')
                bk.commit()
            else:
                self.addbookmsg.setText('Book is already added.')
            bk.close()
        else:
            self.addbookmsg.setText('Enter bookname or no of books to delete.')

    # deletingBook function
    def deletingBook(self):
        if self.booknamedelete.text() != '':
            bk = sqlite3.connect('studentdatabase.db')
            curbk = bk.cursor()
            sql = "select * from Books where BookName='" + self.booknamedelete.text().title() + "';"
            curbk.execute(sql)
            res = curbk.fetchone()
            if res != None:
                #   DELETE FROM table_name WHERE condition;
                sql = "delete from Books where BookName='" + self.booknamedelete.text().title() + "';"
                curbk.execute(sql)
                self.dltbookmsg.setText('Book is successfully deleted.')
                bk.commit()
            else:
                self.dltbookmsg.setText('Book is not there to delete.')
            bk.close()
        else:
            self.dltbookmsg.setText('Enter bookname to delete.')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Book Update"))
        self.label_2.setText(_translate("Dialog", "Book Name"))
        self.label_3.setText(_translate("Dialog", "Total No. of Books"))
        self.label.setText(_translate("Dialog", "Enter Book Details to add"))
        self.addbook.setText(_translate("Dialog", "Add Book"))
        self.label_4.setText(_translate("Dialog", "Enter Book Name to delete "))
        self.label_5.setText(_translate("Dialog", "Book Name"))
        self.deletebook.setText(_translate("Dialog", "Delete Book"))
        self.addbookmsg.setText(_translate("Dialog", " "))
        self.dltbookmsg.setText(_translate("Dialog", " "))

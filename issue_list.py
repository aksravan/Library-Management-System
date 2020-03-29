# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issue_list.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from datetime import date
import sqlite3

class Ui_Dialog(object):
    def go_Back(self, Dialog, rec):
        from student_details import Ui_Student_Details
        self.stu_details = QtWidgets.QMainWindow()
        self.stu_detail_ui = Ui_Student_Details()
        self.stu_detail_ui.setupUi(self.stu_details, rec)
        self.stu_details.show()
        Dialog.hide()

    def setupUi(self, Dialog, rec):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Issued-Books"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # booklist
        self.booklist = QtWidgets.QListWidget(Dialog)
        self.booklist.setObjectName("booklist")
        self.horizontalLayout_2.addWidget(self.booklist)
        # doilist  --> date of issue list
        self.doilist = QtWidgets.QListWidget(Dialog)
        self.doilist.setObjectName("doilist")
        self.horizontalLayout_2.addWidget(self.doilist)
        # dorlist  --> date of return list
        self.dorlist = QtWidgets.QListWidget(Dialog)
        self.dorlist.setObjectName("dorlist")
        self.horizontalLayout_2.addWidget(self.dorlist)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # go back icon 
        self.back = QtWidgets.QCommandLinkButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Custom-Icon-Design-Flatastic-8-Go-back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName("back")
        self.back.clicked.connect(lambda: self.go_Back(Dialog, rec))
        self.horizontalLayout_3.addWidget(self.back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        # returnbook button 
        #after pressing the button the issued book is updated as returned book
        self.returnbook = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.returnbook.setFont(font)
        self.returnbook.setFlat(True)
        self.returnbook.setObjectName("returnbook")
        self.returnbook.clicked.connect(lambda: self.ReturnBook(rec))

        self.horizontalLayout_3.addWidget(self.returnbook)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.previousbookrecord(rec[8], rec[9], rec[10])
    
    # this function will get the issued book to the student
    def previousbookrecord(self, books, doi, dor):
        # adding book
        if books!=None:
            books = books.split(',')            
            for index in books:
                if index!=None and index != '':
                    self.booklist.addItem(index)
        elif books == '':
            self.booklist.addItem("No Book Issued.")            
        else:
            self.booklist.addItem("No Book Issued.")
        # adding date of issue
        if books!=None:
            doi = doi.split(',')            
            for index in doi:
                if index!=None and index != '':
                    self.doilist.addItem(index)
        elif books == '':
            self.doilist.addItem("No Date of issue.")            
        else:
            self.doilist.addItem("No Date of issue.")
        # adding date of return
        if dor!=None:
            dor = dor.split(',')            
            for index in dor:
                if index!=None and index != '':
                    self.dorlist.addItem(index)
        elif dor == '':
            self.dorlist.addItem("No Date of return.")            
        else:
            self.dorlist.addItem("No Date of return.")

        if doi != None and dor != None:
            if len(doi) > len(dor):
                self.dorlist.addItem('Not returned')
        if doi != None and dor != None:
            if len(doi) == len(dor):
                self.returnbook.setEnabled(False)
    
    # returning the las book issued
    def ReturnBook(self, record):
        today = date.today()
        bk = sqlite3.connect('studentdatabase.db')
        curbk = bk.cursor()
        if record[10] != None:
            rec = record[10] + today.strftime('%Y-%m-%d')
        else:
            rec = today.strftime('%Y-%m-%d')
        sql = "update student set DOR='" + rec + ",' where Adm_No=" + str(record[0]) + ";"
        curbk.execute(sql)
        bk.commit()
        self.booklist.clear()
        self.doilist.clear()
        self.dorlist.clear()
        sql = "select * from student where Adm_No=" + str(record[0]) + ";"
        curbk.execute(sql)
        res = curbk.fetchone()
        self.previousbookrecord(res[8], res[9], res[10])
        '''
        UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;
        '''
        bk.commit()
        bk.close()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Issued Books"))
        self.label_2.setText(_translate("Dialog", "Book Name"))
        self.label.setText(_translate("Dialog", "Date of Issue"))
        self.label_3.setText(_translate("Dialog", "Date of Return"))
        self.back.setText(_translate("Dialog", "Back"))
        self.returnbook.setText(_translate("Dialog", "Return Book"))

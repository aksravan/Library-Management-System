# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\student_details.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date

class Ui_Student_Details(object):
    def setupUi(self, StuDetails, rec):
        StuDetails.setObjectName("StuDetails")
        StuDetails.setWindowModality(QtCore.Qt.ApplicationModal)
        StuDetails.resize(900, 700)
        StuDetails.setMinimumSize(QtCore.QSize(900, 700))
        StuDetails.setMaximumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        StuDetails.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Custom-Icon-Design-Pretty-Office-10-Student-id.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StuDetails.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StuDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        # fathername
        self.fathername = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fathername.setFont(font)
        self.fathername.setStyleSheet('color: blue')
        self.fathername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fathername.setObjectName("fathername")
        self.fathername.setText(str(rec[5]))
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fathername)
        # name
        self.name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: blue")
        self.name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.name.setText(str(rec[4]))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name)
        # rollno
        self.rollno = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rollno.setFont(font)
        self.rollno.setAlignment(QtCore.Qt.AlignCenter)
        self.rollno.setObjectName("rollno")
        self.rollno.setStyleSheet('color: blue')
        self.rollno.setText(str(rec[3]))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rollno)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        # mothername
        self.mothername = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mothername.setFont(font)
        self.mothername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mothername.setObjectName("mothername")
        self.mothername.setStyleSheet('color: blue')
        self.mothername.setText(str(rec[7]))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mothername)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem3)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.label_8)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem5)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_9)
        # bookname
        self.bookname = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookname.setFont(font)
        self.bookname.setObjectName("bookname")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.bookname)
        self.bookname.setStyleSheet('color: blue')

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem7)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_11)
        # availbook
        self.availbook = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.availbook.setFont(font)
        self.availbook.setText("")
        self.availbook.setAlignment(QtCore.Qt.AlignCenter)
        self.availbook.setObjectName("availbook")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.availbook)

        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.SpanningRole, spacerItem8)

        # findbook button
        self.findbook = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.findbook.setFont(font)
        self.findbook.setFlat(True)
        self.findbook.setObjectName("findbook")
        self.findbook.clicked.connect(self.findBook)
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.findbook)

        # bookissue list
        self.bookissuelist = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bookissuelist.setFont(font)
        self.bookissuelist.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bookissuelist.setIconSize(QtCore.QSize(15, 20))
        self.bookissuelist.setDefault(False)
        self.bookissuelist.setFlat(True)
        self.bookissuelist.setObjectName("bookissuelist")
        self.bookissuelist.clicked.connect(lambda: self.Book_issue(StuDetails, rec))
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.bookissuelist)

        # issuebookbtn
        self.issuebookbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.issuebookbtn.setFont(font)
        self.issuebookbtn.setFlat(True)
        self.issuebookbtn.setObjectName("issuebookbtn")
        self.issuebookbtn.clicked.connect(self.issuing_Book)
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.issuebookbtn)
        # issueerrormsg
        self.issueerrormsg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.issueerrormsg.setFont(font)
        self.issueerrormsg.setObjectName("issueerrormsg")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.issueerrormsg)

        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem10)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        # classs
        self.classs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.classs.setFont(font)
        self.classs.setStyleSheet('color: blue')
        self.classs.setAlignment(QtCore.Qt.AlignCenter)
        self.classs.setObjectName("classs")
        self.classs.setText(str(rec[1]))
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.classs)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        # admno    ---> admission number
        self.admno = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.admno.setFont(font)
        self.admno.setText(str(rec[0]))
        self.admno.setAlignment(QtCore.Qt.AlignCenter)
        self.admno.setObjectName("admno")
        self.admno.setStyleSheet('color: blue')
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.admno)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        # mobileno
        self.mobileno = QtWidgets.QLabel(self.centralwidget)
        self.mobileno.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mobileno.setFont(font)
        self.mobileno.setText(str(rec[6]))
        self.mobileno.setStyleSheet('color: blue')
        self.mobileno.setAlignment(QtCore.Qt.AlignCenter)
        self.mobileno.setObjectName("mobileno")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mobileno)

        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem14)

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(".\\Custom-Icon-Design-Pretty-Office-10-Student-id.ico"))
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_12)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem15)
        # logout button
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logout.setFont(font)
        self.logout.setFlat(True)
        self.logout.setObjectName("logout")
        self.logout.clicked.connect(lambda: self.logged_out(StuDetails))
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.logout)

        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem16)
        self.horizontalLayout.addLayout(self.formLayout_2)
        StuDetails.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StuDetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        StuDetails.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StuDetails)
        self.statusbar.setObjectName("statusbar")
        StuDetails.setStatusBar(self.statusbar)

        self.retranslateUi(StuDetails)
        QtCore.QMetaObject.connectSlotsByName(StuDetails)

    # logging out of the current student...
    def logged_out(self, StuDetails):
        from lms_mainwindow import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow_ui = Ui_MainWindow()
        self.MainWindow_ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        StuDetails.hide()

    # displaying the issued books list
    def Book_issue(self, StuDetails, rec):
        from issue_list import Ui_Dialog
        self.List = QtWidgets.QDialog()
        self.book_ui = Ui_Dialog()
        self.book_ui.setupUi(self.List, rec)
        self.List.show()
        StuDetails.hide()

    # this function for finding the book in the database
    def findBook(self):
        if self.bookname.text() != '':
            bk = sqlite3.connect('studentdatabase.db')
            curbk = bk.cursor()
            sql = "select * from Books where BookName='" + self.bookname.text().title() + "';"
            curbk.execute(sql)
            res = curbk.fetchone()
            if res != None:
                self.issueerrormsg.setText('Book Found!')
                self.availbook.setText(str(res[1]))
            else:
                self.issueerrormsg.setText('Book is not found!')
        else:
            self.issueerrormsg.setText('Enter a book name!')
    
    # function for issuing the book to the student
    def issuing_Book(self):
        today = date.today()
        
        if self.bookname.text() != '':
            if int(self.availbook.text()) > 0:
                bk = sqlite3.connect('studentdatabase.db')
                curbk = bk.cursor()
                curbk.execute("update books set Quantity=" + str(int(self.availbook.text()) - 1) + " where BookName='" + self.bookname.text().title() + "' ;")
                sql = "select Adm_No, Book_Issued, DOI from student where Adm_No=" + self.admno.text()
                curbk.execute(sql)
                res = curbk.fetchone()
                if res[1] != '' or res[1] != None:
                    result = res[1] + self.bookname.text().title() + ","
                    today = res [2] + today.strftime('%Y-%m-%d') + ","
                    
                else:
                    result  = self.bookname.text().title() + ","
                    today = today.strftime('%Y-%m-%d') + ","                    
                curbk.execute("update student set Book_Issued='" + result + "', DOI='" + today + "' where Adm_No="+ self.admno.text() + ";")
                bk.commit()
                self.availbook.setText(str(int(self.availbook.text()) - 1))
            else:
                self.issueerrormsg.setText('Book is not available to issue.')
        else:
            self.issueerrormsg.setText('Enter a book name and check if avilable.')

    def retranslateUi(self, StuDetails):
        _translate = QtCore.QCoreApplication.translate
        StuDetails.setWindowTitle(_translate("StuDetails", "Student Details"))
        self.label.setText(_translate("StuDetails", "Name"))
        self.label_4.setText(_translate("StuDetails", "Roll NO"))
        self.label_5.setText(_translate("StuDetails", "Father\'s Name"))
        self.label_7.setText(_translate("StuDetails", "Mother\'s Name"))
        self.label_8.setText(_translate("StuDetails", "Issue New Book"))
        self.label_9.setText(_translate("StuDetails", "Book Name"))
        self.label_11.setText(_translate("StuDetails", "Available Books"))
        self.findbook.setText(_translate("StuDetails", "Find Book"))
        self.bookissuelist.setText(_translate("StuDetails", "Book Issue List"))
        self.label_2.setText(_translate("StuDetails", "Class"))
        self.label_3.setText(_translate("StuDetails", "Adm No"))
        self.label_6.setText(_translate("StuDetails", "Mobile No"))
        self.logout.setText(_translate("StuDetails", "Logout"))
        self.issuebookbtn.setText(_translate("MainWindow", "Issue Book"))
        self.issueerrormsg.setText(_translate("MainWindow", " "))
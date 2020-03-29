# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lms_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Itzikgur-My-Seven-Books-1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 476, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(494, 11, 381, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        #   student ID
        self.studentid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.studentid.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentid.setFont(font)
        self.studentid.setObjectName("studentid")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.studentid)
        #   studenterror message
        self.studenterror = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.studenterror.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.studenterror.setFont(font)
        self.studenterror.setObjectName("studenterror")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.studenterror)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        #   login
        self.login = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.login.setFlat(True)
        self.login.clicked.connect(lambda: self.loginFunction(MainWindow))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.login)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 250, 281, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\Itzikgur-My-Seven-Books-1.ico"))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 310, 331, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 360, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(493, 390, 380, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 432, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 580, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 474, 291, 31))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(483, 330, 20, 181))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        #   menubar 
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        # menuFile
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menuFilefunction)

        # menuView
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView.triggered[QtWidgets.QAction].connect(self.menuViewfunction)

        # menuHelp
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.triggered[QtWidgets.QAction].connect(self.menuHelpfunction)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # addstudent
        self.actionAdd_Student = QtWidgets.QAction(MainWindow)
        self.actionAdd_Student.setEnabled(True)
        self.actionAdd_Student.setObjectName("actionAdd_Student")
        # addbook
        self.actionAdd_Book = QtWidgets.QAction(MainWindow)
        self.actionAdd_Book.setEnabled(True)
        self.actionAdd_Book.setObjectName("actionAdd_Book")
        # deletebook
        self.actionDelete_Book = QtWidgets.QAction(MainWindow)
        self.actionDelete_Book.setObjectName("actionDelete_Book")
        # exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        # viewstudents
        self.actionView_Student = QtWidgets.QAction(MainWindow)
        self.actionView_Student.setObjectName("actionView_Student")
        # viewbooks
        self.actionView_Books = QtWidgets.QAction(MainWindow)
        self.actionView_Books.setObjectName("actionView_Books")
        # aboutLMS
        self.actionAbout_LMS = QtWidgets.QAction(MainWindow)
        self.actionAbout_LMS.setObjectName("actionAbout_LMS")
        self.menuFile.addAction(self.actionAdd_Student)
        self.menuFile.addAction(self.actionAdd_Book)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_Book)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionView_Student)
        self.menuView.addAction(self.actionView_Books)
        self.menuHelp.addAction(self.actionAbout_LMS)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # menuHelp function displays the about information...
    def menuHelpfunction(self):
        from lms_about import Ui_Dialog
        self.Dia = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dia)
        self.Dia.show()
    
    # menuFile function-> getting file input...
    def menuFilefunction(self,action):
        act = action.text()
        if act == 'Exit':
            import sys
            sys.exit()
        if act == 'Add Student':
            from addstudent import Ui_Dialog
            self.Dia = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.Dia)
            self.Dia.show()
        if act == 'Add Book' or act == 'Delete Book':
            from addbook import Ui_Dialog
            self.Dia = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.Dia)
            self.Dia.show()

    # menuFile function-> getting file input...
    def menuViewfunction(self,action):
        act = action.text()
        if act == 'View Students':
            from studentdata import Ui_Dialog
            self.Dia = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.Dia)
            self.Dia.show()
        if act == 'View Books':
            from bookdata import Ui_Dialog
            self.Dia = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.Dia)
            self.Dia.show()

    # function will be invoked when login is clicked...
    def loginFunction(self, MainWindow):
        if self.studentid.text() != '':
            from student_details import Ui_Student_Details
            st = sqlite3.connect('studentdatabase.db')
            stbk = st.cursor()
            sql = "select * from student where Adm_No=" + self.studentid.text() + ";"
            stbk.execute(sql)
            rec = stbk.fetchone()
            if rec != None:
                self.stu_details = QtWidgets.QMainWindow()
                self.stu_detail_ui = Ui_Student_Details()
                self.stu_detail_ui.setupUi(self.stu_details, rec)
                self.stu_details.show()
                MainWindow.hide()
                self.studenterror.setText("Student found!")
            else:
                self.studenterror.setText("Student not found!")
            st.close()
        else:
            self.studenterror.setText("Enter Student ID!")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LMS"))
        self.label.setText(_translate("MainWindow", "LIBRARY MANAGEMENT SYSTEM"))
        self.label_2.setText(_translate("MainWindow", "Student ID"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.label_3.setText(_translate("MainWindow", "Welcome to "))
        self.label_5.setText(_translate("MainWindow", "This software allows you to add student data,"))
        self.label_6.setText(_translate("MainWindow", "modify student data, delete student record,"))
        self.label_7.setText(_translate("MainWindow", " add new books to database, delete books which"))
        self.label_8.setText(_translate("MainWindow", "are no longe available at library or not "))
        self.label_9.setText(_translate("MainWindow", "NOTE - Teacher have to login using the admission number of the student."))
        self.label_10.setText(_translate("MainWindow", "necessary to kept them in school."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_Student.setText(_translate("MainWindow", "Add Student"))
        self.actionAdd_Book.setText(_translate("MainWindow", "Add Book"))
        self.actionDelete_Book.setText(_translate("MainWindow", "Delete Book"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_Student.setText(_translate("MainWindow", "View Students"))
        self.actionView_Books.setText(_translate("MainWindow", "View Books"))
        self.actionAbout_LMS.setText(_translate("MainWindow", "About LMS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

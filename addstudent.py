# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addstudent.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import  sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 364)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("addstudent.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        # fathername
        self.fathername = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.fathername.setFont(font)
        self.fathername.setObjectName("fathername")
        self.gridLayout.addWidget(self.fathername, 5, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        # addstudent --> button to get details
        self.addstudent = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.addstudent.setFont(font)
        self.addstudent.setFlat(True)
        self.addstudent.setObjectName("addstudent")
        self.addstudent.clicked.connect(self.addingstudent)
        self.gridLayout.addWidget(self.addstudent, 9, 3, 1, 1)
        # admno
        self.admno = QtWidgets.QLineEdit(Dialog)
        self.admno.setObjectName("admno")
        self.admno.setValidator(QtGui.QIntValidator())
        self.gridLayout.addWidget(self.admno, 5, 3, 1, 1)

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        # section
        self.section = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.section.setFont(font)
        self.section.setMaxLength(1)
        self.section.setObjectName("section")
        self.gridLayout.addWidget(self.section, 3, 3, 1, 1)
        # studenterrormsg
        self.studenterrormsg = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.studenterrormsg.setFont(font)
        self.studenterrormsg.setText("")
        self.studenterrormsg.setObjectName("studenterrormsg")
        self.gridLayout.addWidget(self.studenterrormsg, 9, 0, 1, 2)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        # class_2
        self.class_2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.class_2.setFont(font)
        self.class_2.setObjectName("class_2")
        self.gridLayout.addWidget(self.class_2, 3, 1, 1, 1)
        # mobileno
        self.mobileno = QtWidgets.QLineEdit(Dialog)
        self.mobileno.setText("")
        self.mobileno.setMaxLength(10)
        self.mobileno.setCursorPosition(0)
        self.mobileno.setObjectName("mobileno")
        self.mobileno.setValidator(QtGui.QIntValidator())
        self.gridLayout.addWidget(self.mobileno, 7, 1, 1, 1)
        # rollno
        self.rollno = QtWidgets.QLineEdit(Dialog)
        self.rollno.setObjectName("rollno")
        self.rollno.setCursorPosition(0)
        self.rollno.setMaxLength(2)
        self.rollno.setValidator(QtGui.QIntValidator())
        self.gridLayout.addWidget(self.rollno, 1, 3, 1, 1)
        # mothername
        self.mothername = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.mothername.setFont(font)
        self.mothername.setObjectName("mothername")
        self.gridLayout.addWidget(self.mothername, 7, 3, 1, 1)
        # studentname
        self.studentname = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.studentname.setFont(font)
        self.studentname.setObjectName("studentname")
        self.gridLayout.addWidget(self.studentname, 1, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# curschool.execute("INSERT INTO Books (Adm_no, Class, Section, Roll_No, Name, Father's_Name, Mobile_No, Mother's_Name) 
# VALUES(?,?,?,?,?,?,?,?);",
# (self.admno.text(), self.class_2.text(), self.rollno.text(), self.studentname.text(), self.fathername.text(), self.mobileno.text(),
# self.mothername.text())
    # function for adding new student
    def addingstudent(self):
        if self.fathername.text() != '' and self.studentname.text() != '' and self.mobileno.text() != '':
            if self.mothername.text() != '' and self.class_2.text() != '' and self.section.text() != '':
                if self.rollno.text() != '' and self.admno.text() != '':
                    st = sqlite3.connect('studentdatabase.db')
                    stbk = st.cursor()
                    sql = "select * from student where Adm_no=" + self.admno.text() + ";"
                    stbk.execute(sql)
                    res = stbk.fetchone()
                    if res == None:
                        sql = "INSERT INTO Books (Adm_no, Class, Section, Roll_No, Name, Father_Name, Mobile_No, Mother_Name) VALUES(?,?,?,?,?,?,?,?);",int(self.admno.text()), self.class_2.text(), int(self.rollno.text()), self.studentname.text().title(), self.fathername.text().title(), int(self.mobileno.text()), self.mothername.text().title()
                        stbk.execute(sql)
                        self.studenterrormsg.setText('Student is added.')
                        st.commit()
                    else:
                        self.studenterrormsg.setText('Student already exists.')  
                    st.close()
                else:
                    self.studenterrormsg.setText('Plese fill all the entries.')
            else:
                self.studenterrormsg.setText('Please fill all the entries.')
        else:
            self.studenterrormsg.setText('Please fill all the entries.')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Student"))
        self.label_3.setText(_translate("Dialog", "Class"))
        self.label_4.setText(_translate("Dialog", "Father\'s Name"))
        self.label_9.setText(_translate("Dialog", "Section"))
        self.label_5.setText(_translate("Dialog", "Roll No"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.addstudent.setText(_translate("Dialog", "Add Student"))
        self.label_7.setText(_translate("Dialog", "Mother\'s Name"))
        self.label_6.setText(_translate("Dialog", "Adm No"))
        self.label_8.setText(_translate("Dialog", "Mobile"))
        self.label.setText(_translate("Dialog", "Enter Student Details to add"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

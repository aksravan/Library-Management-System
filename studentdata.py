# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student data.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 500)
        Dialog.setMaximumSize(QtCore.QSize(1100, 500))
        Dialog.setMinimumSize(QtCore.QSize(1100, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Student_data"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # selectclass
        self.selectclass = QtWidgets.QComboBox(Dialog)
        self.selectclass.setMinimumSize(QtCore.QSize(150, 30))
        self.selectclass.setMaximumSize(QtCore.QSize(150, 30))
        self.selectclass.setObjectName("selectclass")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.selectclass.addItem("")
        self.horizontalLayout.addWidget(self.selectclass)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        # showdata
        # this will displays the all student data
        self.showdata = QtWidgets.QPushButton(Dialog)
        self.showdata.setMinimumSize(QtCore.QSize(150, 30))
        self.showdata.setMaximumSize(QtCore.QSize(150, 30))
        self.showdata.setFlat(True)
        self.showdata.clicked.connect(self.Select_Class)
        self.showdata.setObjectName("showdata")
        self.horizontalLayout.addWidget(self.showdata)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.studenttable = QtWidgets.QTableWidget(Dialog)
        self.studenttable.setObjectName("tableWidget")
        self.studenttable.setColumnCount(8)
        self.studenttable.setRowCount(0)
        self.verticalLayout.addWidget(self.studenttable)
        # changing font and font size
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(70)
        self.studenttable.setFont(font)
        self.studenttable.setEnabled(False)
        # setting up the column width
        self.studenttable.setColumnWidth(5,200)
        self.studenttable.setColumnWidth(6,130)
        self.studenttable.setColumnWidth(7,200)
        self.studenttable.setColumnWidth(0,80)
        self.studenttable.setColumnWidth(1,80)
        self.studenttable.setColumnWidth(2,80)
        self.studenttable.setColumnWidth(3,80)
        self.studenttable.setColumnWidth(4,200)


        col_head = ['Adm No', 'Class', 'Section', 'Roll No', 'Name', 'Father\'s Name', 'Mobile No', 'Mother\'s Name']
        self.studenttable.setHorizontalHeaderLabels(col_head)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    # this will execute for the selecting the class
    def Select_Class(self):
        txt = self.selectclass.currentText()
        self.Show_Student_Data(txt)

    # this will execute for the selecting the class
    def Show_Student_Data(self, txt):
        if txt == 'Select':
            from msgbox import App
            ex = App()
        else:
            bk = sqlite3.connect('studentdatabase.db')
            sql = 'select * from student where class="' + txt + '";'
            result = bk.execute(sql)
            self.studenttable.setRowCount(0)
            for row, row_data in enumerate(result):
                self.studenttable.insertRow(row)
                for column, data in enumerate(row_data):
                    self.studenttable.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

            bk.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student data"))
        self.label.setText(_translate("Dialog", "Selct Class"))
        self.selectclass.setItemText(0, _translate("Dialog", "Select"))
        self.selectclass.setItemText(1, _translate("Dialog", "1"))
        self.selectclass.setItemText(2, _translate("Dialog", "2"))
        self.selectclass.setItemText(3, _translate("Dialog", "3"))
        self.selectclass.setItemText(4, _translate("Dialog", "4"))
        self.selectclass.setItemText(5, _translate("Dialog", "5"))
        self.selectclass.setItemText(6, _translate("Dialog", "6"))
        self.selectclass.setItemText(7, _translate("Dialog", "7"))
        self.selectclass.setItemText(8, _translate("Dialog", "8"))
        self.selectclass.setItemText(9, _translate("Dialog", "9"))
        self.selectclass.setItemText(10, _translate("Dialog", "10"))
        self.selectclass.setItemText(11, _translate("Dialog", "11"))
        self.selectclass.setItemText(12, _translate("Dialog", "12"))
        self.showdata.setText(_translate("Dialog", "Show Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

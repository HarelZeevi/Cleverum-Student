# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../ui/student_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import resources
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1040, 681)
        Form.setStyleSheet("background-color:#2C2F33;")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(300, 130, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: white;")
        self.label_36.setObjectName("label_36")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(350, 230, 221, 341))
        self.frame.setStyleSheet("QFrame{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    padding: 10px;    \n"
"    background-color: #035397;\n"
"}")
        # creating a QGraphicsDropShadowEffect object
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(7)
        shadow1.setOffset(4, 4)
        shadow1.setColor(Qt.black) 
        self.frame.setGraphicsEffect(shadow1)

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("border: 0px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"border: 0px;\n"
"padding: 0px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2)
        self.download_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet("QPushButton{\n"
"    background-color: #FED049;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background-color: #7289DA;\n"
"        color: white;\n"
"}")
        self.download_btn.setObjectName("download_btn")
        self.verticalLayout.addWidget(self.download_btn)
        self.upload_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.upload_btn.setFont(font)
        self.upload_btn.setStyleSheet("QPushButton{\n"
"    background-color: #FED049;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background-color: #7289DA;\n"
"        color: white;\n"
"}")
        self.upload_btn.setObjectName("submit")
        self.verticalLayout.addWidget(self.upload_btn)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(620, 300, 391, 371))
        self.label_4.setObjectName("label_4")
        self.time_left = QtWidgets.QLabel(Form)
        self.time_left.setGeometry(QtCore.QRect(20, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.time_left.setFont(font)
        self.time_left.setStyleSheet("color: beige;\n"
"border: 1px solid beige;\n"
"padding: 6px;\n"
"color: white;\n"
"border-radius: 10px;")
        self.time_left.setObjectName("label_37")
        

       # creating a QGraphicsDropShadowEffect object
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(7)
        shadow2.setOffset(4, 4)
        shadow2.setColor(Qt.black) 
        self.time_left.setGraphicsEffect(shadow2)


        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-190, 220, 361, 471))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_36.setText(_translate("Form", "Test has started"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/icons/icons/docs.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "Test.docs"))
        self.download_btn.setText(_translate("Form", "Download"))
        self.upload_btn.setText(_translate("Form", "Uplaod"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\":/illustrations/imgs/25.png\"/></p></body></html>"))
        self.time_left.setText(_translate("Form", "Time Left: 01:40:00"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/illustrations/imgs/29.png\"/></p></body></html>"))



class StudentTest(Ui_Form):
    def setupUi(self, Form, stackedWidget=None):
        ''' this function gets the stacked widget and changes 
        the shown page according to the events in the page '''
        
        super().setupUi(Form)
        
        # define stack widget as a class property that is accessible within the class 
        self.stackedWidget = stackedWidget

        # This call opens a dianlog for saving the test document
        self.download_btn.clicked.connect(lambda: self.download_test())
        
        # This button open an upload dialog for submitting the finished test
        self.upload_btn.clicked.connect(lambda: self.upload_test())


    def get_document_name(self):
        ''' This function gets the document's name '''
        pass 



    def download_test(self):
        ''' This funcitn downloads the test from the server '''
        pass



    def upload_test(self):
        ''' This funciton uploads the finished test back to the server '''
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = StudentTest()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

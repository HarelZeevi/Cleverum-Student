# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/test_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import resources
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1456, 691)
        Form.setStyleSheet("background-color:#001E6C;")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(560, 90, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(26)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.panel = QtWidgets.QFrame(Form)
        self.panel.setGeometry(QtCore.QRect(110, 210, 1241, 306))
        self.panel.setStyleSheet("QFrame{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: black;\n"
"    padding: 4px;    \n"
"    background-color: #8F43EE;\n"
"}")

        
        self.panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panel.setObjectName("panel")
        self.gridLayout = QtWidgets.QGridLayout(self.panel)
        self.gridLayout.setObjectName("gridLayout")
        self.container2 = QtWidgets.QFrame(self.panel)
        self.container2.setStyleSheet("background-color: #2D033B;\n"
"color: white;\n"
"margin: 0px;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.container2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container2.setObjectName("container2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.container2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name2 = QtWidgets.QLabel(self.container2)
        self.name2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(22)
        self.name2.setFont(font)
        self.name2.setStyleSheet("border: 0px;\n"
"padding: 0px;")
        self.name2.setObjectName("name2")
        self.verticalLayout_2.addWidget(self.name2, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.container2)
        self.frame_6.setStyleSheet("border: 0px;\n"
"background-color: #2D033B;\n"
"color: white;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.camera2 = QtWidgets.QFrame(self.frame_6)
        self.camera2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera2.setObjectName("camera2")
        self.gridLayout_3.addWidget(self.camera2, 1, 0, 1, 1)
        self.screenshot2 = QtWidgets.QFrame(self.frame_6)
        self.screenshot2.setStyleSheet("")
        self.screenshot2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screenshot2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screenshot2.setObjectName("screenshot2")
        self.gridLayout_3.addWidget(self.screenshot2, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.gridLayout.addWidget(self.container2, 0, 1, 1, 1)
        self.container1 = QtWidgets.QFrame(self.panel)
        self.container1.setStyleSheet("background-color: #2D033B;\n"
"color: white;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.container1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container1.setObjectName("container1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.container1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name1 = QtWidgets.QLabel(self.container1)
        self.name1.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(22)
        self.name1.setFont(font)
        self.name1.setStyleSheet("border: 0px;\n"
"padding: 0px;")
        self.name1.setObjectName("name1")
        self.verticalLayout_3.addWidget(self.name1, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.container1)
        self.frame_7.setStyleSheet("border: 0px;\n"
"background-color: #2D033B;\n"
"color: white;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.camera1 = QtWidgets.QFrame(self.frame_7)
        self.camera1.setStyleSheet("")
        self.camera1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera1.setObjectName("camera1")
        self.gridLayout_4.addWidget(self.camera1, 1, 0, 1, 1)
        self.screenshot1 = QtWidgets.QFrame(self.frame_7)
        self.screenshot1.setStyleSheet("")
        self.screenshot1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screenshot1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screenshot1.setObjectName("screenshot1")
        self.gridLayout_4.addWidget(self.screenshot1, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.gridLayout.addWidget(self.container1, 0, 0, 1, 1)
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(10, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: beige;\n"
"border: 1px solid beige;\n"
"padding: 6px;\n"
"color: white;\n"
"border-radius: 10px;")
        self.time_label.setObjectName("label_37")
        self.next_btn = QtWidgets.QPushButton(Form)
        self.next_btn.setGeometry(QtCore.QRect(1370, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.next_btn.setFont(font)
        self.next_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.next_btn.setAutoFillBackground(False)
        self.next_btn.setStyleSheet("QPushButton{\n"
"    background-color: #035397;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:5px;\n"
"    border-color: beige;\n"
"    padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #7289DA;\n"
"}")
        self.next_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon)
        self.next_btn.setIconSize(QtCore.QSize(170, 170))
        self.next_btn.setObjectName("next_btn")
        self.previous_btn = QtWidgets.QPushButton(Form)
        self.previous_btn.setGeometry(QtCore.QRect(20, 320, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_btn.sizePolicy().hasHeightForWidth())
        self.previous_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.previous_btn.setFont(font)
        self.previous_btn.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.previous_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.previous_btn.setStyleSheet("QPushButton{\n"
"    background-color: #035397;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:5px;\n"
"    border-color: beige;\n"
"    padding: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #7289DA;\n"
"}")
        self.previous_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn.setIcon(icon1)
        self.previous_btn.setIconSize(QtCore.QSize(170, 170))
        self.previous_btn.setObjectName("previous_btn")
        self.flow_btn = QtWidgets.QPushButton(Form)
        self.flow_btn.setGeometry(QtCore.QRect(620, 560, 113, 39))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.flow_btn.setFont(font)
        self.flow_btn.setStyleSheet("QPushButton{\n"
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
        self.flow_btn.setObjectName("flow_btn")
        self.velocity_slider = QtWidgets.QSlider(Form)
        self.velocity_slider.setGeometry(QtCore.QRect(1190, 177, 151, 20))
        self.velocity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.velocity_slider.setObjectName("velocity_slider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1230, 140, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Teacher Panel"))
        self.name2.setText(_translate("Form", "Olivia Hall"))
        self.name1.setText(_translate("Form", "Brock Lott"))
        self.time_label.setText(_translate("Form", "Time Left: 01:40:00"))
        self.flow_btn.setText(_translate("Form", "Flow "))
        self.label.setText(_translate("Form", "Velocity"))



class TestPanel(Ui_Form):

    def __init__(self):
        
        # init list of client names
        self.names = []


        
    def setupUi(self, Form, stackedWidget=None):
        ''' this function gets the stacked widget and changes 
        the shown page according to the events in the page '''
        
        super().setupUi(Form)
        
        
        # creating a QGraphicsDropShadowEffect object
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setOffset(2, 2)
        shadow.setColor(Qt.black)
        self.container2.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)
        shadow.setOffset(2, 2)
        shadow.setColor(Qt.black)
        self.container1.setGraphicsEffect(shadow)
        

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setOffset(4, 4)
        shadow.setColor(Qt.black)
        self.panel.setGraphicsEffect(shadow)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)
        shadow.setOffset(4, 4)
        shadow.setColor(Qt.black)
        self.next_btn.setGraphicsEffect(shadow)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)
        shadow.setOffset(4, 4)
        shadow.setColor(Qt.black)
        self.previous_btn.setGraphicsEffect(shadow)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)
        shadow.setOffset(4, 4)
        shadow.setColor(Qt.black)
        self.flow_btn.setGraphicsEffect(shadow)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)
        shadow.setOffset(4, 4)
        shadow.setColor(Qt.black)
        self.time_label.setGraphicsEffect(shadow)




        # define stack widget as a class property that is accessible within the class 
        self.stackedWidget = stackedWidget

        # 'next page'  button event that switches to next page 
        self.next_btn.clicked.connect(lambda: self.next_page())

        # 'previous page'  button event that switches to previous page 
        self.previous_btn.clicked.connect(lambda: self.previous_page())



    def update_slots(self):
        ''' This funciton updates the slots of the screenshots and
            the video streams'''
        
        ind_stu_1 = self.page_num * 2 + 1
        ind_stu_2 = self.page_num * 2 + 2
        
        # student 1 video stream placement 
        # student 1 screenshot placement 

        # only room for student 1, no other stuednt's left
        if ind_stu_2 == len(self.names):

            # hide students 2 frame           
            return 
            
        # student 1 video stream placement
        # student 1 screenshot placement 


        
            

    def next_page(self):
        ''' This function switches to the next existing page and shows it '''
        
        print("next")
  
        # if it is the last existing page (there's no next
        if len(self.names) - (self.page_num + 1) * 40 < 0:
            return 

        # increasing the number of the current page by 1 
        self.page_num = self.page_num + 1

        # init the new video streams in the slots
        self.update_slots()
        
        print("New Page: ", self.page_num)



    def previous_page(self):
        ''' This function switches to the previous existing page and shows it '''
        
        # if it is the first existing page (there's no previous)
        if self.page_num == 0:
            return

        # decreasing the number of the current page by 1 
        self.page_num = self.page_num - 1
        
        # init the new video streams in the slots
        self.update_slots()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
import resources
from PyQt5 import QtCore, QtGui, QtWidgets

import socket
import threading
import cv2 
import numpy as np

# import class for udp video transmission
import sys
sys.path.append('./socket/')
from udp_student import UdpStudent 

from student_test import StudentTest 



class StudentTestSock(UdpStudent, StudentTest):
    ''' This class inherits from the TestSock class which is responsible for 
        the Gui of the student's test page in Pyqt, and from UdpStudent that is reponsible for 
        trasmitting video stream from the pc's camera and screenshots at the teacher's request'''


    def __init__(self, accessToken, filename, **kwargs):
        
        # init pyqt gui
        StudentTest.__init__(self, accessToken, filename)

        # init udp socket 
        UdpStudent.__init__(self, **kwargs)
        

    def show_widget(self):
        print("showing widget, got your signal from server")



    def auth(self):
        ''' This funciton authenticates the student by the given token '''

        AUTH_MSG = self.fullname + ", " + self.token

        print("sending authentication msg: ", AUTH_MSG)
        self.sock.sendto(AUTH_MSG.encode(), (self.HOST, 8080))
        
        response, addr = self.sock.recvfrom(1024)

        if response.decode() == 'AUTH_SUCCESS':
            self.streaming = True
            self.start_video_stream()
        else:
            # return back to test token enter page 
            print('Not authenticated!')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # run gui
    integrated_obj = StudentTestSock(port=8081, host='localhost', token='ABC123')
   
    print("setuping")

    integrated_obj.setupUi(Form)
         
    listener_thread = threading.Thread(target=integrated_obj.start, daemon=True)
    
    print("showing")
    Form.show()
    
    listener_thread.start() 
    
    sys.exit(app.exec_())
 

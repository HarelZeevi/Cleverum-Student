import socket
import threading
import cv2
import pyautogui
import numpy as np

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot



class UdpStudent():


    def __init__(self, **kwargs):

        self.PORT = kwargs['port']
        self.HOST = kwargs['host']
        self.token = kwargs['token']
        self.fullname = kwargs['fullname']

        # screenshot sending flag 
        self.sending_screenshot = False
        
        # define a udp server listener for a further udp communication
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
         # streaming flag
        self.streaming = False
        
    
    def start(self):

        ''' This function fires up a udp server listener '''

        # bind the server 
        self.sock.bind((self.HOST, self.PORT))
        print(f'[UDP Server at {self.HOST}:{self.PORT} is Active]...')

        
        # authenticate the student
        self.auth()

        # starting video streaming
        stream_thread = threading.Thread(target=self.start_video_stream, daemon=True)
        stream_thread.start()

        while True:
            # listener that recieves commands from server
            command, _  = self.sock.recvfrom(1024)
            print("command: ", command)
            
            self.route(command.decode())
  
         

    def route(self, command):
        ''' Listen from incomming requests from the server
            and send send the route it to the different methods'''
        
        if command == 'GET_SCREENSHOT':
            self.sending_screenshot = True 

    
    def send_screenshot(self):
        ''' This function sends  a screenshot to the server'''

        # Get the screen resolution
        screen_width, screen_height = pyautogui.size()

        # Capture the screenshot using PyAutoGUI
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array
        screenshot_np = np.array(screenshot)

        # Convert the color space from RGB to BGR
        screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        return screenshot_np


    def start_video_stream(self):
        ''' This fucntion starts transmitting  a camera video stream to
            the server'''
        
        # Define the chunk size (in bytes)
        CHUNK_SIZE = 65506

        # Initialize the camera
        cap = cv2.VideoCapture(0)
        
        # Check if the camera is working
        if not cap.isOpened():
            print("Could not open camera")
            return

        # used to record the time when we processed last frame
        prev_frame_time = 0

        # used to record the time at which we processed current frame
        new_frame_time = 0
        
        # Loop to read frames from the camera and send them to the UDP socket
        while True:

            if self.sending_screenshot:
                print("Taking snapshot")
                frame = self.send_screenshot()
            
            else: 
                # Capture a frame from the camera
                ret, frame = cap.read()
                
            # Convert the frame to a byte array
            data = cv2.imencode('.jpg', frame)[1].tobytes()

            # Send the data in chunks over UDP
            num_chunks = len(data) // CHUNK_SIZE + 1
           
            # sending number of chunks 
            self.sock.sendto(str(num_chunks).encode(), (self.HOST, 8080))               
           

            for i in range(num_chunks):
                end = min((i + 1) * CHUNK_SIZE + 1, len(data))

                # adding textual alert for screenshot
                if self.sending_screenshot:
                    print("sending Screenshot")
                   
                    frame = self.send_screenshot()
                    
                    # Convert the frame to a byte array
                    data = cv2.imencode('.jpg', frame)[1].tobytes()
                
                    data = b"screen" + data
                    
                    self.sending_screenshot = False

                else:
                    data = b"camera" + data
 
                chunk = data[i * CHUNK_SIZE: end]

                self.sock.sendto(chunk, (self.HOST, 8080))               
            
        
        # Release the camera and close the UDP socket
        cap.release()
        
        cv2.destroyAllWindows()



    def stop_video_stream(self):
        '''This function stops streaming video to the server'''
        
        self.streaming = False



if __name__ == '__main__':
    client = UdpStudent(port=8081, host='localhost', token='ABC123', fullname='Harel Zeevi')

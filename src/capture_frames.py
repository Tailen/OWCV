import time

import cv2
import mss
import numpy as np

import directkeys
from process_frames import process_frame
from utils import *
from getkeys import key_check


def record_samples():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 649, 'left': 1651, 'width': 140, 'height': 140}
        # Initialize fps vars
        fps = 0
        paused = False
        last_time = time.time()
        # Starting countdown
        #count_down()

        # Main loop
        while(True):
            if not paused:
                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))
                # Process the frame
                # processed_frame = process_frame(img)
                # Store to file
                # save_data(processed_frame)
                # Display the picture
                cv2.imshow('imshow_window', cv2.circle(img, (25,115), 1, (0,0,255), 1))
                # Detect skill check
                if img[70,35,0] == 0 and img[70,35,1] == 0 and img[70,35,2] == 0 and img[70,105,0] == 0 and img[70,105,1] == 0 and img[70,105,2] == 0:
                    print('Found skill check')
                    print(img[115,25])
                # Print fps
                fps, last_time = print_fps(fps, last_time)
                # Press "=" to quit
                if cv2.waitKey(1) & 0xFF == ord('='):
                    break
            # Check for pause recording
            paused = check_pause(paused)


def save_data(processed_frame):
    pass


if __name__ == '__main__':
    record_samples()
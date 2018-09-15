import numpy as np
import cv2



def process_frame(frame):

    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    # some other processes

    return processed_frame
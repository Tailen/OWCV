import time
import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('C:/Users/Tailen/Videos/2018-04-08 21-16-50.flv')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

#setup fps counter
last_time = time.time()
fps = 0
 
# Read until video is completed
while(cap.isOpened()):
  if time.time() - last_time < 1:
    fps += 1
  else:
    print(fps)
    last_time = time.time()
    fps = 0

  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
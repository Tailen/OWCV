import cv2
import mss
import numpy
# import time



with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 450, 'left': 880, 'width': 160, 'height': 180}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', img)

        # Display fps
        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

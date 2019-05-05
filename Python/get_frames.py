import time

import cv2
import mss
import numpy



# slow way using PIL ImageGrab
def screen_record():
    try:
        from PIL import ImageGrab
    except ImportError:
        return 0

    # 800x600 windowed mode
    mon = (0, 40, 800, 640)

    title = '[PIL.ImageGrab] FPS benchmark'
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        img = numpy.asarray(ImageGrab.grab(bbox=mon))
        fps += 1

        # cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return fps


# fast way using mss
def screen_record_efficient():
    # 800x600 windowed mode
    mon = {'top': 180, 'left': 540, 'width': 800, 'height': 640}

    title = '[MSS] FPS benchmark'
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while time.time() - last_time < 1:
        img = numpy.asarray(sct.grab(mon))
        fps += 1

        # cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return fps


print('PIL:', screen_record())
print('MSS:', screen_record_efficient())



with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 240, 'left': 560, 'width': 800, 'height': 600}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        #cv2.imshow('OpenCV/Numpy normal', img)

        # Display the picture in grayscale
        cv2.imshow('OpenCV/Numpy grayscale',
                   cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
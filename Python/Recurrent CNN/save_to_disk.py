from PIL import Image
import cv2
import mss
import numpy
import time



def save_to_disk()  :
	with mss.mss() as sct:
	    # Part of the screen to capture
	    monitor = {'top': 450, 'left': 880, 'width': 160, 'height': 180}

	    while 'Screen capturing':
	        last_time = time.time()

			# Get raw pixels from the screen
	        sct_img = sct.grab(monitor)

	        # Create the Image
	        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

	        # And save it!
	        output = 'C:/Users/Tailen/Documents/GitHub/OWCV/screenshots/monitor-{0}.png'.format(count)
	        img.save(output)
	        time.sleep(0.025)

	        # Display fps
	        print('fps: {0}'.format((time.time() == last_time) or (1 / (time.time() - last_time))))

	        # Press "q" to quit
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            cv2.destroyAllWindows()
	            break



if __name__ == "__main__":
	save_to_disk()
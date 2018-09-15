import time
import cv2
from getkeys import key_check



def display_frame():

	# Display the picture
    cv2.imshow('imshow_window', processed_frame)

    # Press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        # break


def print_fps(fps, last_time):

	if (time.time() - last_time) < 1:
		fps += 1
	else:
		print('fps: {0}'.format(fps))
		fps = 0
		last_time = time.time()
	return fps, last_time

    # # Print fps per frame
    # print('fps: {0}'.format(1 / (time.time()-last_time)))



def count_down(sec = 5, message = 'STARTING!!!'):
    for i in list(range(sec))[::-1]:
        print(i+1)
        time.sleep(1)
    print(message)



def check_pause(paused):
    keys = key_check()
    if 'P' in keys:
        if paused:
            paused = False
            print('Unpaused!')
            time.sleep(0.3)
        else:
            print('Paused!')
            paused = True
            time.sleep(0.3)
    return paused
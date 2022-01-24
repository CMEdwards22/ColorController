import cv2 as cv
import numpy as np

# This code was inspired by and created from the example give from openCV documentation
# Documentation example can be found here: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

vidCap = cv.VideoCapture(0)  # Assigning video capture to variable, needs the 0 or it breaks (need to figure out why)
if (not vidCap.isOpened()):  # statement to ensure camera is working
    print("Error: Could not open camera, now exiting")
    exit()

while True:  # keep going until program is killed
    # does a frame by frame capture into frame variable and if frame is read in corectly into frameTest boolean
    frameTest, frame = vidCap.read()

    if (not frameTest):  # Another statement to ensure that the frames are working
        print("Error: Frame not read in correctly, now stopping program")
        break

    # Grayscales video, only use if need converting
    display = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Constantly prints the type of each frame, is uint8
    #print(frame.dtype)

    # Displays video in openCV GUI
    cv.imshow('TitleExample', frame)  # frame for standard video input, use display variable for modified version
    if cv.waitKey(1) == ord('q'):  # Not sure what this line does, I think it might just be a quit key
        # turns out the wait key IS ABSOLUTELY NEEDED becuase you can't use the x button to quit.
        break

# Simple end of program stuff to prevent memory leaks
vidCap.release()
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

# newVideoCapture.py
# Includes wrappers for openCV video capture to include error checking

# Wrapper for cv.VideoCapture to include error checking
def getVideoCapture():
    vidCap = cv.VideoCapture(0)
    if (not vidCap.isOpened()):
        print("Error occured in getVideoCapture: Cannot open camera, now exiting")
        exit()
    return vidCap

# Wrapper function for VideoCapture.read() to include error checking
def getFrame(vidCap):
    frameTest, frame = vidCap.read()
    if (not frameTest):  # Another statement to ensure that the frames are working
        print("Error: Frame not read in correctly, now stopping program")
        exit()
    return frame
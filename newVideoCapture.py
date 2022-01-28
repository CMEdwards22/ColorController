import cv2 as cv
import numpy as np

# newVideoCapture.py
# Wrapper for cv.VideoCapture to include error checking

def getVideoCapture():
    vidCap = cv.VideoCapture(0)
    if (not vidCap.isOpened()):
        print("Error occured in getVideoCapture: Cannot open camera, now exiting")
        exit()
    return vidCap
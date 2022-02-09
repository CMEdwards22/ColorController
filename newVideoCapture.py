import cv2 as cv
import numpy as np

# newVideoCapture.py
# Includes wrappers for openCV video capture to include error checking


def getVideoCapture():
    """Wrapper for cv.VideoCapture to inlcude error checking

    Returns:
        videoCapture: video capture for webcam on computer
    """
    vidCap = cv.VideoCapture(0)
    if (not vidCap.isOpened()):
        print("Error occured in getVideoCapture: Cannot open camera, now exiting")
        exit()
    return vidCap


def getFrame(vidCap):
    """Wrapper function for VideoCapture.read() to include error checking

    Args:
        vidCap (videoCapture): input video capture to get frames from

    Returns:
        numpy.ndarray: the frame from the video capture
    """
    frameTest, frame = vidCap.read()
    if (not frameTest):  # Another statement to ensure that the frames are working
        print("Error: Frame not read in correctly, now stopping program")
        exit()
    return frame


def frame2hsv(frame):
    """Function to convert frame to HSV color map version

    Args:
        frame ([type]):  BGR frame

    Returns:
        numpy.ndarray: HSV frame
    """
    display = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    return display


def hsvFrame(vidCap):
    """Combined step of getFrame and frame2hsv

    Args:
        vidCap (videoCapture): input video capture to get frames from

    Returns:
        numpy.ndarray: the frame from the video capture
    """
    frame = getFrame(vidCap)
    return frame2hsv(frame)
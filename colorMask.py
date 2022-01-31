import cv2 as cv
import numpy as np

# File to comiple all colormasking into on location

# function to convert rgb to useable hsv color for masks
def rgb2hsv(red, green, blue):
    color = np.uint8([[[blue, green, red]]]) #puts into BGR
    hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    return hsv_color


# helper function for colorRange
def findBounds(value, offset):
    # for lower bound
    if (value - offset) < 0:
        lowerbound = 0
    else:
        lowerbound = value - offset
    
    # for upper bound
    if (value + offset) > 255:
        upperbound = 255
    else:
        upperbound = value + offset
    
    return [lowerbound, upperbound]


def colorRange(hsv, hOffset = 10, sOffset = 150, vOffset = 150):
    h_val = hsv[0][0][0]
    s_val = hsv[0][0][1]
    v_val = hsv[0][0][2]

    h_bounds = findBounds(h_val, hOffset)
    s_bounds = findBounds(s_val, sOffset)
    v_bounds = findBounds(v_val, vOffset)

    lowerbound = [h_bounds[0], s_bounds[0], v_bounds[0]]
    upperbound = [h_bounds[1], s_bounds[1], v_bounds[1]]

    return [lowerbound, upperbound]
    
def buildMask(frame, hsvRange, mt = True, mtKernel = 7):
    lowerbound = np.array(hsvRange[0])
    upperbound = np.array(hsvRange[1])
    colorMask = cv.inRange(frame, lowerbound, upperbound)
    if mt:
        kernel = np.ones((mtKernel, mtKernel), np.uint8)
        colorMask = cv.morphologyEx(colorMask, cv.MORPH_OPEN, kernel)
    return colorMask

def getMask(frame, red, green, blue, hOffset = 10, sOffset = 150, vOffset = 150, mt = True, mtKernel = 7):
    color = rgb2hsv(red, green, blue)
    cr = colorRange(color, hOffset, sOffset, vOffset)
    mask = buildMask(frame, cr, mt, mtKernel)
    return mask
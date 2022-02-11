import cv2 as cv
import numpy as np

# File to comiple all colormasking functions into one location

# function to convert rgb to useable hsv color for masks
def rgb2hsv(red, green, blue):
    """Function to convert rgb to useable hsv color for masks

    Args:
        red (int): red value
        green (int): green value
        blue (int): blue value

    Returns:
        np.uint8: matrix with convert hsv values
    """
    color = np.uint8([[[blue, green, red]]]) #puts into BGR
    hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    return hsv_color


# helper function for colorRange
def findBounds(value, offset):
    """Helper Function to calculate bounds for a specific value

    Args:
        value (int): The starting value to create range from
        offset (int): Value to offset by in both directions

    Returns:
        list[int, int]: returns 2 length list of ints with upper and lower bounds in list[0] and list[1] respectivly
    """
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


# Color Range takes in an hsv color and an optional offset for hue, saturation, and value
# and returns a 2 element array with lowerbound and upperbound
def colorRange(hsv, hOffset = 10, sOffset = 150, vOffset = 150):
    """Finds color range for given hsv value

    Args:
        hsv (list[int]): list with HSV values
        hOffset (int, optional): Amount to offset hue by. Defaults to 10.
        sOffset (int, optional): Amount to offset saturation by. Defaults to 150.
        vOffset (int, optional): Amount to offset value by. Defaults to 150.

    Returns:
        list[List[int]: returns list of lists containing upper and lower bound for h, s, and v
    """
    h_val = hsv[0][0][0]
    s_val = hsv[0][0][1]
    v_val = hsv[0][0][2]

    h_bounds = findBounds(h_val, hOffset)
    s_bounds = findBounds(s_val, sOffset)
    v_bounds = findBounds(v_val, vOffset)

    lowerbound = [h_bounds[0], s_bounds[0], v_bounds[0]]
    upperbound = [h_bounds[1], s_bounds[1], v_bounds[1]]

    return [lowerbound, upperbound]
    
# BuildMask can be used individually but is called by getMask. Takes in the frame, the hsv range,
# and optinal whether or not you want morphalogical tranformation, and the morphalogical tranformation kernel size
# returns the mask
def buildMask(frame, hsvRange, mt = True, mtKernel = 7, itera = 1):
    """Builds a mask given a frame and hsvRange

    Args:
        frame (numpy.ndarray): HSV frame to build mask off of
        hsvRange (list): detection range for hsv values to mask
        mt (bool, optional): Whether or not to apply morphological transformation. Defaults to True.
        mtKernel (int, optional): Kernel Size to apply in mt, needs mt to be true to use. Defaults to 7.
        itera (int, optional): Number of times to run mt. Defaults to 1.

    Returns:
        numpy.ndarray: returns color mask based on given frame
    """
    lowerbound = np.array(hsvRange[0])
    upperbound = np.array(hsvRange[1])
    colorMask = cv.inRange(frame, lowerbound, upperbound)
    if mt:
        kernel = np.ones((mtKernel, mtKernel), np.uint8)
        colorMask = cv.morphologyEx(colorMask, cv.MORPH_CLOSE, kernel)
        colorMask = cv.morphologyEx(colorMask, cv.MORPH_OPEN, kernel)
        colorMask = cv.erode(colorMask, kernel, iterations= itera)
        colorMask = cv.dilate(colorMask, kernel, iterations= itera)
    return colorMask

# getMask combines all steps of building the mask, only requires and hsv frame and rgb values.
# Takes in an optional offsets for h, s, and v along with the mt and kernal option for buildMask 
def getMask(frame, red, green, blue, hOffset = 10, sOffset = 150, vOffset = 150, mt = True, mtKernel = 7):
    """All-in-one function for building a color mask

    Args:
        frame (numpy.ndarray): HSV Frame to build mask off of
        red (int): red color value
        green (int): green color value
        blue (int): blue color value
        hOffset (int, optional): Amount to offset hue by. Defaults to 10.
        sOffset (int, optional): Amount to offset saturation by. Defaults to 150.
        vOffset (int, optional): Amount to offset value by. Defaults to 150.
        mt (bool, optional): Whether or not to apply morphological transformations. Defaults to True.
        mtKernel (int, optional): Kernel Size to apply in mt, needs mt to be true to use. Defaults to 7.

    Returns:
        numpy.ndarray: returns color mask based on given frame
    """
    color = rgb2hsv(red, green, blue)
    cr = colorRange(color, hOffset, sOffset, vOffset)
    mask = buildMask(frame, cr, mt, mtKernel)
    return mask
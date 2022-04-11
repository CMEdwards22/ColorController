from os import truncate
import cv2 as cv
import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import numpy as np


class colorTrackingParams:
    """Class to store all parameters needed to run tracker.
    The color tracking parameters can be changed and are the following:

    vidCap: the video capture of the computer. Auto generated but can be replaced if needed
    red (int): red color value. Defaults to 255
    green (int): green color value. Defaults to 0
    blue (int): blue color value. Defaults to 0
    hOffset (int): Amount to offset hue by. Defaults to 10.
    sOffset (int): Amount to offset saturation by. Defaults to 150.
    vOffset (int): Amount to offset value by. Defaults to 150.
    mt (bool): Whether or not to apply morphological transformations. Defaults to True.
    mtKernel (int): Kernel Size to apply in mt, needs mt to be true to use. Defaults to 7.
    itera (int): Number of times to run mt. Defaults to 1.
    minArea (int): minimum area a blob can be.
    maxArea (int): maximun area a blob can be.
    simple (bool): Option to use simple blob tracking or multi-blob detection, set to true for simple. Defaults to True.
    debugMode (bool): Debug mode to print blob values to terminal. Defaults to False.
    circle_red (int): red RGB/BGR color value for drawn circle. Defaults to 0.
    circle_green (int): green RGB/BGR color value for drawn circle. Defaults to 0.
    circle_blue (int): blue RGB/BGR color value for drawn circle. Defaults to 255.
    showTracker (bool): if the frame and tracker should be shown. Defaults to True.
    showMask (bool): if the color mask should be shown. Defaults to False.
    trackerTitle (String): the title name of the color tracker window
    maskTitle (String): the title of the name of the color mask window
    checkHooks (bool): if the update function should check for hooks or not. Defaults to True.
    hooks (dict): a dict list of triggers set by setTrigger function. Do not change manually. Defaults to {}.
    showOptions (bool): if the options panel and dynamic sliders should be shown. Defaults to False.
    optionsPanel (None): placeholder for the window for the option panels. To set use the enableOptions(params) function. Defualts to None.
    advanceOptions (bool): if additonal options should be shown in the options panel and options readout. Defualts to False.
    showOptionVals (bool): if a seperate GUI showing current values for parameter should be shown. Defualts to False.
    """
    def __init__(self):
        self.vidCap = vc.getVideoCapture()
        self.red = 255
        self.green = 0
        self.blue = 0
        self.hOffset = 10
        self.sOffset = 150
        self.vOffset = 150
        self.mt = True
        self.mtKernel = 7
        self.itera = 1
        self.minArea = 0
        self.maxArea = 100000
        self.simple = True
        self.debugMode = False
        self.circle_red = 0
        self.circle_green = 0
        self.circle_blue = 255
        self.showTracker = True
        self.showMask = False
        self.trackerTitle = "Tracker"
        self.maskTitle = "Mask"
        self.checkHooks = True
        self.hooks = {}
        self.showOptions = False
        self.optionsPanel = None
        self.advanceOptions = False
        self.showOptionVals = False

    def changeRed(self, val):
        self.red = val

    def changeGreen(self, val):
        self.green = val

    def changeBlue(self, val):
        self.blue = val

    def changeHueOffset(self, val):
        self.hOffset = val

    def changeSatOffset(self, val):
        self.sOffset = val

    def changeValOffset(self, val):
        self.vOffset = val

    def changeItera(self, val):
        self.itera = val

    def changeminArea(self, val):
        self.minArea = val

    def changemaxArea(self, val):
        self.maxArea = val

    def changeCircleRed(self, val):
        self.circle_red = val

    def changeCircleGreen(self, val):
        self.circle_green = val

    def changeCircleBlue(self, val):
        self.circle_blue = val

    def changeDebugMode(self, val):
        if val == 1:
            self.debugMode = True
        else:
            self.debugMode = False

    def changeKernel(self, val):
        self.mtKernel = val
    

def setHook(params, x, y, function):
    """Function used to set a hook with an x and y coordinate.

    Args:
        params (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        function (_type_): _description_
    """
    params.hooks[(x,y)] = function


def removeHook(params, x, y):
    del params.hooks[(x,y)]


def setRangeHook(params, x1, y1, x2, y2, function):
    for x in range (x1, x2):
        for y in range(y1, y2):
            params.hooks[(x,y)] = function


def checkHooks(params, x, y):
    hook = params.hooks.get((x,y))
    if hook is not None:
        hook()


def incTupleCoord(tup, val):
    newY = tup[1] + val
    return (tup[0], newY)


def update(params):
    """Update function that updates all needed data which includes frames, masks, blobdetectors, and imshows.

    Args:
        params (_type_): Parameter class object containing all parameter settings for color tracker.

    Returns:
        x, y, size, blobCount: 4 ints with the first blob's x coord, y coord, size, and the total number of blobs
    """


    if params.showOptionVals:
        font = cv.FONT_HERSHEY_SIMPLEX
        textloc = (0,0)
        fontScale = 0.5
        fontColor = (255,255,255)
        thickness = 1
        linetype = 2
        img = np.zeros((225,225,3), np.uint8)

        redText = "Red: " + str(params.red)
        greenText = "Green: " + str(params.green)
        blueText = "Blue: " + str(params.blue)
        hueText = "Hue Offset: " + str(params.hOffset)
        satText = "Saturation Offset: " + str(params.sOffset)
        lightText = "Lightness Offset: " + str(params.vOffset)
        if params.mt:
            ppText = "Postprocessing: " + str(params.itera)
        else:
            ppText = "Postprocessing: Disabled"

        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, redText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, greenText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, blueText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, hueText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, satText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, lightText, textloc, font, fontScale, fontColor, thickness, linetype)
        textloc = incTupleCoord(textloc, 15)
        cv.putText(img, ppText, textloc, font, fontScale, fontColor, thickness, linetype)

        if params.advanceOptions:
            minText = "Minimum Area: " + str(params.minArea)
            maxText = "Maximum Area: " + str(params.maxArea)
            crText = "Circle Red: " + str(params.circle_red)
            cgText = "Circle Green: " + str(params.circle_green)
            cbText = "Circle Blue: " + str(params.circle_blue)
            if params.debugMode:
                debugText = "Debug Mode: Enabled"
            else:
                debugText = "Debug Mode: Disabled"
            kText = "Kernal Size: " + str(params.mtKernel) + "x" + str(params.mtKernel)

            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, minText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, maxText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, crText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, cgText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, cbText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, debugText, textloc, font, fontScale, fontColor, thickness, linetype)
            textloc = incTupleCoord(textloc, 15)
            cv.putText(img, kText, textloc, font, fontScale, fontColor, thickness, linetype)

    if params.showOptions:
        if not params.showOptionVals:
            img = np.zeros((1,1,3), np.uint8)
        cv.imshow(params.optionsPanel, img)
    elif params.showOptionVals:
        cv.imshow("Option Values", img)
        

    # Creates needed frames, hsv frames, and masks
    hsvFrame = vc.hsvFrame(params.vidCap)
    frame = vc.getFrame(params.vidCap)
    mask = cm.getMask(hsvFrame, params.red, params.green, params.blue, hOffset=params.hOffset, sOffset=params.sOffset, vOffset=params.vOffset, mt= params.mt, mtKernel= params.mtKernel, itera= params.itera)

    # Builds tracker and gets the needed values
    x,y,size,blobCount = ct.buildBlobTracker(frame, mask, params.minArea, params.maxArea, simple= params.simple, debugMode= params.debugMode, circle_red= params.circle_red, circle_green= params.circle_green, circle_blue= params.circle_blue)

    # checks if hooks are enable and if they should be triggered right now or not
    if params.checkHooks:
        if blobCount > 0:
            intX = int(x)
            intY = int(y)
            checkHooks(params, intX, intY)

    # Determines if tracker and mask should be shown or not
    if params.showTracker:
        cv.imshow(params.trackerTitle, frame)
    if params.showMask:
        cv.imshow(params.maskTitle, mask)


    return x,y,size,blobCount


def destroy():
    """Wrapper function to close all openCV windows
    """
    cv.destroyAllWindows()


#def nothing():
#    """Empty Function required for createTrackbar
#    """
#    pass

def changeRed(val, params):
    params.red = val

def enableOptions(params):
    params.showOptions = True
    params.optionsPanel = cv.namedWindow("Options", cv.WINDOW_NORMAL)
    cv.createTrackbar("Red", "Options", params.red, 255, params.changeRed)
    cv.createTrackbar("Green", "Options", params.green, 255, params.changeGreen)
    cv.createTrackbar("Blue", "Options", params.blue, 255, params.changeBlue)
    cv.createTrackbar("Hue Offset", "Options", params.hOffset, 255, params.changeHueOffset)
    cv.createTrackbar("Saturation Offset", "Options", params.sOffset, 255, params.changeSatOffset)
    cv.createTrackbar("Lightness Offset", "Options", params.vOffset, 255, params.changeValOffset)
    cv.createTrackbar("Postprocessing", "Options", params.itera, 15, params.changeItera)
    if params.advanceOptions:
        cv.createTrackbar("Minimum Area", "Options", params.minArea, 1000000, params.changeminArea)
        cv.createTrackbar("Maximum Area", "Options", params.maxArea, 1000000, params.changemaxArea)
        cv.createTrackbar("Circle Red", "Options", params.circle_red, 255, params.changeCircleRed)
        cv.createTrackbar("Circle Green", "Options", params.circle_green, 255, params.changeCircleGreen)
        cv.createTrackbar("Circle Blue", "Options", params.circle_blue, 255, params.changeCircleBlue)
        cv.createTrackbar("Debug Mode", "Options", 0, 1, params.changeDebugMode)
        cv.createTrackbar("Kernel Size", "Options", params.mtKernel, 15, params.changeKernel)
    cv.resizeWindow("Options", 800, 70)

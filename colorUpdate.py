import cv2 as cv
import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct


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
    trackerTitle (String): the title name of the color tracker window. Defaults to "Tracker"
    maskTitle (String): the title of the name of the color mask window. Defaults to "Mask"
    showOptions (bool): if options gui should be displayed. Defualts to True
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
        self.maxArea = 10000
        self.simple = True
        self.debugMode = False
        self.circle_red = 0
        self.circle_green = 0
        self.circle_blue = 255
        self.showTracker = True
        self.showMask = False
        self.trackerTitle = "Tracker"
        self.maskTitle = "Mask"
        self.showOptions = True
    


def update(params):
    hsvFrame = vc.hsvFrame(params.vidCap)
    frame = vc.getFrame(params.vidCap)
    mask = cm.getMask(hsvFrame, params.red, params.green, params.blue, hOffset=params.hOffset, sOffset=params.sOffset, vOffset=params.vOffset, mt= params.mt, mtKernel= params.mtKernel, itera= params.itera)
    x,y,size,blobCount = ct.buildBlobTracker(frame, mask, params.minArea, params.maxArea, simple= params.simple, debugMode= params.debugMode, circle_red= params.circle_red, circle_green= params.circle_green, circle_blue= params.circle_blue)
    if params.showTracker:
        cv.imshow(params.trackerTitle, frame)
    if params.showMask:
        cv.imshow(params.maskTitle, mask)
    return x,y,size,blobCount

def destroy():
    """Wrapper function to close all openCV windows
    """
    cv.destroyAllWindows()
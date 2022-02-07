import cv2 as cv
import numpy as np

# Builds a simple set of parameters for blob detection
def buildSimpleParams(min_area, max_area):
    blobDetectorParams = cv.SimpleBlobDetector_Params()

    # Threshold doesn't matter since operationing on a binary color mask
    blobDetectorParams.minThreshold = 0
    blobDetectorParams.maxThreshold = 255
    # Sets max and min area according to parameters
    blobDetectorParams.filterByArea = True
    blobDetectorParams.minArea = min_area
    blobDetectorParams.maxArea = max_area
    # Convexity and Inertia disabled for simple params
    blobDetectorParams.filterByConvexity = False
    blobDetectorParams.filterByInertia = False

    return blobDetectorParams


# gets all the key points (blobs)
def getKeyPoints(mask, params):
    # Inverts the mask to allow key point detention to work properly
    invertMask = 255 - mask
    blobDetector = cv.SimpleBlobDetector_create(params)
    keyPoints = blobDetector.detect(invertMask)
    return keyPoints

# Gets blob data from set of keypoints. Data includes blob count, x axis
# y axis, and blob size
def getBlobData(keypoints):
    BlobCount = len(keypoints)

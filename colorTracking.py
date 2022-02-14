import cv2 as cv


def buildSimpleParams(min_area, max_area):
    """builds a simple set of parameters for blob detection

    Args:
        min_area (int): minimum area of blob needed to track value
        max_area (int): maximum area of blob needed to track value

    Returns:
       cv2.SimpleBlobDetector_Params : parameter set for blob detector
    """
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
    """Used to find all keypoints (blobs)

    Args:
        mask (numpy.ndarray): mask to find blobs on
        params (cv2.SimpleBlobDetector_Params): parameters to use to determine key points

    Returns:
        tuple: returns tuple of keypoints
    """
    # Inverts the mask to allow key point detention to work properly
    invertMask = 255 - mask
    blobDetector = cv.SimpleBlobDetector_create(params)
    keyPoints = blobDetector.detect(invertMask)
    return keyPoints


def getSingleBlobData(keypoint):
    """Helper function to get data from a single key point (blob)

    Args:
        keypoint (tuple): keypoint to extract data from

    Returns:
        int: 3 ints determining x axis, y axis, and size of blob in that order
    """
    x = keypoint.pt[0]
    y = keypoint.pt[1]
    size = keypoint.size
    return x,y,size


# Gets blob data from first keypoint. Data includes blob count, x axis
# y axis, and blob size. Also adds circle to main vidcap
def simpleBlobTracker(keypoints, frame, debugMode= False, circle_red= 0, circle_green=0, circle_blue=255):
    """Builds a sinple blob tracker that only returns data on first blob detected in the frame

    Args:
        keypoints (tuple): [description]
        frame (numpy.ndarray): frame to apply blob detection to
        debugMode (bool, optional): activate debug mode which will print out x, y, size, and blob count to terminal. Defaults to False.
        circle_red (int, optional): red RGB/BGR color value for drawn circle. Defaults to 0.
        circle_green (int, optional): green RGB/BGR color value for drawn circle. Defaults to 0.
        circle_blue (int, optional): blue RGB/BGR color value for drawn circle. Defaults to 255.

    Returns:
        int: returns 3 ints x-axis, y-axis, and size of the first blob detected
    """
    BlobCount = len(keypoints)
    if BlobCount > 0:
        x, y, size = getSingleBlobData(keypoints[0])
        # Dividing circle size by two so it looks nice
        # Draw circle on main frame
        cv.circle(frame, (int(x),int(y)), int(size / 2), (circle_blue, circle_green, circle_red), 2)

        if debugMode:
            sText = "Blob 0 Size = " + "{:.2f}".format(size)
            xText = "Blob 0 X-Axis = " + "{:.2f}".format(x)
            yText = "Blob 0 Y-Axis = " + "{:.2f}".format(y)
            print("Blob Count: ", BlobCount)
            print(xText)
            print(yText)
            print(sText)
    else:
        x = -1
        y = -1
        size = -1
        if debugMode:
            print("No blobs detected")
    return x, y, size, BlobCount


# Warning: could run very slow when used
# Returns a list of dictinaries of all key point data
def multiBlobTracker(keypoints, frame, debugMode= False, circle_red= 0, circle_green=0, circle_blue=255):
    """Builds a multi blob tracker WARNING: WIP - COULD CAUSE MAJOR PERFORMACE ISSUES

    Args:
        keypoints (tuple): [description]
        frame (numpy.ndarray): frame to apply blob detection to
        debugMode (bool, optional): activate debug mode which will print out x, y, size, and blob count to terminal. Defaults to False.
        circle_red (int, optional): red RGB/BGR color value for drawn circle. Defaults to 0.
        circle_green (int, optional): green RGB/BGR color value for drawn circle. Defaults to 0.
        circle_blue (int, optional): blue RGB/BGR color value for drawn circle. Defaults to 255.

    Returns:
        list: Returns a list of dicts for each blob detected containing the blob number, x, y, and size
    """
    BlobCount = len(keypoints)
    if debugMode:
            print("Blob Count: ", BlobCount)
    if BlobCount > 0:
        counter = 0
        pointData = []
        for blob in BlobCount:
            x, y, size = getSingleBlobData(blob)
            cv.circle(frame, (int(x),int(y)), int(size / 2), (circle_blue, circle_green, circle_red), 2)
            blobDict = {
                "BlobNumber": counter,
                "x": x,
                "y": y,
                "size": size
            }
            pointData.append(blobDict)

            if debugMode:
                nText = "Blob Number: " + str(counter)
                sText = "Blob 0 Size = " + "{:.2f}".format(size)
                xText = "Blob 0 X-Axis = " + "{:.2f}".format(x)
                yText = "Blob 0 Y-Axis = " + "{:.2f}".format(y)
                print(nText)
                print(xText)
                print(yText)
                print(sText)

            counter += 1
    return pointData

def buildBlobTracker(frame, mask, minArea, maxArea, simple=True, debugMode= False, circle_red= 0, circle_green=0, circle_blue=255):
    """All-in-one step for building a blob tracker

    Args:
        frame (numpy.ndarray): Frame to apply blob tracking to.
        mask (numpy.ndarray): color mask to determine blobs
        minArea (int): minimum area a blob can be.
        maxArea (int): maximun area a blob can be.
        simple (bool, optional): Option to use simple blob tracking or multi-blob detection, set to true for simple. Defaults to True.
        debugMode (bool, optional): Debug mode to print blob values to terminal. Defaults to False.
        circle_red (int, optional): red RGB/BGR color value for drawn circle. Defaults to 0.
        circle_green (int, optional): green RGB/BGR color value for drawn circle. Defaults to 0.
        circle_blue (int, optional): blue RGB/BGR color value for drawn circle. Defaults to 255.

    Returns:
        int/list: returns x,y, and size ints for simple= True or returns list of dicts of blob data for simple= False
    """
    params = buildSimpleParams(minArea, maxArea)
    keypoints = getKeyPoints(mask, params)
    if simple:
        x,y,size,blobCount = simpleBlobTracker(keypoints, frame, debugMode, circle_red, circle_green, circle_blue)
        return x,y,size,blobCount
    else:
        data = multiBlobTracker(keypoints, frame, debugMode, circle_red, circle_green, circle_blue)
        return data, 0, 0

import cv2 as cv

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


def getSingleBlobData(keypoint):
    x = keypoint.pt[0]
    y = keypoint.pt[1]
    size = keypoint.size


# Gets blob data from first keypoint. Data includes blob count, x axis
# y axis, and blob size. Also adds circle to main vidcap
def simpleBlobTracker(keypoints, frame, debugMode= False, circle_red= 0, circle_green=0, circle_blue=255):
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
        x,y,size = None
        if debugMode:
            print("No blobs detected")
    return x,y,size


# Warning: could run very slow when used
# Returns a list of dictinaries of all key point data
def multiBlobTracker(keypoints, frame, debugMode= False, circle_red= 0, circle_green=0, circle_blue=255):
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
    params = buildSimpleParams(minArea, maxArea)
    keypoints = getKeyPoints(mask, params)
    if simple:
        x,y,size = simpleBlobTracker(keypoints, frame, debugMode, circle_red, circle_green, circle_blue)
        return x,y,size
    else:
        data = multiBlobTracker(keypoints, frame, debugMode, circle_red, circle_green, circle_blue)
        return data

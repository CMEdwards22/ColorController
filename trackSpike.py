import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import numpy as np


vidCap = vc.getVideoCapture()
while True:
    frame = vc.hsvFrame(vidCap)
    frame2 = vc.getFrame(vidCap)
    hsv = cm.rgb2hsv(255,0,0)
    hsvR = cm.colorRange(hsv)
    mask = cm.buildMask(frame, hsvR, itera= 9)

    p_img = 255 - mask
    maskImg = cv.bitwise_and(frame, frame, mask = mask)

    tracker, here = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    output = cv.drawContours(mask, tracker, -1, (255, 0, 0), 3)

    blobDetectorParams = cv.SimpleBlobDetector_Params()

    blobDetectorParams.minThreshold = 0
    blobDetectorParams.maxThreshold = 255
    blobDetectorParams.filterByArea = True
    blobDetectorParams.minArea = 250
    blobDetectorParams.maxArea = 10000
    blobDetectorParams.filterByConvexity = False
    #blobDetectorParams.minConvexity = 0.5
    blobDetectorParams.filterByInertia = False
    #blobDetectorParams.minInertiaRatio = 0.5

    blobDetector = cv.SimpleBlobDetector_create(blobDetectorParams)

    invertMask = 255 - mask

    keyPoints = blobDetector.detect(invertMask)
    blobCount = len(keyPoints)
    print("Blob count: ", blobCount)
    #img = cv.drawKeypoints(img, keyPoints, np.array([]), (255, 0, 0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # have the prints as optional debug feature in method
    if blobCount > 0:
        # Write X position of first blob
        blob_x = keyPoints[0].pt[0]
        text2 = "X=" + "{:.2f}".format(blob_x )
        #cv.putText(frame, text2, (5,50), font, 1, (0, 255, 0), 2)
        print(text2)

        # Write Y position of first blob
        blob_y = keyPoints[0].pt[1]
        text3 = "Y=" + "{:.2f}".format(blob_y)
        #cv.putText(frame, text3, (5,75), font, 1, (0, 255, 0), 2)        
        print(text3)

        # Write Size of first blob
        blob_size = keyPoints[0].size
        text4 = "S=" + "{:.2f}".format(blob_size)
        #cv.putText(frame, text4, (5,100), font, 1, (0, 255, 0), 2)    
        print(text4)

        # Draw circle to indicate the blob
        cv.circle(frame2, (int(blob_x),int(blob_y)), int(blob_size / 2), (255, 0, 0), 2) 


    cv.imshow("Output", frame2)
    #cv.imshow("img", img)



    cv.imshow("buildMaskTest", mask)
    if cv.waitKey(1) == ord('q'):  
        break

cv.destroyAllWindows()


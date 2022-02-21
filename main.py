from cv2 import imshow
import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import colorUpdate as cu

def main1():
    print("Test main")
    vidCap = vc.getVideoCapture() #includes error checking
    while True:
        frame = vc.getFrame(vidCap)
        cv.imshow('TitleExample', frame)
        if cv.waitKey(1) == ord('q'):  
            break

def main2():
    color = cm.rgb2hsv(255,0,0) #test on red
    print("Color: ", color)
    print("Color[0]: ", color[0])
    print("Color[0][0]: ", color[0][0])
    print("Color[0][0][0]: ", color[0][0][0])
    cr = cm.colorRange(color, 50, 150, 150)
    cr2 = cm.colorRange(color)
    print("cr: ", cr)
    print("cr2: ", cr2)



def main3():
    vidCap = vc.getVideoCapture()
    while True:
        frame = vc.hsvFrame(vidCap)
        mask = cm.getMask(frame, 255, 0, 0)
        cv.imshow("title", frame)
        cv.imshow("Please work", mask)
        if cv.waitKey(1) == ord('q'):  
            break

def main4():
    vidCap = vc.getVideoCapture()
    while True:
        frame = vc.hsvFrame(vidCap)
        hsv = cm.rgb2hsv(255,0,0)
        hsvR = cm.colorRange(hsv)
        mask = cm.buildMask(frame, hsvR, mtKernel= 3)
        cv.imshow("buildMaskTest", mask)
        if cv.waitKey(1) == ord('q'):  
            break

def main5():
    vidCap = vc.getVideoCapture()
    while True:
        hsvFrame = vc.hsvFrame(vidCap)
        frame = vc.getFrame(vidCap)
        mask = cm.getMask(hsvFrame, 255, 0, 0, itera=6)
        x,y,size,blobCount = ct.buildBlobTracker(frame, mask, 0, 30000) 
        cv.imshow("Frame with Color Tracking", frame)
        cv.imshow("Red Color Mask", mask)
        if blobCount > 0:
            print("\n")
            print("Total blob count: ", blobCount)
            print("x : ", x)
            print("y : ", y)
            print("size : ", size)
        else:
            print("No blobs detected")
        if cv.waitKey(1) == ord('q'):  
            break

def main():
    params = cu.colorTrackingParams()
    params.showMask = False
    params.maxArea = 30000
    params.itera = 6
    params.trackerTitle = "Test tracker title"
    params.maskTitle = "Test mask title"
    while True:
        x, y, size, blobCount = cu.update(params)
        if blobCount > 0:
            print("\n")
            print("Total blob count: ", blobCount)
            print("x : ", x)
            print("y : ", y)
            print("size : ", size)
        else:
            print("No blobs detected")
        if cv.waitKey(1) == ord('q'):  
            break
    







if __name__ == "__main__":
    main()
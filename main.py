import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import colorUpdate as cu
import tkinter as tk
import numpy as np

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

def main6():
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
    
def main7broke():
    params = cu.colorTrackingParams()
    #params.showTracker = False
    #params.itera = 6

    # all gui stuff --
    root = tk.Tk()
    root.title("Red Color tracked GUI")
    drawing = tk.Canvas(root, bg='white', height=720, width=1280)
    drawing.pack()
    # --
    while True:
        x,y,size,blobCount = cu.update(params)
        if blobCount > 0:
            # Used to draw oval into gui
            drawing.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="red", outline="")
        # used to update gui
        root.update()
        if cv.waitKey(0) == ord('q'):
            break


#def quitAll():
#    root.protocol('WM_DELETE_WINDOW', quitAll)

def main8():
    def quitAll():
        print("quitting all...")
        root.destroy()
        cu.destroy()
    params = cu.colorTrackingParams()
    params.itera = 6

    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', quitAll)
    root.title("Red color draw test")
    drawing = tk.Canvas(root, bg='white', height=720, width= 1280)
    drawing.pack()
    while True:
        #print("loop print test")
        x,y,size,bc = cu.update(params)

        if bc > 0:
            print('test')
            drawing.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="red", outline="")
        
        root.update()
        #if cv.waitKey(1) == ord('q'):
        #    root.destroy()
        #    break

def nothing(x):
    pass
    
def main():
    params = cu.colorTrackingParams()
    #cu.enableOptions(params)
    img = np.zeros((1,1,3), np.uint8)
    x = cv.namedWindow("Options", cv.WINDOW_NORMAL)
    cv.createTrackbar("Hue", "Options", 0, 180, nothing)
    while True:
        #imshow("Options", img)
        cv.imshow(x)
        if cv.waitKey(1) == ord('q'):
            break

def main10():
    params = cu.colorTrackingParams()
    cu.enableOptions(params)
    while True:
        x,y,z,w = cu.update(params)
        if cv.waitKey(1) == ord("q"):
            break



cv.destroyAllWindows()




if __name__ == "__main__":
    main10()
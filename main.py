from cv2 import destroyWindow, imshow
import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import colorUpdate as cu
import tkinter as tk

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
    
def main7GuiFixTest():
    params = cu.colorTrackingParams()
    params.showMask = False
    #params.showTracker = False
    params.maxArea = 30000
    params.itera = 6
    params.trackerTitle = "Test tracker title"
    params.maskTitle = "Test mask title"
    while True:
        x, y, size, blobCount = cu.update(params)
        if cv.waitKey(1) == ord('q'):
            #cv.destroyAllWindows()  
            break


#def quitAll():
#    root.protocol('WM_DELETE_WINDOW', quitAll)

def main():
    def quitAll():
        print("quitting all...")
        root.destroy()
        cu.destroy()
    params = cu.colorTrackingParams()
    params.itera = 6

    root = tk.Tk()
    #root.protocol('WM_DELETE_WINDOW', quitAll)
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
        if cv.waitKey(1) == ord('q'):
            root.destroy()
            break

    
def sample():
    params = cu.colorTrackingParams()
    params.itera = 4
    params.showMask = True
    params.red = 0
    params.blue = 255
    params.green = 0
    params.debugMode = True
    params.maxArea = 10000000
    while True:
        x,y,size,count = cu.update(params)

        if cv.waitKey(1) == ord('q'):
            break


def isLeft():
    print("Left")

def isRight():
    print("Right")

def demo():
    params = cu.colorTrackingParams()
    params.itera = 3

    # Selecting color to detect
    params.red = 0
    params.blue = 255
    params.green = 0

    # set hooks
    cu.setRangeHook(params, 0, 0, 320, 480, isLeft)
    cu.setRangeHook(params, 320, 0, 640, 480, isRight)

    # Stuff for tkinter gui to show of gui connection, not apart of color based controller
    root = tk.Tk()
    root.title("Drawing board")
    drawing = tk.Canvas(root, bg='white', height=480, width= 640)
    drawing.pack()

    while True:
        x,y,size,count = cu.update(params)

        if count > 0:
            # add circle to drawing board based on size and location of blobs
            drawing.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="blue", outline="")
        
        # update function for tkinter
        root.update()
        
        if cv.waitKey(1) == ord('q'):
            root.destroy()
            break





cv.destroyAllWindows()




if __name__ == "__main__":
    #main()
    #sample()
    demo()
    #main7GuiFixTest()
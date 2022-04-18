import cv2 as cv
import colorUpdate as cu
import tkinter as tk

def isTopLeft():
    print("Top Left")

def isTopRight():
    print("Top Right")

def isBottomLeft():
    print("Bottom Left")

def isBottomRight():
    print("Bottom Right")


def main():
    params = cu.colorTrackingParams()
    params.showMask = True

    # Selecting color to detect
    params.red = 0
    params.blue = 255
    params.green = 0

    # Enabling options
    cu.enableOptions(params)

    # set hooks
    cu.setRangeHook(params, 0, 0, 320, 240, isTopLeft)
    cu.setRangeHook(params, 320, 0, 640, 240, isTopRight)
    cu.setRangeHook(params, 0, 240, 320, 480, isBottomLeft)
    cu.setRangeHook(params, 320, 240, 640, 480, isBottomRight)

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
    main()
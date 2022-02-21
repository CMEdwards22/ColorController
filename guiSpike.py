import tkinter as tk
import numpy as np

import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import colorUpdate as cu

# Root is like foundation for standard GUI, need Canvas for drawing and such
root = tk.Tk()
root.title("GUI spike test")

drawing = tk.Canvas(root, bg='white', height=720, width=1280)

#coord = 10, 10, 300, 300
#arc = drawing.create_arc(coord, start=0, extent=150, fill="red")

# Coords are as follows: x0,y0,x1,y1
# x0 and y0 are the xy coords of the top left of circle/oval
# x1 and y1 are the xy coords of the bottom right of circle/oval
#drawing.create_oval(60,60,210,210, fill="red")

# X Axis goes from left right with low values on left and high values on right
# Y Axis goes from top down with low values on top and high values on bottom
#drawing.create_oval(120, 60, 270, 210, fill="blue")


# adds drawing canvas to window
# Apparently don't have to pack at the end, could pack right after creating varaible and add stuff later
drawing.pack()
# Runs the window
#root.mainloop()

#cv.getWindowImageRect('Frame')
#print(frame.shape)

# Same thing as root.mainloop()
#while True:
#    root.update()

# root.destroy() can be used to kill gui like the destroywindows of openCV

#vidCap = vc.getVideoCapture()

# while True:
#         hsvFrame = vc.hsvFrame(vidCap)
#         frame = vc.getFrame(vidCap)
#         mask = cm.getMask(hsvFrame, 255, 0, 0, itera=6)
#         x,y,size,blobCount = ct.buildBlobTracker(frame, mask, 0, 30000) 
#         cv.imshow("Frame with Color Tracking", frame)
#         cv.imshow("Red Color Mask", mask)
#         if blobCount > 0:
#             #print("\n")
#             #print("Total blob count: ", blobCount)
#             #print("x : ", x)
#             #print("y : ", y)
#             #print("size : ", size)
#             drawing.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="red", outline="")
#         #else:
#         #    print("No blobs detected")
#         if cv.waitKey(1) == ord('q'):  
#             break
#         root.update()


xtest = np.arange(1000)
ytest = np.arange(1000)

#print(type(xtest[1]))

params = cu.colorTrackingParams()

params.showTracker = False
print(params.showTracker)
print(params.blue)

counter = 0
y = 200
while True:
    #drawing.create_oval((xtest[counter] - 5, y - 5, xtest[counter] + 5, y + 5, outline="", fill="red")
    drawing.create_oval(xtest[counter] - 15, 200, xtest[counter] - 15, 200, fill="red", outline="")
    counter += 1
    root.update()
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
root.destroy()
import tkinter as tk

import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct

# Root is like foundation for standard GUI, need Canvas for drawing and such
root = tk.Tk()
root.title("GUI spike test")

drawing = tk.Canvas(root, bg='white', height=300, width=300)

#coord = 10, 10, 300, 300
#arc = drawing.create_arc(coord, start=0, extent=150, fill="red")

# Coords are as follows: x0,y0,x1,y1
# x0 and y0 are the xy coords of the top left of circle/oval
# x1 and y1 are the xy coords of the bottom right of circle/oval
drawing.create_oval(60,60,210,210, fill="red")




# adds drawing canvas to window
# Apparently don't have to pack at the end, could pack right after creating varaible and add stuff later
drawing.pack()
# Runs the window
#root.mainloop()

#cv.getWindowImageRect('Frame')
#print(frame.shape)

# Same thing as root.mainloop()
while True:
    root.update()
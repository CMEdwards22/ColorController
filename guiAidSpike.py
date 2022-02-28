import newVideoCapture as vc
import colorMask as cm
import cv2 as cv
import colorTracking as ct
import colorUpdate as cu
import tkinter as tk

def activateHook(function):
    function()

def triggerTest():
    print('test trigger')

def triggerTest2():
    print('test tigger the sequel')

params = cu.colorTrackingParams()
params.itera = 6
cu.setHook(params, 1, 2, triggerTest)
print(params.hooks)

#fun = params.hooks[(1,2)]
#activateHook(fun)

cu.checkHooks(params, 1, 2)

cu.removeHook(params, 1, 2)
print(params.hooks)

#cu.setRangeHook(params, 0, 0, 5, 5, triggerTest2)
#print(params.hooks)

cu.checkHooks(params, 2, 3)
cu.checkHooks(params, 1, 2)
cu.checkHooks(params, 10, 10)

cu.setRangeHook(params, 0, 0, 5000, 5000, triggerTest)
#print(params.hooks)
print("finished storing hashmap")

'''
root = tk.Tk()
root.title("Red color draw test")
drawing = tk.Canvas(root, bg='white', height=720, width= 1280)
drawing.pack()
'''
while True:
    #print("loop print test")
    x,y,size,bc = cu.update(params)

    #if bc > 0:
        #print('test')
        #drawing.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill="red", outline="")
        
    #root.update()
    if cv.waitKey(1) == ord('q'):
        #root.destroy()
        break

    


cv.destroyAllWindows()


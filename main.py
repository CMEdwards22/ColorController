import newVideoCapture as vc
import colorMask as cm
import cv2 as cv

def main1():
    print("Test main")
    vidCap = vc.getVideoCapture() #includes error checking
    while True:
        frame = vc.getFrame(vidCap)
        cv.imshow('TitleExample', frame)
        if cv.waitKey(1) == ord('q'):  
            break

def main():
    color = cm.rgb2hsv(255,0,0) #test on red
    print("Color: ", color)
    print("Color[0]: ", color[0])
    print("Color[0][0]: ", color[0][0])
    print("Color[0][0][0]: ", color[0][0][0])
    cr = cm.colorRange(color, 10, 100, 100)
    print("cr: ", cr)






if __name__ == "__main__":
    main()
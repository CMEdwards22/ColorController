import cv2 as cv
import numpy as np

# This code was inspired by and created from the example give from openCV documentation
# Documentation example can be found here: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

vidCap = cv.VideoCapture(0)  # Assigning video capture to variable, needs the 0 or it breaks (need to figure out why)
if (not vidCap.isOpened()):  # statement to ensure camera is working
    print("Error: Could not open camera, now exiting")
    exit()

yellow = np.uint8([[[0,255,255]]])
hsv_yellow = cv.cvtColor(yellow,cv.COLOR_BGR2HSV)
print(hsv_yellow)

red = np.uint8([[[0,0,255]]])
hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
print("red: ", hsv_red)

while True:  # keep going until program is killed
    # does a frame by frame capture into frame variable and if frame is read in corectly into frameTest boolean
    frameTest, frame = vidCap.read()

    if (not frameTest):  # Another statement to ensure that the frames are working
        print("Error: Frame not read in correctly, now stopping program")
        break

    # Grayscales video, only use if need converting
    display = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    vibrantDisplay = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerBoundYellow = np.array([10,100,100])
    upperBoundYellow = np.array([35,255,255])

    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    lower_red = np.array([0,100,100])
    upper_red = np.array([5,255,255])

    colorMask = cv.inRange(vibrantDisplay, lowerBoundYellow, upperBoundYellow) # gets all colors in range
    mask2 = cv.inRange(vibrantDisplay, lower_blue, upper_blue)

    maskedImage = cv.bitwise_and(frame, frame, mask= colorMask)
    maskedImage2 = cv.bitwise_and(frame, frame, mask= mask2)

    redMask = cv.inRange(vibrantDisplay, lower_red, upper_red)
    imageRedMasked = cv.bitwise_and(frame, frame, mask= redMask)


    # Morphological Transformation test
    kernel = np.ones((7,7), np.uint8) # just like in the ai class
    opening = cv.morphologyEx(redMask, cv.MORPH_OPEN, kernel)
    cv.imshow("Morphological Transformation on Red Mask", opening)


    # Constantly prints the type of each frame, is uint8
    #print(frame.dtype)

    # Displays video in openCV GUI
    cv.imshow('TitleExample', frame)  # frame for standard video input, use display variable for modified version
    #if cv.waitKey(1) == ord('q'):  # Not sure what this line does, I think it might just be a quit key
        # turns out the wait key IS ABSOLUTELY NEEDED becuase you can't use the x button to quit.
    #    break

    # Displays video in openCV GUI
    #cv.imshow('Vibrant Display', vibrantDisplay)  

    #cv.imshow('Please don\'t openCV. Please', colorMask)
    #cv.imshow('Please don\'t openCV. Part 2', maskedImage)
    #cv.imshow('Please don\'t openCV. Part 3', colorMask)
    #cv.imshow('Come on openCV', mask2)
    
    #cv.imshow('Light blue works very well', maskedImage2)
    #cv.imshow('Big Yellow time', maskedImage)
    #cv.imshow('Yellow but not', colorMask)

    cv.imshow("red is easy color made for children", redMask)
    #cv.imshow("Its the mask but redder than before", imageRedMasked)

    if cv.waitKey(1) == ord('q'):  
        break



# Simple end of program stuff to prevent memory leaks
vidCap.release()
cv.destroyAllWindows()
import newVideoCapture as vc
import cv2 as cv

def main():
    print("Test main")
    vidCap = vc.getVideoCapture() #includes error checking
    while True:
        frame = vc.getFrame(vidCap)
        cv.imshow('TitleExample', frame)
        if cv.waitKey(1) == ord('q'):  
            break







if __name__ == "__main__":
    main()
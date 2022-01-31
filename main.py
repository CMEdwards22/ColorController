import newVideoCapture
import cv2 as cv

def main():
    print("Test main")
    vidCap = newVideoCapture.getVideoCapture()
    while True:
        frameTest, frame = vidCap.read()
        if (not frameTest):  # Another statement to ensure that the frames are working
            print("Error: Frame not read in correctly, now stopping program")
            break
        cv.imshow('TitleExample', frame)
        if cv.waitKey(1) == ord('q'):  
            break







if __name__ == "__main__":
    main()
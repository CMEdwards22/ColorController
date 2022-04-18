import cv2 as cv
import colorUpdate as cu


def isLeft():
    print("Left")

def isRight():
    print("Right")


def main():
    # Setting options
    params = cu.colorTrackingParams()

    params.showMask = True
    params.showOptionVals = True

    params.red = 0
    params.blue = 255

    # Enabling dynamic options
    cu.enableOptions(params)


    # Setting hooks
    cu.setRangeHook(params, 0, 0, 320, 480, isLeft)
    cu.setRangeHook(params, 320, 0, 640, 480, isRight)


    while True:
        # Updating to new frame
        x,y,z,w = cu.update(params)

        # Used to quit program
        if cv.waitKey(1) == ord("q"):
            break

cv.destroyAllWindows()

if __name__ == "__main__":
    main()
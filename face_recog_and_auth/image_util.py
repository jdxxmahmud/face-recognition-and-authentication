import cv2
import numpy as np

def show_img_in_windows(givenFile, testFile):


    givenImg = cv2.imread(givenFile, 0)
    givenImg = resize_image(givenImg)

    testImg = cv2.imread(testFile, 0)
    testImg = resize_image(cv2.imread(testFile, 0))


    window_name = "Face Matching"

    hori = np.concatenate((givenImg, testImg), axis=1)
    cv2.imshow(window_name, hori)


    # verti = np.concatenate((givenImg, testImg), axis=0)
    # cv2.imshow(window_name, verti)



    


    

    cv2.waitKey(0)

    cv2.destroyAllWindows()


def resize_image(image, size=(500, 500)):
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)


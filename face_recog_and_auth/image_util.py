import cv2
import numpy as np
from face_util import crop_face

def show_img_in_windows(givenImg, testImg, matching_status):

    bleh = "" if matching_status else " don't"

    givenImg = convert_to_color_image(resize_image(crop_face((givenImg))))
    testImg = convert_to_color_image(resize_image(crop_face(testImg)))

    window_name = f"The faces{bleh} match"

    hori = np.concatenate((givenImg, testImg), axis=1)
    cv2.imshow(window_name, hori)


    # verti = np.concatenate((givenImg, testImg), axis=0)
    # cv2.imshow(window_name, verti)
  
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def resize_image(image, size=(200, 200)):
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)


def convert_to_color_image(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



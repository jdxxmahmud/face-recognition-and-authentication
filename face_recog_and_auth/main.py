import face_recognition as fr
from image_util import show_img_in_windows, resize_image
from face_util import crop_face

givenFile = "images/test1.jpg"
testFile = "images/test2.jpg"

given_image = fr.load_image_file(givenFile)
given_img = resize_image(given_image, size=(500, 500))
given_img_encoding = fr.face_encodings(given_img)[0]


test_image = fr.load_image_file(testFile)
test_img = resize_image(test_image, size=(500, 500))
test_img_encoding = fr.face_encodings(test_img)[0]


results = fr.compare_faces([given_img_encoding], test_img_encoding)

print(f'{givenFile}\n{testFile}\n\n')

if results[0]:
    print("Matched")
    matching_status = True
else:
    print("No match")
    matching_status = False


show_img_in_windows(given_img, test_img, matching_status)


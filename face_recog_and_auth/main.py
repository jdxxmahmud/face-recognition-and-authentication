import face_recognition as fr
from image_util import show_img_in_windows, resize_image

givenFile = "images/given2.jpg"
testFile = "images/test1.jpg"

given_image = fr.load_image_file(givenFile)
given_img = resize_image(given_image)
given_img_encoding = fr.face_encodings(given_img)[0]


test_image = fr.load_image_file(testFile)
test_img = resize_image(test_image)
test_img_encoding = fr.face_encodings(test_img)[0]


results = fr.compare_faces([given_img_encoding], test_img_encoding)

print(f'{givenFile}\n{testFile}\n\n')

if results[0]:
    print("Matched")
else:
    print("No match")

show_img_in_windows(givenFile, testFile)


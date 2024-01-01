from face_recognition import face_locations

def crop_face(image, expansion = 100):
    
    face_loc = face_locations(image)

    if face_loc:
        top, right, bottom, left = face_loc[0]

        top = max(top - expansion, 0)
        left = max(left - expansion, 0)
        bottom = min(bottom + expansion, image.shape[0])
        right = min(right + expansion, image.shape[1])


        face_image = image[top: bottom, left: right]

    else:
        print("Face not found!")
        return image

    return face_image
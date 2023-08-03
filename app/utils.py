import requests
import cv2
import numpy as np
import base64
import face_recognition

"""
    This util service receives a base64 image encoding and an image URL
    encodes the image url
    compares both image encodings
    and returns 
            (1) a percentage match value: 0 indicates no match and 100 indicates a 100% match
            (2) true or false is there is a match or not based on the tolerance level set     
"""

def load_image_from_url(img_url):
    response = requests.get(img_url)
    img_array = np.array(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    return img


def load_image_from_base64(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def get_face_encodings(image):
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # returns a list of faces in the image
    face_locations = face_recognition.face_locations(rgb_image)  #e.g [(231, 795, 498, 527)]

    # Get face encodings for any faces in the image
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    return face_encodings


def compare_faces(face_encodings1, face_encodings2):

    tolerance = 0.6
    
    face_distance = face_recognition.face_distance(face_encodings1, face_encodings2[0])

    clampedDistance = max(0, min(face_distance[0], tolerance))
    match_percentage = 100 * (1 - (clampedDistance/tolerance))
    return match_percentage, bool(face_distance[0] <= tolerance)


# img1 = face_recognition.load_image_file('images/nin.jpg')

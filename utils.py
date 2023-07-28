import requests
import cv2
import numpy as np
import base64
import face_recognition

"""
This function receives a base64 image encoding and an image URL
encodes the image url
compares both image encodings
and returns a percentage match value
cut off mark is 30%, a value below that indicates no match
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
    face_locations = face_recognition.face_locations(rgb_image)  #[(231, 795, 498, 527)]

    # Get face encodings for any faces in the image
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    return face_encodings

def compare_faces(face_encodings1, face_encodings2):
    # If no faces are found, return 0% match
    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        print("no face detected")
        return 0

    tolerance = 1.0
    # Compare faces and return average match percentage
    matches = face_recognition.face_distance(face_encodings1, face_encodings2[0])
    print(matches)

    clampedDistance = max(0, min(matches, tolerance))
    # match_percentage = matches.count(True) / len(matches) * 100
    match_percentage = 100 * (1 - (clampedDistance/tolerance))
    return match_percentage


# img1 = face_recognition.load_image_file('images/nin.jpg')
# known_face_encodings = get_face_encodings(img1)
# test = face_recognition.load_image_file('images/sope2.jpg')

# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = video_capture.read()
#     print(video_capture.read())
#     face_encodings = get_face_encodings(frame)

#     compare_faces(known_face_encodings, face_encodings)

    

# print(compare_faces(get_face_encodings(img1), get_face_encodings(test)))

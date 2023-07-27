from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from face_match.app import *

app = Flask(_name_)

@app.route("/verify", methods=[POST])
async def verify(base64_img:str, image_url:str):
    """
    params
    base64_img: base64 image encoding
    image_url: image url

    returns
    match_value: a percentage match value of the two images
    """

    base64_img = load_image_from_base64(base64_img)
    image_url = load_image_from_url(image_url)

    face_encodings1 = get_face_encodings(base64_img)
    face_encodings2 = get_face_encodings(image_url)

    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        abort(422)
    
    return compare_faces(face_encodings1, face_encodings2)

@app.errorhandler(422)
def unprocessable(error):
    return (jsonify({
        "status": 422,
        "error": "Unprocessable Entity",
        "message": "The image has been processed successfully, but no identifiable face was found. Please ensure that the image is clear and contains a visible face."
    }), 422)


from flask import Flask, request, abort, jsonify
# from flask_cors import CORS, cross_origin
from utils import *

app = Flask(__name__)

@app.route("/verify", methods=["POST"])
async def verify():
    """
    Compares two images to determine a face match.

    Args:
        base64_img(str): base64 image encoding.
        image_url(str): image url.

    Raises:
        HTTPException [404]: Unprocessable Entity.
    
    Returns:
        A json containing a percentage match value of the two images.
        {
            "match_value": result,
            "match_cut_off": "30%"
        }

    """
    data = request.get_json()
    base64_img = load_image_from_base64(data["base64_img"])
    image_url = load_image_from_url(data["image_url"])

    face_encodings1 = get_face_encodings(base64_img)
    face_encodings2 = get_face_encodings(image_url)

    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        abort(422)
    
    
    result = compare_faces(face_encodings1, face_encodings2).tolist()[0]
    return jsonify({
        "match_value": result,
        "match_cut_off": "30%"
    }), 200


@app.errorhandler(422)
def unprocessable(error):
    return (jsonify({
        "status": 422,
        "error": "Unprocessable Entity",
        "message": "No identifiable face was found. Please ensure that the image is clear and contains a visible face."
    }), 422)


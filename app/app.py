from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils import *
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Images(BaseModel):
    base64_img: str
    image_url: str

@app.post("/verify")
async def verify(request: Images):
    print(request, "request")

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
            "match_bool": match_bool,
            "match_value": match_value,
        }

    """
    base64_img = load_image_from_base64(request.base64_img)
    image_url = load_image_from_url(request.image_url)
    print(image_url, "image_url")
    face_encodings1 = get_face_encodings(base64_img)
    face_encodings2 = get_face_encodings(image_url)

    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "status": 422,
                "error": "Unprocessable Entity",
                "message": "No identifiable face was found. Please ensure that the image is clear and contains a visible face."
            }
        )
    
    match_value, match_bool = compare_faces(face_encodings1, face_encodings2)

    response_data = {
        "match_bool": match_bool,
        "match_value": match_value,
    }

    return JSONResponse(content=response_data, status_code=status.HTTP_200_OK)




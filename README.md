# face_match
 a face match backend service

Fork this repository to have a copy of it in your own github account

Clone the forked repo to your PC, this gives you access to the repo locally

Install Python from https://www.python.org/downloads/ if you haven't

cd into the project folder

cd into the backend folder

Ensure a virtual environment has been created and activated by either using

python -m venv venv # to create a virtualenv
source venv/bin/activate # activate for linux
venv\Scripts\activate # activate for windows
Install all dependencies

pip install -r requirements.txt
Run the somman below to start the server

uvicorn app:app --reload
Navigate to http://127.0.0.1:8000/docs to access the Swagger UI docs to test endpoints.

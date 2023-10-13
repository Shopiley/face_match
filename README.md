# face_match
## A face match backend service

## About the project
The facial recognition system assesses the similarity between two faces and provides a percentage as a result. This percentage indicates the confidence level of the system that the two faces are a match. The algorithm uses the Euclidean distance between corresponding points on both faces. The tolerance level has been set to 0.5 which is a level stricter than the default 0.6.

- A `match_value` of 0% suggests that there is no resemblance or match between the two faces being compared – they are completely different.
- A `match_value` of 100% means there is a perfect match; the system is fully confident that the two faces are identical.
- A `match_value` above 0% and up to 100% denotes some degree of similarity between the two faces.

However, due to the potential for false positives and the sensitivity of the system, values below 5% are usually treated as no match to increase the system's reliability. This means that while there might be a very slight resemblance, it is not considered significant enough to denote a match.

Therefore, a match is only confirmed if `match_value` > 5%.

## How to run the project locally

- Fork this repository to have a copy of it in your own github account

- Clone the forked repo to your PC, this gives you access to the repo locally

- Install Python from https://www.python.org/downloads/ if you haven't

- cd into the project folder

- cd into the backend folder

- Ensure a virtual environment has been created and activated by either using

```
python -m venv venv # to create a virtualenv
source venv/bin/activate # activate for linux
venv\Scripts\activate # activate for windows
```

- Install all dependencies

```
pip install -r requirements.txt
```

- Run the command below to start the server

```
uvicorn app:app --reload
```

- Navigate to http://127.0.0.1:8000/docs to access the Swagger UI docs to test endpoints.

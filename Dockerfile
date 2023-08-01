FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt .
COPY ./packages.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.app:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", $PORT]


FROM python:3.10.12

WORKDIR /code

COPY ./requirements.txt .
COPY ./packages.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.app:app", "--reload", "--proxy-headers", "--host", "0.0.0.0"]

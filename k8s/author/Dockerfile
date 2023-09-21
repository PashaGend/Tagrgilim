
FROM python:latest


COPY ./requirements.txt /app/requirements.txt
COPY ./main_author.py /app/main_author.py
COPY ./Pavel.json /app/Pavel.json


WORKDIR /app

RUN pip install -r requirements.txt

RUN /bin/bash

CMD uvicorn main_author:app --host 0.0.0.0 --port 8000

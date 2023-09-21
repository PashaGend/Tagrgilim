
FROM python:latest


COPY ./requirements.txt /app/requirements.txt
COPY ./main_book.py /app/main_book.py
COPY ./Pavel.json /app/Pavel.json


WORKDIR /app

RUN pip install -r requirements.txt

CMD uvicorn main_book:app --host 0.0.0.0 --port 8000

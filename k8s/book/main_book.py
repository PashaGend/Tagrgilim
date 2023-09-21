from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()


with open("Pavel.json") as json_file:
    data = json.load(json_file)

#@app.get("/")
#def root():
#    return {"message": "Welcome to my FastAPI project!!!!!!"}


@app.get("/book/{book_name}")
def read_item(book_name: str):
    for item in data["books"]:
        if item["book"] == book_name:
            return item
    return {"error": "This book was not found"}

from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()


with open("Pavel.json") as json_file:
    data = json.load(json_file)

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI project!!!!!!"}


@app.get("/author/{author_name}")
def read_item(author_name: str):
    for item in data["authors"]:
        if item["author"] == author_name:
            return item
    return {"error": "This author was not found"}

import imp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"data":"here"}

@app.get("/user")
def home():
    return {"data":"user"}
# FASTAPI

from fastapi import FastAPI
from dotenv import load_dotenv
import requests, json, os
load_dotenv()

APP_2_URL = os.getenv("APP_2_URL")


app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/connection/test")
async def test_connection():
    try:
        app_2_response = requests.get(APP_2_URL).json()
    except Exception as e:
        app_2_response = {"message": "Could not connect to app-2"}
    return {"app-1": {"message": "Hello From App 1"},  "app-2": app_2_response}


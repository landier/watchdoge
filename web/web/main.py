import json
import asyncio
from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

with open('measurements.json', 'r') as file:
    measurements = iter(json.loads(file.read()))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.htm", {"request": request})

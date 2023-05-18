from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory='app/build')
app.mount("/static", StaticFiles(directory="app/build"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
 
@app.get("/all/{td}/{type}")
def get_all(td, type):
    ids = []
    with open('app/trds.json') as file:
        data = json.load(file)
    for i in data[td]:
        if i["type"] == type:
            ids.append(i["id"])
    return ids

@app.get("/id/{id}/{type}")
def get_all(id, type):
    with open('app/trds.json') as file:
        data = json.load(file)
    for i in data[type]:
        if i["id"] == int(id):
            q = i
    if type == 'dares':
        return q['task']
    else:
        return q['question']

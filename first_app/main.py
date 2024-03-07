from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")

ATLAS_URI = "mongodb+srv://zeeshanshaan391:5B1jJj0TFfdluKZo@cluster0.dcc0rmy.mongodb.net/"
DB_NAME = "shan"
conn = MongoClient("mongodb+srv://zeeshanshaan391:5B1jJj0TFfdluKZo@cluster0.dcc0rmy.mongodb.net")


    





@app.get("/item/{id}", response_class=HTMLResponse)
async def read_item(request: Request,id: str):
    return templates.TemplateResponse(
        request=request, name="item.html",context={"id":id}
    )
    
    
@app.get("/index", response_class=HTMLResponse)
async def read_docss(request: Request):
    docs = conn.shan.notes.find({})
    
    new_Docs=[]
    
    if docs:
        for doc in docs:
            new_Docs.append({
                "id": doc["_id"],
                "title": doc["note"],
                "desc":doc["desc"]
            })
        return templates.TemplateResponse(
            request=request, name="index.html",
            context={"new_Docs":new_Docs}
        )
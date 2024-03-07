from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request
from model.note import Note
from config.db import conn

note = APIRouter()

templates = Jinja2Templates(directory="templates")
note.mount("/static",StaticFiles(directory="static"),name="static")

@note.get("/index")
async def read_docss(request: Request):
    docs = conn.shan.notes.find({})
    
    new_Docs=[]
    
    if docs:
        for doc in docs:
            new_Docs.append({
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"]
            })
        return templates.TemplateResponse(
            request=request, name="index.html",
            context={"new_Docs":new_Docs}
        )

@note.post("/index")
async def add_notes(note:Note,request:Request):
    form = await request.form()
    conn.shan.notes.insert_one(dict(form))
    return {"success":True}
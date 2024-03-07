from pydantic import BaseModel


class Note(BaseModel):
    _id: int 
    title: str
    desc: str
    important: bool = False
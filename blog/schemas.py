from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id:int
    username:str
    password:str
    email:str

class UserDisplay(BaseModel):
    username:str
    email:str

    class Config():
        orm_mode = True

class Comment(BaseModel):
    comment_data:str
    id:str
    author:str
    date_of_comment: datetime =None
from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class Article(BaseModel):
    title:str
    content:str
    published:bool
    class config():
        orm_mode =True

class UserBase(BaseModel):
    id: Optional[int] = None    
    username:str
    password:str
    email:str

class UserDisplay(BaseModel):
    username:str
    email:str
    items:List[Article] = []
    class Config():
        orm_mode = True


class ArticleRequestModel(BaseModel):
    title : str
    id : int
    content : str
    author_name :str
    published : Optional[bool]

class User(BaseModel):
    id:int
    username:str
    class config():
        orm_mode=True

        
class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user: User
    class config():
        orm_mode =True

class Comment(BaseModel):
    comment_data:str
    id:str
    author:str
    date_of_comment: datetime =None
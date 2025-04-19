from pydantic import BaseModel
from datetime import datetime
class Blogs(BaseModel):
    title:str
    author_name:str
    published:bool
    published_date: datetime
    contents:str

class ShowBlog(Blogs):
    pass
    class Config():
        orm_mode=True


class User(BaseModel):
    __tablename__ ="users"
    name=Column


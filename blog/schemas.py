from pydantic import BaseModel

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
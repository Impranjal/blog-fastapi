from fastapi import FastAPI
from enum import Enum
import uvicorn
from pydantic import BaseModel
class ModelName(str,Enum):
    alexnet = 'alexnet'
    starnet='starnet'
    lenet = 'lenet'

class blog(BaseModel):
    title:str
    body_text:str
    author_name:str
    published:bool
    author:str

app = FastAPI()

@app.get('/')
def index():
    return {'data':{"name":"sarthak"}}

@app.get('/blog/')
def unpublished(limit,published):
    return {"data":{
        "name":"Scientific manual",
        "_id":"1",
        "author" : "niranjan jha",
        "published" : published,
        "limit": limit
    }}
@app.get('/about/{id}')
def about(id:int):
    return "My name is pranjal im working on a project to show connection for the social media users, you are user no is " +id 

@app.get('/model/{model_name}')
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"message":"Currently learning  deep learning ftw"}
    elif model_name is  ModelName.starnet:
        return {"model_name":model_name,"message":"Currently learning machine learing"}
    else:
        return {"model_name":model_name,"message":"the last model"}


@app.get('/blog')
def ind(limit,published:bool):
    if published:

        return {'data':f'{limit} blogs from the data'}
    else:
        return {'data':f'{limit} blogs are {published}'}


@app.post('/blogs')
def create_blogs(title,body):
    return {'title':title,'body':body}
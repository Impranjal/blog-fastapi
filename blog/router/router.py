from fastapi import FastAPI,APIRouter,Request,Query,Path,Cookie,Header,Form,Depends,HTTPException,Form
import uvicorn
from typing import Optional
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel,Field 
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import status
from database.database_user import create_user,get_user
from schemas import UserBase,UserDisplay,Comment

from validator.request_validation import RequestModel

router= APIRouter(prefix='/blog',tags=['blog'])
templates= Jinja2Templates(directory='template')

@router.post('/create_post')
async def submit_post(title:str=Form(),id:int=Form(),content:str=Form(),author_name:str=Form(),published:Optional[str]=Form()):
    if published:
        published_bool=True
    else:
        published_bool=False
    blog_post= RequestModel(
        title=title,
        id=id,
        content=content,
        author_name=author_name,
        published=published_bool
    )
    return {"msg":"The blog post has been created","data":blog_post.dict()}

@router.post('/comment_data/{id}')
async def comments_data(request:Comment):
    if request:
        return {
            "data":request
        }
    return HTTPException(status=401,details="Request couldn't be processed")



from fastapi import APIRouter
from fastapi import FastAPI,Request,Query,Path,Cookie,Header,Form,Depends,HTTPException
import uvicorn
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel,Field 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import status
from database.database_user import create_user,get_user
from schemas import UserBase,UserDisplay

from validator.request_validation import RequestModel

router= APIRouter(prefix='/blog',tags=['blog'])
templates= Jinja2Templates(directory='template')

@router.post('/blogs_data/{id}')   
async def create_blogs_data(rq:RequestModel):
    return {
        "data":rq,
        "message": "Created a entry"
    }




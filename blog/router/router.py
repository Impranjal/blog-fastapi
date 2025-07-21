from fastapi import APIRouter
from fastapi import FastAPI,Request,Query,Path,Cookie,Header,Form
from schema import Blogs,ShowBlog,User
from database import *
import uvicorn
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel,Field 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import status


router= APIRouter(prefix='/blog',tags=['blog'])
templates= Jinja2Templates(directory='template')


@router.on_event("startup")
def load_all_data():
    create_db_and_tables()

@router.get('/read_cookies')
async def read_cookies(ads:Annotated[int,Cookie()]):
    return {"ads":ads}

@router.get('/read_headers')
async def read_headers(x_token:Annotated[int,Header()]):
    return {"x token":x_token}

@router.post('/data',status_code=201)
def add_data(request:Blog,session:SessionDep):
    session.add(request)
    session.commit()
    session.refresh(request)
    return request


@router.get('/blogs_data/{id}', response_class=HTMLResponse)
def fetching_all_data(id: int, request: Request, session: SessionDep):
    try:
        blog = session.exec(select(Blog).where(Blog.id == id)).first()
        if not blog:
            raise Exception()
    except Exception:
        raise HTTPException(status_code=404, detail="Blogs detail was not extracted")
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "blog": blog,
            "message": "Hello from FastAPI!",
            "username": "Pranjal"
        
    )

# @router.get('/blogs_data/{id}', response_class=HTMLResponse)
# def fetching_data_by_id(id: int, request: Request, session: SessionDep):
#     try:
#         blog = session.exec(select(Blog).where(Blog.id == id)).first()
#         if not blog:
#             raise Exception()
#     except Exception:
#         raise HTTPException(status_code=404, detail="Blogs detail was not extracted")
#     return templates.TemplateResponse(
#         "base.html",
#         {
#             "request": request,
#             "blog": blog,
#             "message": "Hello from FastAPI!",
#             "username": "Pranjal"
#         }
#     )


@router.post('/blog')
def create(blogs:Blogs):
    return blogs

@router.delete('/blog_del/{id}',status_code=204 )
def destroy(id:int,session:SessionDep):
    raw_id = session.get(Blog,id)
    if not raw_id:
        raise HTTPException(status_code=404,detail="Blog record not found")
    session.delete(raw_id)
    session.commit()
    return {'ok':True}



@router.post('/users')
def create_user(request:User):
    return request

@router.get('/users/{users_catalog}')
def show_user_catalog(users_catalog:str):
    if users_catalog:
        raise HTTPException(status_code=404,detail="User catalog not available")
    return users_catalog

@router.get('/blog_val')
async def blog_val(skip:int =0,limit:int =0):
    return {"skip":skip,"limit":limit}
# ---- templating -----


@router.get('/contacts/{owner}')
async def blog_contact(owner:Annotated[int,Path(title="The path to contacts list")]):
    return owner


class Blogoutput(BaseModel):
    id:str
    summary:Annotated[str,Query(max_length=50)]
    page_no:int

@router.get('/blogoutput',response_model=Blogoutput)
async def get_out(r:Blogoutput):
    return r
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


@app.on_event("startup")
def load_all_data():
    create_db_and_tables()

@app.get('/read_cookies')
async def read_cookies(ads:Annotated[int,Cookie()]):
    return {"ads":ads}

@app.get('/read_headers')
async def read_headers(x_token:Annotated[int,Header()]):
    return {"x token":x_token}

@app.post('/data',status_code=201)
def add_data(request:Blog,session:SessionDep):
    session.add(request)
    session.commit()
    session.refresh(request)
    return request

@app.get('/blogs_data/{id}')
def fetching_all_data(id:int,session:SessionDep,response_model=ShowBlog):
    try:
        blogs = session.exec(select(Blog).where(Blog.id==id))
    except Exception:
        raise HTTPException(status_code=404,detail="Blogs detail was not extracted")
    return blogs.first()

@app.post('/blog')
def create(blogs:Blogs):
    return blogs

@app.delete('/blog_del/{id}',status_code=204 )
def destroy(id:int,session:SessionDep):
    raw_id = session.get(Blog,id)
    if not raw_id:
        raise HTTPException(status_code=404,detail="Blog record not found")
    session.delete(raw_id)
    session.commit()
    return {'ok':True}



@app.post('/users')
def create_user(request:User):
    return request

@app.get('/users/{users_catalog}')
def show_user_catalog(users_catalog:str):
    if users_catalog:
        raise HTTPException(status_code=404,detail="User catalog not available")
    return users_catalog

@app.get('/blog_val')
async def blog_val(skip:int =0,limit:int =0):
    return {"skip":skip,"limit":limit}
# ---- templating -----


@app.get('/contacts/{owner}')
async def blog_contact(owner:Annotated[int,Path(title="The path to contacts list")]):
    return owner


class Blogoutput(BaseModel):
    id:str
    summary:Annotated[str,Query(max_length=50)]
    page_no:int

@app.get('/blogoutput',response_model=Blogoutput)
async def get_out(r:Blogoutput):
    return r
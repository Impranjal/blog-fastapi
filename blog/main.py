from fastapi import FastAPI,Request
from schema import Blogs,ShowBlog
from database import *
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="blog/static"), name="static")


templates = Jinja2Templates(directory="blog/template")

@app.on_event("startup")
def load_all_data():
    create_db_and_tables()

@app.post('/data',status_code=201)
def add_data(request:Blog,session:SessionDep):
    session.add(request)
    session.commit()
    session.refresh(request)
    return request

@app.get('/blogs_data/{id}')
def fetching_all_data(id:int,session:SessionDep,response_model=ShowBlog):
    blogs = session.exec(select(Blog).where(Blog.id==id))
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

@app.get('/fetch_blogs',response_class=HTMLResponse)
async def get_records(res:Request,id:str):
    return templates.TemplateResponse(
        request=res, name="item.html", context={"id": id}
    )
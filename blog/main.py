from fastapi import FastAPI
from schema import Blogs
from database import *
import uvicorn

app = FastAPI()
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
def fetching_all_data(id,session:SessionDep):
    blogs = session.exec(select(Blog)).filter(Blog.id==id)
    return blogs

@app.post('/blog')
def create(blogs:Blogs):
    return blogs
if __name__ == "__main__":
    uvicorn.run('main:app',host='127.0.0.1',port=5051,reload=True)
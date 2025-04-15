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
def fetching_all_data(id:int,session:SessionDep):
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

if __name__ == "__main__":
    uvicorn.run('main:app',host='127.0.0.1',port=5051,reload=True)
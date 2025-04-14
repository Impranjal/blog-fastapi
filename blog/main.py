from fastapi import FastAPI
from schema import Blogs
app = FastAPI()

@app.post('/blog')
def create(blogs:Blogs):
    return f"My name is pranjal singh this is my first blog title {blogs.title} having contents as {blogs.contents} and is getting published on {blogs.published_date}"
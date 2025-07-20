from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import router

app = FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
app.include_router(router.router)

@app.get('/Welcome')
def hello():
    return {"message":"Hello world"}
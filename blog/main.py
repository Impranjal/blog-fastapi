from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import router
from router import user
from database.database import engine
from database import models
app: FastAPI =FastAPI(title="GenAI Blog API",description="API powered by GenAI",version="1.0.0")

app.mount('/static',StaticFiles(directory='static'),name='static')
app.include_router(router.router)
app.include_router(user.router)


@app.get('/Welcome')
def hello():
    return {"message":"Hello world"}
    

models.Base.metadata.create_all(bind=engine)
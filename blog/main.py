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
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/static',StaticFiles(directory='static'),name='static')
app.include_router(router.router)
app.include_router(user.router)
templates= Jinja2Templates(directory='template')


@app.get('/')
def hello(request:Request):
    return templates.TemplateResponse("landing.html", {"request": request})

    

models.Base.metadata.create_all(bind=engine)
from fastapi import FastAPI,Depends
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import router_article
from router import user
from typing import Annotated
from database.database import engine
from database import models
from exception import Storyexceptions
from fastapi.security import OAuth2PasswordBearer
app: FastAPI =FastAPI(title="GenAI Blog API",description="API powered by GenAI",version="1.0.0")
from fastapi.middleware.cors import CORSMiddleware

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/static',StaticFiles(directory='static'),name='static')
app.include_router(router_article.router)
app.include_router(user.router)
templates= Jinja2Templates(directory='template')

@app.get('/')
def hello(request:Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/items")
async def get_new_items(token:Annotated[str,Depends(oauth2_scheme)]):
    return {"token":token}

@app.exception_handler(Storyexceptions)
def exception_handler(request:Request,exp:Storyexceptions):
    return JSONResponse(
        status_code=418,
        content= {"detail":exp.name}
    )

    

models.Base.metadata.create_all(bind=engine)
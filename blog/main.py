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
app: FastAPI =FastAPI(title="GenAI Blog API",description="API powered by GenAI",version="1.0.0")
from fastapi.middleware.cors import CORSMiddleware
from schemas import User_auth
from auth import auth


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/static',StaticFiles(directory='static'),name='static')
app.include_router(router_article.router)
app.include_router(user.router)
app.include_router(auth.router)
templates= Jinja2Templates(directory='template')


@app.get('/')
def hello(request: Request):
    username = request.cookies.get("access_token")
    from jose import jwt, JWTError
    SECRET_KEY = '2dc62fb76d115486b0dc5bd94337edfd'
    ALGORITHM = 'HS256'
    user_name = None
    if username:
        try:
            payload = jwt.decode(username, SECRET_KEY, algorithms=[ALGORITHM])
            user_name = payload.get("sub")
        except JWTError:
            user_name = None
    return templates.TemplateResponse("landing.html", {"request": request, "username": user_name})



@app.exception_handler(Storyexceptions)
def exception_handler(request:Request,exp:Storyexceptions):
    return JSONResponse(
        status_code=418,
        content= {"detail":exp.name}
    )

    

models.Base.metadata.create_all(bind=engine)
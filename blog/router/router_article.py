from fastapi import FastAPI,APIRouter,Request,Query,Path,Cookie,Header,Form,Depends,HTTPException,Form
from sqlalchemy.orm import Session
import uvicorn
from typing import Optional
from datetime import datetime
from typing import Annotated
from pydantic import BaseModel,Field 
from fastapi.responses import Response,HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import status
from database.database import get_db
from database.database_article import create_article,get_all_article,get_article_by_id
from schemas import UserBase,UserDisplay,Comment,ArticleRequestModel
from validator.request_validation import RequestModel

router= APIRouter(prefix='/blog',tags=['blog'])
templates= Jinja2Templates(directory='template')

@router.get('/create_post', response_class=HTMLResponse)
async def show_create_post_form(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.post('/create_post')
async def submit_post(
    request: Request,
    title: str = Form(),
    id: int = Form(),
    content: str = Form(),
    author_name: str = Form(),
    published: Optional[str] = Form(),
    author_id:int=Form(),
    db:Session=Depends(get_db)
):
    if published:
        published_bool=True
    else:
        published_bool=False
    blog_post= ArticleRequestModel(
        title=title,
        id=id,
        content=content,
        author_name=author_name,
        published=published_bool,
        author_id=author_id
    )
    try:
        blog_res= create_article(db,blog_post)
    except Exception as e:
        raise HTTPException(status_code=404,detail=f"The blog entry was not create caught a exception {e}")
    
    return templates.TemplateResponse(
        "base.html",
        {"request": request, "message": "Blog created successfully!"}
    )

@router.post('/comment_data/{id}')
async def comments_data(request:Comment):
    if request:
        return {
            "data":request
        }
    return HTTPException(status=401,details="Request couldn't be processed")






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
from schemas import UserBase,UserDisplay,Comment,ArticleRequestModel,User
from validator.request_validation import RequestModel
from auth.oauth2 import oauth2_scheme,get_current_user

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
    author_id: int = Form(),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if published:
        published_bool = True
    else:
        published_bool = False
    blog_post = ArticleRequestModel(
        title=title,
        id=id,
        content=content,
        author_name=author_name,
        published=published_bool,
        author_id=author_id
    )
    try:
        blog_res = create_article(db, blog_post)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"The blog entry was not create caught a exception {e}")
    return templates.TemplateResponse(
        "base.html",
        {"request": request, "message": "Blog created successfully!", "current_user": current_user}
    )

@router.post('/comment_data/{id}')
async def comments_data(request: Comment, current_user: User = Depends(get_current_user)):
    if request:
        return {
            "data": request,
            "current_user": current_user
        }
    return HTTPException(status_code=401, detail="Request couldn't be processed")

@router.get('/get_all_blog')
async def get_all_the_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return {
        "data": get_all_article(db),
        "current_user": current_user
    }

@router.get('/get_all_blog/{id}')
async def get_all_the_blogs_id(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return {
        "data": get_article_by_id(db, id),
        "current_user": current_user
    }

@router.get('/blog', response_class=HTMLResponse)
async def show_all_blogs(request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blogs = get_all_article(db)
    return templates.TemplateResponse("blog.html", {"request": request, "blogs": blogs, "current_user": current_user})
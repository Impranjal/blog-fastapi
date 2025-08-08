from fastapi import APIRouter,Depends,HTTPException,Request
from schemas import UserBase,UserDisplay
from database.database import get_db
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from database.database_user import *
router = APIRouter(
    prefix='/user',
    tags=['user']
)
templates= Jinja2Templates(directory='template')
#create user
@router.get("/",response_class=HTMLResponse,status_code=201)
async def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})
                                      
@router.post('/',response_model=UserDisplay, status_code=201)
async def create_user_data(request:UserBase,db:Session=Depends(get_db)):
    return create_user(db,request)

@router.get('/',response_model=list[UserDisplay])
async def get_user_route(db:Session=Depends(get_db)): 
    return get_user(db)

@router.get('/{id}',response_model=UserDisplay,status_code=201)
async def get_user_based_on_id(id :int ,db:Session=Depends(get_db)):
    return get_user_id(id,db)

@router.post('/update/{id}')
async def update_user_data(id:int,request:UserBase,db:Session=Depends(get_db)):
    return update_user(id,request,db)

@router.delete('/delete/{id}',status_code=200)
async def delete_user_data(id:int,db:Session=Depends(get_db)):
    if delete_user(id,db):
        return {"User id {id} data deleted successfully"}
    return HTTPException(status_code=404,detail="Delete couldn't be performed")
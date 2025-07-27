from fastapi import APIRouter,Depends
from schemas import UserBase,UserDisplay
from database.database import get_db
from sqlalchemy.orm import Session
from database.database_user import *
router = APIRouter(
    prefix='/user',
    tags=['user']
)

#create user
@router.post('/',response_model=UserDisplay, status_code=201)
async def create_user_data(request:UserBase,db:Session=Depends(get_db)):
    return create_user(db,request)

@router.get('/',response_model=list[UserDisplay])
async def get_user_route(db:Session=Depends(get_db)): 
    return get_user(db)

@router.get('/{id}',response_model=UserDisplay,status_code=201)
async def get_user_based_on_id(id :int ,db:Session=Depends(get_db)):
    return get_user_id(id,db)

@router.post('/update/{id}',response_model=UserDisplay)
async def update_user_data(id:int,request:UserBase,db:Session=Depends(get_db)):
    return update_user(id,request,db)
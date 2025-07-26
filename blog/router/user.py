from fastapi import APIRouter,Depends
from schemas import UserBase,UserDisplay
from database.database import get_db
from sqlalchemy.orm import Session
from database.database_user import create_user
router = APIRouter(
    prefix='/user',
    tags=['user']
)

#create user
@router.post('/',response_model=UserDisplay, status_code=201)
async def create_user_route(request:UserBase,db:Session=Depends(get_db)):
    return create_user(db,request)
from sqlalchemy.orm.session import Session
from schemas import UserBase
from database.models import UserData
from database.hash import Hash
def create_user(db: Session, request: UserBase):
    new_user = UserData(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session):
    return db.query(UserData).all()

def get_user_id(id: int ,db:Session):
    return db.query(UserData).filter(UserData.id==id).first()

def update_user(id:int,request:UserBase,db:Session):
    user =db.query(UserData).filter(UserData.id==id)
    user.update({
        UserData.username: request.username,
        UserData.email: request.email,
        UserData.password:Hash.bcrypt(request.password)

    })
    db.commit()
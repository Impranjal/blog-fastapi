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
         
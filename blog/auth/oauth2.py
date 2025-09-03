from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from fastapi import APIRouter,Depends,HTTPException,Form,status
from sqlalchemy.orm import Session
from database.database import get_db
from jose.exceptions import JWTError
from database.database_user import get_user_username
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '2dc62fb76d115486b0dc5bd94337edfd'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token:str=Depends(oauth2_scheme),db:str=Depends(get_db)):
    credential_exeption= HTTPException(status_code=401)
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username :str = payload.get("sub")
        if username is None:
            raise credential_exeption
    except JWTError:
       raise credential_exeption
    user = get_user_username(username,db)
    if user is None:
       raise credential_exeption
    return user
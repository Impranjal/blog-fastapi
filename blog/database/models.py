from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String
from database.database import Base

class UserData(Base):
    __tablename__ ="Users"
    id = Column(Integer,primary_key=True)
    email =Column(String)
    username = Column(String)
    password = Column(String)
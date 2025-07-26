
from database.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String

class UserData(Base):
    __tablename__ ="Users"
    id = Column(Integer,primary_key=True,index=True)
    email =Column(String)
    username = Column(String)
    password = Column(String)
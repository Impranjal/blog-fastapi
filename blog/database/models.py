
from database.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy.sql.schema import ForeignKey

class UserData(Base):
    __tablename__ ="users"
    id = Column(Integer,primary_key=True,index=True)
    email =Column(String)
    username = Column(String)
    password = Column(String)
    items = relationship("ArticleData",back_populates="user")

class ArticleData(Base):
    __tablename__ = "articles"
    id = Column(Integer,primary_key=True,index=True)
    content = Column(String)
    title = Column(String)
    author_name=Column(String)
    published= Column(Boolean)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("UserData",back_populates='items')
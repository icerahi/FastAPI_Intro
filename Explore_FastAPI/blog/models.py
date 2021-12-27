from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column,Integer,String

class Blog(Base):
    __tablename__='blog'
    id=Column(Integer, primary_key=True,index=True)
    title = Column(String) 
    body = Column(String)
    user_id = Column(Integer,ForeignKey('user.id'))
    creator = relationship('User',back_populates='blogs')
    
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String,unique=True)
    password=Column(String)
    blogs = relationship('Blog',back_populates='creator')
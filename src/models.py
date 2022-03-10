import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=True)
    content = Column(String, nullable=True)
    author = Column(Integer, ForeignKey('users.id'))

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
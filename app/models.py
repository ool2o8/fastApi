from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, VARCHAR, Text
from sqlalchemy.orm import relationship
import datetime
from .db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    foods = relationship("Food", back_populates="owner")
    posts =relationship("Post", back_populates="owner")

class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    img_url=Column(String, index=True, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_dt=Column(DateTime, default=datetime.datetime.now())

    owner = relationship("User", back_populates="foods")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    img_url=Column(String, index=True, nullable=True)
    description = Column(String, index=True)
    created_dt=Column(DateTime, default=datetime.datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

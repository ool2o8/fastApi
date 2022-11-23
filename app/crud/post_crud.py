from sqlalchemy.orm import Session
from ..utils.auth_utils import get_current_user
from fastapi import Request
from ..schemas import blog_schemas

from .. import models

def create_post(request: Request, db: Session, post: blog_schemas.PostBase):
    auth= get_current_user(db=db, request=request)
    db_post = models.Post(owner=auth, owner_id=auth.id, title=post.title, description=post.description)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def list_post(request: Request, db:Session):
    db_post=db.query(models.Post).all()
    return db_post

def retrieve_post(request: Request, db:Session, post_id: int):
    db_post=db.query(models.Post).filter(models.Post.id==post_id).first()
    return db_post

def update_img(request: Request, db: Session,post_id: int, img_url: str):
    auth= get_current_user(db=db, request=request)
    
    db_food = db.query(models.Post).filter(models.Post.id==post_id)
    db_food.update({models.Post.img_url:img_url})
    db.commit()
    
    return {'response': "upload complete."}
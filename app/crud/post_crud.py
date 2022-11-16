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

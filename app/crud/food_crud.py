from sqlalchemy.orm import Session
from ..utils.auth_utils import get_current_user
from fastapi import Request
from ..schemas import food_schemas
from .. import models

def create_food(request: Request, db: Session, title: str, img_url: str):
    auth= get_current_user(db=db, request=request)
    db_food = models.Food(owner=auth, owner_id=auth.id, title=title, img_url=img_url)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food
from sqlalchemy.orm import Session
from ..utils.auth_utils import get_current_user
from fastapi import Request
from ..schemas import food_schemas

from .. import models

def create_food(request: Request, db: Session, food: food_schemas.foodBase):
    auth= get_current_user(db=db, request=request)
    db_food = models.Food(owner=auth, owner_id=auth.id, title=food.title, description=food.description)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def list_food(request: Request, db:Session):
    db_food=db.query(models.Food).all()
    return db_food

def retrieve_food(request: Request, db:Session, food_id: int):
    db_food=db.query(models.Food).filter(models.Food.id==food_id).first()
    return db_food

def update_img(request: Request, db: Session,food_id: int, img_url: str):
    auth= get_current_user(db=db, request=request)
    
    db_food = db.query(models.Food).filter(models.Food.id==food_id)
    db_food.update({models.Food.img_url:img_url})
    db.commit()
    
    return {'response': "upload complete."}

def get_myfood(request: Request, db: Session):
    auth= get_current_user(db=db, request=request)
    db_food=db.query(models.Food).filter(models.Food.owner_id==auth.id).all()
    print(auth.id, db_food)
    return db_food
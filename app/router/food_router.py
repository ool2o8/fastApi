from sqlalchemy.orm import Session
from fastapi import Depends, Request, UploadFile, File
from ..crud import food_crud
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db, IMG_URL
from typing import List
import os
from ..schemas.food_schemas import FoodBase

from fastapi import APIRouter

router = APIRouter()
# @router.get("/food")
# def retrieve_post(reqeust: Request, db: Session = Depends(get_db)):
#     return post_crud.list_post(request=reqeust,db=db)



   
    

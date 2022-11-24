
from sqlalchemy.orm import Session
from fastapi import Depends, Request, UploadFile, Response
from fastapi.responses import FileResponse
from ..crud import food_crud
from ..schemas import food_schemas
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db

from ..crud import food_crud
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db, IMG_URL
import os
from fastapi import APIRouter
from.. import models

router = APIRouter()
@router.get("")
def retrieve_food(reqeust: Request, db: Session = Depends(get_db)):
    return food_crud.list_food(request=reqeust,db=db)

@router.post("")
def creat_food(request: Request, food: food_schemas.foodBase, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    return food_crud.create_food(request=request, db=db, food=food)

@router.get("/me")
def view_myfood(request: Request, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    return food_crud.get_myfood(request=request, db=db)

@router.get("/{food_id}")
def retrieve_food(food_id: int, reqeust: Request, db: Session = Depends(get_db)):
    return food_crud.retrieve_food(request=reqeust,db=db, food_id=food_id)

@router.get("/{food_id}/img")
async def upload_img(food_id: int, request: Request, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    db_food=db.query(models.Food).filter(models.Food.id==food_id)
    return FileResponse(os.path.join(IMG_URL, db_food[0].img_url))

@router.post("/img")
async def upload_img(request: Request, food_id: int, file: UploadFile, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
   
    contents = await file.read()
    with open(os.path.join(IMG_URL, file.filename), "wb") as fp:
        fp.write(contents)
    return food_crud.update_img(request=request, db=db, food_id=food_id, img_url=file.filename)
    

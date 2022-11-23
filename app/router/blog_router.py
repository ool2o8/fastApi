
from sqlalchemy.orm import Session
from fastapi import Depends, Request, UploadFile, Response
from fastapi.responses import FileResponse
from ..crud import post_crud
from ..schemas import blog_schemas
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db

from ..crud import post_crud
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db, IMG_URL
import os
from fastapi import APIRouter
from.. import models

router = APIRouter()
@router.get("/post")
def retrieve_post(reqeust: Request, db: Session = Depends(get_db)):
    return post_crud.list_post(request=reqeust,db=db)

@router.post("/post")
def creat_post(request: Request, post: blog_schemas.PostBase, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    return post_crud.create_post(request=request, db=db, post=post)

@router.get("/post/{post_id}")
def retrieve_post(post_id: int, reqeust: Request, db: Session = Depends(get_db)):
    return post_crud.retrieve_post(request=reqeust,db=db, post_id=post_id)

@router.get("/post/{post_id}/img")
async def upload_img(post_id: int, request: Request, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    db_post=db.query(models.Post).filter(models.Post.id==post_id)
    return FileResponse(os.path.join(IMG_URL, db_post[0].img_url))

@router.post("/img")
async def upload_img(request: Request, post_id: int, file: UploadFile, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
   
    contents = await file.read()
    with open(os.path.join(IMG_URL, file.filename), "wb") as fp:
        fp.write(contents)
    return post_crud.update_img(request=request, db=db, post_id=post_id, img_url=file.filename)
    

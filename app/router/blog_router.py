
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Request
from ..crud import post_crud
from ..schemas import blog_schemas
from ..utils.auth_utils import AuthProvider
from ..db.database import get_db


from fastapi import APIRouter

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



from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi import Cookie, Request
from ..crud import post_crud
from ..models import Post
from ..schemas import blog_schemas
from ..utils.auth_utils import signJWT,get_current_user,AuthProvider, get_user_by_username, get_users, get_user_by_email, get_db


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



from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi import Cookie, Request
from ..crud import auth_crud

from ..schemas import auth_schemas
from ..utils.auth_utils import signJWT,get_current_user,AuthProvider, get_user_by_username, get_users, get_user_by_email, get_db


from fastapi import APIRouter

router = APIRouter()


@router.post("/token")
async def create_token(response:Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_dict = get_user_by_username(db,form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = get_user_by_username(db, user_dict.username)
    if not auth_crud.get_verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token=signJWT(form_data.username)
    response.set_cookie(key="access_token", value=token)
    return (token, {"token_type": "bearer"})


@router.post('/login')
def login(response: Response, data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    user = get_user_by_username(db, username=username)

    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif not auth_crud.get_verify_password(password, user.hashed_password):
        raise InvalidCredentialsException
    token = RedirectResponse(url='/auth/token')
    
    return token


@router.post("/users/")
def create_user(user: auth_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth_crud.create_user(db=db, user=user)


@router.get("/users/", response_model=list[auth_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/me/", response_model=auth_schemas.User)
def read_users(request: Request, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    
    token = RedirectResponse(url='/auth/token')
    return get_current_user(db, request)
    

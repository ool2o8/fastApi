from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import jwt
import time
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from fastapi import Cookie

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
SECRET=b'e406f87ee7323ab75daaecb3cef40076beb38701428b0134'
ALGORITHM="HS256"

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 6000
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return token


from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token[2:-1], SECRET, ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
        
    except:
        return {}


class AuthProvider:
    async def __call__(self, request: Request):
        authorization: str=request.cookies
        if not jwt.decode(authorization["access_token"][2:-1], SECRET, ALGORITHM):
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        return True


@app.post("/token")
async def create_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_dict = crud.get_login_data(db,form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = crud.get_login_data(db, user_dict.username)
    if not crud.get_verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return signJWT(form_data.username)


def get_current_user(request:Request):
    authorization: str=request.cookies
    user=jwt.decode(authorization["access_token"][2:-1], SECRET, ALGORITHM)
    return user


@app.post('/login')
def login(response: Response, data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    user = crud.get_login_data(db, username=username)

    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif not crud.get_verify_password(password, user.hashed_password):
        raise InvalidCredentialsException
    access_token=signJWT(username)
    print(access_token)
    response.set_cookie(key="access_token", value=access_token)
    return (access_token, {"token_type": "bearer"})


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/me/", response_model=schemas.User)
def read_users(request: Request, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
    return crud.get_user(db, get_current_user(request)['user_id'])
    

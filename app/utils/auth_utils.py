from typing import Union
import jwt, datetime,time
from sqlalchemy.orm import Session
from fastapi import Request, Depends, HTTPException
from .. import models
from jose import jwt
from app.db.database import SessionLocal
from .. import models
import os
import json
from pathlib import Path
from ..db.database import get_db

BASE_DIR=Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secret.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())


SECRET_KEY =secrets["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 6000
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
        
    except:
        return {}


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user(username: str, db: Session):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


class AuthProvider:
    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        authorization: str=request.cookies
        token=decodeJWT(authorization["access_token"])
        if not token:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if not get_user(token["user_id"], db):
            raise HTTPException(status_code=403, detail="Not auth")
        return True


async def get_current_active_user(current_user: models.User = Depends(AuthProvider)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def token_response(token: str):
    return {
        "access_token": token
    }


def get_current_user( db: Session,request:Request):
    authorization: str=request.cookies
    user=jwt.decode(authorization["access_token"], SECRET_KEY, ALGORITHM)
    return get_user(user['user_id'], db)


def create_access_token(data: dict, expires_delta: Union[datetime.timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt





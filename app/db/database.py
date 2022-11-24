from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os.path, json
from pathlib import Path
from .. import models

BASE_DIR=Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secret.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

DB_URL = f"mysql+pymysql://{secrets['DB']['user']}:{secrets['DB']['password']}@{secrets['DB']['host']}:{secrets['DB']['port']}/{secrets['DB']['database']}?charset=utf8"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
IMG_URL = os.path.join(BASE_DIR, 'static/')
engine = create_engine(
    DB_URL, encoding = 'utf-8'
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_metadata():
    return models.Base.metadata
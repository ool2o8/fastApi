from fastapi import Depends, FastAPI
from .. import models
from ..db.database import SessionLocal, engine
from ..router import auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth")


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

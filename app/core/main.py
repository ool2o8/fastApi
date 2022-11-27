from fastapi import Depends, FastAPI

from ..router import food_router
from .. import models
from ..db.database import SessionLocal, engine
from ..router import auth_router, food_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

app.include_router(auth_router.router, prefix="/auth")
app.include_router(food_router.router,prefix="/food")
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




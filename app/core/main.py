from fastapi import Depends, FastAPI
from .. import models
from ..db.database import SessionLocal, engine
from ..router import auth_router, blog_router, food_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(auth_router.router, prefix="/auth")
app.include_router(blog_router.router,prefix="/blog")
app.include_router(food_router.router, prefix="/food")
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

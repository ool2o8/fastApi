from fastapi import UploadFile

from pydantic import BaseModel
from fastapi import File
class FoodBase(BaseModel):
    title: str

class FoodImgBase(FoodBase):
    img: UploadFile

class Food(FoodBase):
    id: int
    title: str
    img: str
    class Config:
        orm_mode = True
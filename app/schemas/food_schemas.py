from fastapi import UploadFile

from pydantic import BaseModel

class FoodBase(BaseModel):
    title: str


class Food(FoodBase):
    id: int
    title: str
    img: str
    class Config:
        orm_mode = True
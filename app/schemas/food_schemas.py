from pydantic import BaseModel
class foodBase(BaseModel):
    title: str
    description: str


class food(foodBase):
    id: int
    class config:
        orm_mode=True


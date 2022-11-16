from pydantic import BaseModel
class PostBase(BaseModel):
    title: str
    description: str


class Post(PostBase):
    id: int
    class config:
        orm_mode=True


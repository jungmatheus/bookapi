
from pydantic import BaseModel
from datetime import datetime


class BookIn(BaseModel):
    title: str 
    category_id: int

    class Config:
        orm_mode=True


class BookOut(BaseModel):
    title: str
    category_id: int
    created_at: datetime
    id: int

    class Config:
        orm_mode=True
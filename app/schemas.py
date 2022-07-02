
from pydantic import BaseModel, EmailStr
from datetime import datetime


class BookIn(BaseModel):
    title: str 
    category_id: int

    class Config:
        orm_mode=True



class CategoryOut(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode=True



class BookOut(BaseModel):
    title: str
    category_id: int
    created_at: datetime
    id: int
    category: CategoryOut

    class Config:
        orm_mode=True

class UserIn(BaseModel):

    email: EmailStr
    password: str
    username: str
    


    class Config:
        orm_mode=True
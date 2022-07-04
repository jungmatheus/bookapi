
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

class UserOut(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode=True


class BookOut(BaseModel):
    title: str
    created_at: datetime
    id: int
    category: CategoryOut
    user: UserOut


    class Config:
        orm_mode=True

class UserIn(BaseModel):

    email: EmailStr
    password: str
    username: str

    class Config:
        orm_mode=True


class TokenData(BaseModel):

    id: int
    username: str
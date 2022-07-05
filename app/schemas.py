
from pydantic import BaseModel, EmailStr
from datetime import datetime


class BookIn(BaseModel):
    title: str 
    category_id: int
    author: str | None = None
    number_of_pages: int | None = None

   


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

class BookBase(BaseModel):
    title: str
    author: str | None = None
    number_of_pages: str | None = None
    created_at: datetime
    id: int
    category: CategoryOut
    user: UserOut
    

    class Config:
        orm_mode=True



class BookOut(BaseModel):
    Book: BookBase
    votes: int
    
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


class VoteIn(BaseModel):
    book_id: int
    vote_dir: bool

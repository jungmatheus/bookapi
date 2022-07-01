from fastapi import APIRouter




router = APIRouter(prefix='/books', tags=['Books'])



@router.get('/')
def get_books():
    return {"message": "books"}
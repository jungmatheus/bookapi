from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, database_models, oauth2
from typing import List



router = APIRouter(prefix='/books', tags=['Books'])



@router.get('/', response_model=List[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    books = db.query(database_models.Book).all()
    return books


@router.get('/{id}', response_model=schemas.BookOut)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(database_models.Book).filter(database_models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Could not find the book you are looking for')
    return book



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BookOut)
def create_book(book: schemas.BookIn, db: Session = Depends(get_db), user: oauth2.get_current_user = Depends()):
    print(user.id, user.username)
    new_book = database_models.Book(title=book.title, category_id=book.category_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put('/{id}', response_model=schemas.BookOut)
def update_book(id: int, book: schemas.BookIn, db: Session = Depends(get_db)):
    query = db.query(database_models.Book).filter(database_models.Book.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The book you want to update does not exist')
    query.update(book.dict(), synchronize_session=False)
    db.commit()
    return query.first()


@router.delete('/{id}')
def delete_book(id: int, db: Session = Depends(get_db)):
    query = db.query(database_models.Book).filter(database_models.Book.id == id)

    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The book you are trying to delete does not exist')
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
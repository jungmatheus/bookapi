from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, database_models, oauth2
from typing import List
from sqlalchemy import func



router = APIRouter(prefix='/books', tags=['Books'])


@router.get('/', response_model=List[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    books = db.query(database_models.Book, func.count(database_models.Vote.book_id).label('votes')).join(database_models.Vote, 
    database_models.Book.id == database_models.Vote.book_id, isouter=True).group_by(database_models.Book.id).all()
    return books


@router.get('/{id}', response_model=schemas.BookOut)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(database_models.Book, func.count(database_models.Vote.book_id).label('votes')).join(database_models.Vote, 
    database_models.Book.id == database_models.Vote.book_id, isouter=True).group_by(database_models.Book.id).filter(database_models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Could not find the book you are looking for')
    return book



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BookBase)
def create_book(book: schemas.BookIn, db: Session = Depends(get_db), user: oauth2.get_current_user = Depends()):
    new_book = database_models.Book(user_id=user.id, **book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put('/{id}', response_model=schemas.BookBase)
def update_book(id: int, book: schemas.BookIn, db: Session = Depends(get_db), user: oauth2.get_current_user = Depends()):
    query = db.query(database_models.Book).filter(database_models.Book.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no book with that id')
    if query.first().user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not the owner of the book')    
    query.update(book.dict(), synchronize_session=False)
    db.commit()
    return query.first()


@router.delete('/{id}')
def delete_book(id: int, db: Session = Depends(get_db), user: oauth2.get_current_user = Depends()):
    query = db.query(database_models.Book).filter(database_models.Book.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no book with that id')
    if query.first().user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not the owner of the book') 
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
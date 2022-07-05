from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import oauth2, schemas, database_models

router = APIRouter(prefix='/vote', tags=['Vote'])


@router.post('/')
def vote(vote_info: schemas.VoteIn,db: Session = Depends(get_db), user: oauth2.get_current_user = Depends()):

    book = db.query(database_models.Book).filter(vote_info.book_id == database_models.Book.id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is no book with an id of {vote_info.book_id}')


    vote_row = db.query(database_models.Vote).filter(vote_info.book_id == database_models.Vote.book_id, user.id == database_models.Vote.user_id)
    if vote_row.first():
        if vote_info.vote_dir is False:
            vote_row.delete(synchronize_session=False)
            db.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='You have already voted on this book')
    if not vote_row.first():
        if not vote_info.vote_dir:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='You already have no vote on this book')
        else:
            new_vote = database_models.Vote(user_id=user.id, book_id=vote_info.book_id)
            db.add(new_vote)
            db.commit()
            return Response(status_code=status.HTTP_201_CREATED)


        





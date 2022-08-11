from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from .. import database_models, schemas, utils
from ..database import get_db


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):

    hashed_pwd = utils.hash_password(user.password)
    user.password = hashed_pwd
    new_user = database_models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(database_models.User).filter(database_models.User.id == id).first()
    return user

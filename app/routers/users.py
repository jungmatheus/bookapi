from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from .. import database_models, schemas, utils
from ..database import get_db



router = APIRouter(prefix='/users', tags=['Users'])



@router.post('/')
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):

    hashed_pwd = utils.hash_password(user.password)
    user.password = hashed_pwd
    new_user = database_models.User(**user.dict())
    db.add(new_user)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED)


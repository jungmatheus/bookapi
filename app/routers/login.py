from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from .. import database_models, utils, oauth2

router = APIRouter(prefix='/login', tags=['Login'])


@router.post('/')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    credentials =  db.query(database_models.User).filter(database_models.User.email == form_data.username).first()
    if not credentials or not utils.verify_password(form_data.password, credentials.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid email or password')
    token = oauth2.create_access_token({"user_id": credentials.id, "username": credentials.username})
    return {"access_token": token, "token_type": "bearer"}
    


   



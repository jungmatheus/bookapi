from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas
from .config import settings as s


oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = s.SECRET_KEY
ALGORITHM = s.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = s.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    exp  = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": exp})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_acess_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get('user_id')
        username: str = payload.get('username')
    except JWTError:
        raise credentials_exception 
    
    token_data = schemas.TokenPayload(user_id=id, username=username)
    return token_data

def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'bearer'})
    return verify_acess_token(token, credentials_exception)



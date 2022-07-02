from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt


oauth2_schema = OAuth2PasswordBearer

SECRET_KEY = 'ddd80a711e1f3cb938d2bf638e9e402ac842e8dc0a674c48ad59e12dd47df0e4'
ALGORITHM = 'HS256'
ACESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    exp  = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": exp})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_acess_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get('user_id')
    except JWTError:
        raise credentials_exception 

def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'bearer'})
    return verify_acess_token(token, credentials_exception)



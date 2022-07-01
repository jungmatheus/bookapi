from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import database_models, schemas
from typing import List

router = APIRouter(prefix='/categories', tags=['Categories'])

@router.get('/', response_model=List[schemas.CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(database_models.Category).all()
    return categories


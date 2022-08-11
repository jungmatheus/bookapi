from fastapi.testclient import TestClient
from ..main import app
from ..config import settings as s
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..database import get_db
from .. import database_models
import pytest



#ACCESSING TESTING DATABASE


SQLALCHEMY_DATABASE_URL = f'postgresql://{s.DATABASE_USERNAME}:{s.DATABASE_PASSWORD}@{s.DATABASE_HOSTNAME}/{s.DATABASE_NAME}_test'
engine = create_engine(SQLALCHEMY_DATABASE_URL)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



@pytest.fixture()
def session():
    database_models.Base.metadata.drop_all(bind=engine)
    database_models.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):

    def get_test_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = get_test_db
    
    return TestClient(app)
from fastapi.testclient import TestClient
from ..main import app
from ..config import settings as s
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..database import get_db
from .. import database_models
import pytest
from ..oauth2 import create_access_token



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



@pytest.fixture
def test_user(client):
    new_user = {
        "email": "firstuser@gmail.com",
        "password": "987654",
        "username": "firstuser"
    }
    res = client.post("/users/", json=new_user)
    assert res.status_code == 201
    user_data = res.json()
    user_data['password'] = new_user["password"]
    return user_data


@pytest.fixture
def token(test_user):
    user_payload = {"user_id": test_user['id'], "username": test_user['username']}
    return create_access_token(user_payload)


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client 



@pytest.fixture
def create_categories(session):
    categories = [
        {"name": "Terror"},
        {"name": "Romance"},
        {"name": "Historical"}
    ]
    session.add_all(list(map(lambda x: database_models.Category(**x), categories)))
    session.commit()
    return session.query(database_models.User).all()

@pytest.fixture
def create_books(test_user, session, create_categories):

    books = [
        {
            "title": "The Lady of The Lake",
            "category_id": 1,
            "user_id": test_user['id'],
            "author": "Author123",
            "number_of_pages": 499
        },
        {
           "title": "The Mountain",
            "category_id": 2,
            "user_id": test_user['id'],
            "author": "Name444",
            "number_of_pages": 150 
        },
          {
           "title": "Bees",
            "category_id": 1,
            "user_id": test_user['id'],
            "author": "Beequeen",
            "number_of_pages": 999 
        }
    ]

    formatted_books = list(map(lambda x: database_models.Book(**x), books))
    session.add_all(formatted_books)
    session.commit()
    return session.query(database_models.Book).all()


    
from app import database_models
from .. import schemas


def test_get_books(authorized_client, create_books):
    res = authorized_client.get('/books/')
    formatted_books = list(map(lambda x: schemas.BookOut(**x), res.json()))
    assert res.status_code == 200


def test_unauthorized_user_get_all(client, create_books):
    res = client.get('/books/')
    assert res.status_code == 401

    
def test_unauthorized_user_get_one(client, create_books):
    id = create_books[0].id
    res = client.get(f"/books/{id}")
    assert res.status_code == 401

def test_invalid_id(authorized_client, create_books):
    res = authorized_client.get('/books/9999')
    print(res.json())
    assert res.status_code == 404


def test_get_one(authorized_client, create_books):
    res = authorized_client.get(f"/books/{create_books[0].id}")
    assert res.status_code == 200
    assert res.json()['Book']['title'] == create_books[0].title
    

def test_create_book(authorized_client, create_categories):
    res = authorized_client.post("/books/", json={
        "category_id": create_categories[0].id,
        "title": "Test title 001",
        "author": "testAuthor001",
        "number_of_pages": 555
    })
    assert schemas.BookBase(**res.json())
    assert res.status_code == 201 


def test_unathorized_delete(client, create_books):
    res = client.delete(f"/books/{create_books[0].id}")
    assert res.status_code == 401

def test_delete_book(authorized_client, create_books):
    res = authorized_client.delete(f"/books/{create_books[0].id}")
    assert res.status_code == 204

def test_delete_invalid_book(authorized_client, create_books):
    res = authorized_client.delete("/books/9999")
    assert res.status_code == 404

from http.client import HTTPException
from jose import jwt
from ..config import settings as s
from .. import schemas
import pytest



def test_create_user(client):
    res = client.post('/users/', json={
        "email": "firstuser@gmail.com",
        "password": "987654",
        "username": "firstuser"
    })
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post('/login/', data={
        "username": test_user['email'],
        "password": test_user['password']
    })
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, s.SECRET_KEY, algorithms=[s.ALGORITHM])
    assert res.status_code == 200
    assert payload.get('user_id') == test_user['id']



@pytest.mark.parametrize("email, password, status_code", [
    ("firstuser@gmail.com", "wrongpass", 403),
    ("wrongemail", "987654", 403),
    ("wrongemail", "wrongpassword", 403),
    (None, "987654", 422),
    ("firstuser@gmail.com", None, 422)
])
def test_wrong_credentials(client, test_user, email, password, status_code):
   
    res = client.post('/login/', data={
        "username": email,
        "password": password
    })
    assert res.status_code == status_code
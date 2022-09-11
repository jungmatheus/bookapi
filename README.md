# Bookapi

## General info
A simple API built with FastAPI, tested with Pytest and containerized and deployed to DockerHub. It has a simple CI/CD pipeline built with GitHub Actions.


## Main Technologies
* FastAPI
* PostgreSQL
* Docker
* SQLAlchemy

## Setup
To test this API, navigate to https://bookishocto.shop/docs

If you want to run it on your local machine, you'll need to have Python3 installed and a connection to a PostgreSQL database. Then, you can follow these steps:

```
$ mkdir bookapi && cd $_
$ git clone https://github.com/jungmatheus/bookapi.git .
$ python3 -m venv venv
$ pip install -r requirements.txt
```
Then, create a .env file in the app directory. It should look like this: 
```
DATABASE_USERNAME=postgres
DATABASE_NAME=testdb
DATABASE_PASSWORD=password123
SECRET_KEY=ddd80a711e1f3cb938d2bf638e9e402ac842e8dc0a674c48ad59e12dd47df0e4
DATABASE_HOSTNAME:localhost
ACCESS_TOKEN_EXPIRE_MINUTES:90
ALGORITHM:HS256
DATABASE_PORT:5432
```
Finally, run:
```
uvicorn app.main:app --reload
``` 


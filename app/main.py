from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import books, categories, users, login, vote
from . import database_models
from .database import engine



database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)



app.include_router(books.router)
app.include_router(categories.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return {"message": "Hello World deployed to ubuntu!"}

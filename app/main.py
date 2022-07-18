from fastapi import FastAPI
from .routers import books, categories, users, login, vote
from . import database_models
from .database import engine



database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)
app.include_router(categories.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return {"message": "Hello World"}

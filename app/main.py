from fastapi import FastAPI
from .routers import books, categories
from . import database_models
from .database import engine



database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)
app.include_router(categories.router)




@app.get('/')
def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from .routers import books
from . import database_models
from .database import engine



database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books.router)




@app.get('/')
def root():
    return {"message": "Hello World"}

"""Main api initial"""
from fastapi import FastAPI
from .routers import items, users
import uvicorn


app = FastAPI()
app.include_router(users.router)
app.include_router(items.router, prefix='/items', tags=['items'])


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

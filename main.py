"""Main api initial"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    """Root path (/)"""
    return {'message': 'Hello world'}

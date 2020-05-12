"""Main api initial"""
from enum import Enum
from fastapi import FastAPI
import uvicorn


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


@app.get('/')
async def root():
    """Root path (/)"""
    return {'message': 'Hello world'}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/files/{file_path:path}')
async def get_file(file_path: str):
    return {'message': f'Your file path: {file_path}'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

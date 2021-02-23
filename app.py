from fastapi import FastAPI, HTTPException
from CatNotes import CatNotes
import numpy as np
import sklearn
import pickle
import uvicorn
import pandas as pd

app = FastAPI()
pickle_in = open("classificate.pkl", "rb")
classificate = pickle.load(pickle_in)


@app.get("/")
def index():
    return {'message': 'hello'}


@app.post("/predict")
def predict_catnote(data: CatNotes):
    data = data.dict()
    name = data['name']
#   category = data['category']
# print(classificate.predict([name]))
    prediction = classificate.predict([name])
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
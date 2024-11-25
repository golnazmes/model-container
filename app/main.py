from fastapi import FastAPI
from transformers import pipeline
import numpy as np

model = pipeline('sentiment-analysis')


app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Model Inference API'}

@app.post('/infer')
def infer(data: str):
    prediction = model(data)
    return {'prediction': prediction}

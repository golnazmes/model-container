from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
)

# Initialize FastAPI app
app = FastAPI()


# Define input schema
class InputData(BaseModel):
    input: str


@app.get("/")
def read_root():
    return {"message": "Model Inference API"}


@app.post("/infer")
def infer(data: InputData):
    # Extract the text input
    input_text = data.input
    # Perform sentiment analysis
    analysis = sentiment_pipeline(input_text)
    return {"analysis": analysis}

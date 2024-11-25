# Sentiment Analysis API Docker Setup

I used  `cardiffnlp/twitter-roberta-base-sentiment-latest`, documentation: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest


## Why This Model:

- **Fine-tuned for Social Media**: Specifically trained on social media data, perfect for informal text.
- **State-of-the-Art**: Utilizes the RoBERTa transformer architecture.
- **Pretrained on Relevant Datasets**: Includes emojis, hashtags, and slang for better accuracy.
- **Suitable For**:
  - **Data**: Short text with emojis, hashtags, and slang.
  - **Labels**: Positive, negative, neutral sentiment.
  - **Use Cases**: Social media monitoring, feedback, and trend analysis.

## Considerations When Choosing a Model:
- **Data Relevance**: Ensure the model matches your data.
- **Fine-tuning**: Decide if additional fine-tuning is needed.
- **Model Size & Speed**: Larger models offer better accuracy but are slower and require more resources. Balance as needed.


## Local Access\
run the following:\
```bash
   fastapi dev main.py
```


## Docker Setup

1. **Build the Docker image**:
   ```bash
   docker build -t infer_model_image .
2. **Run the Docker Container**:
    ```bash
    ddocker run --name infer_model_container -p 8000:8000 infer_model_image

3. **Access the API**\
a) via web interface

http://0.0.0.0:8000/docs \

2)via a script\
`clien.ipynb`


4. **Next steps**

- push image to dockerhub
- deploy the container to cloud (e.g aws)
- automate the test and deployment process with workflows
- improve documentation

 



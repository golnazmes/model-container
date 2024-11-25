# model-container

FROM python:3.11 #what python image are you going to use (pulled from dockerhob,)

WORKDIR /app  #create code directory in the container and assign as the working directory

COPY ./app /app copy the requirements and everything and place them inside the directory

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 $some endpoint to where we can send the data and interact
c#command to run
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
uvicorn: server gateway interface, aqllows fast api to serve the requests
"app.server:app" what to run
network to host the container
port which was exposed

docker build -t image_name . #run the container
docker run --name container_name -o 8000:8000 image_name
d


/docs
default endpoint within fast api
get and post


/how to send data
import json
import requests

data
url
data 
response = requests.post()
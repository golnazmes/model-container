#start with a base image that has python installed
FROM python:3.11 

#change the working directory to /code 
WORKDIR /code

#copy the requirements file to the working directory of docker image
COPY ./requirements.txt /code/requirements.txt

#install the dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

#copy the rest of the application code to the working directory of docker image
COPY ./app /code/app

EXPOSE 8000

#commands to run whene the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

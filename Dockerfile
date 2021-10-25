#Dockerfile, Image, container

FROM python:3.6.15-alpine3.13

WORKDIR .

#Install dependencies
COPY requirements.txt .
#RUN pip install -r ./requirements.txt 
RUN python3 -m pip install -r requirements.txt
#copy source codes
#ADD core.py .
COPY /tests .

#run applications
CMD ["python","./core.py"]

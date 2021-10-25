#Dockerfile, Image, container

FROM python:3.11.0a1-bullseye

WORKDIR .

#Install dependencies
#COPY requirements.txt .
RUN pip install -r requirements.txt 

#copy source codes
#COPY /test.py .
RUN pip install -r requirements.txt 

#run applications

#ADD core.py .

#RUN pip install requests numpy

CMD ["python","./core.py"]

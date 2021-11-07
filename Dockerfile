FROM python:3.8-slim-buster
EXPOSE 5000

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install python3-opencv -y

COPY requirements.txt requirements.txt
RUN pip3 install Flask

COPY . .
CMD ["python3", "app.py"]

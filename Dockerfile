FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

RUN python3 -m pip install --upgrade pip

ENV TZ=Asia/Kolkata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

COPY . /app/

WORKDIR /app/

RUN pip3 install -U -r requirements.txt

CMD ["bash", "startup"]

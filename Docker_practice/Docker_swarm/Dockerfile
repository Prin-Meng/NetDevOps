# syntax=docker/dockerfile:1
FROM centos
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN  yum -y install python3 vim net-tools bind-utils
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000
COPY app.py /code/app.py
CMD ["flask", "run"]
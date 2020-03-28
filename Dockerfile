FROM python:slim

WORKDIR /app
COPY source_code/ /app

RUN pip install -r requirements.txt

ENV MYSQL_HOST MYSQL_USER MYSQL_PWD PK

ENTRYPOINT ["python", "server.py"]

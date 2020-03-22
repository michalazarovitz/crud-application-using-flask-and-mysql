FROM python:3.5-alpine

WORKDIR /app
COPY source_code/ /app

RUN pip install -r requirements.txt

ENV MYSQL_HOST MYSQL_USER MYSQL_PWD

ENTRYPOINT ["python", "server.py"]

FROM postgres:latest

LABEL maintainer="Prin<xxx@qq.com>"
LABEL version = "1.0"
LABEL description="prin psql images"

ENV POSTGRES_PASSWORD=Cisc0123

ADD init-user-db.sql /docker-entrypoint-initdb.d/


FROM centos:latest

LABEL maintainer="Prin<xxx@qq.com>"
LABEL version = "1.0"
LABEL description="prin First DcokerFile"

RUN yum -y update && yum -y install yum net-tools

WORKDIR /prin

ADD For_add /prin
COPY For_cp /prin
ADD for_add1.tar.gz /prin/unzip/

ENV IF_NAME =ens33 SSH_POST=22

VOLUME /prin

EXPOSE $SSH_POST

CMD "ifconfig $IF_NAME"

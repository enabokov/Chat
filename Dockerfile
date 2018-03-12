FROM ubuntu:16.04

RUN apt-get -y update \
    && apt-get -y install software-properties-common python3-software-properties \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get -y update

RUN apt-get -y install curl \
    && curl -sL https://deb.nodesource.com/setup_4.x | bash \
    && apt-get -y install nodejs \
    && apt-get -y update

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/

RUN apt-get -y install python3.6 python3.6-dev python3.6-venv

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6

RUN apt-get -y update

WORKDIR /opt/app
ADD . /opt/app

RUN pip3.6 install -r requirements.txt

#RUN rm -r node_modules
#RUN npm cache clean
#RUN npm install

RUN python3.6 -V
RUN pip3.6 -V

CMD ["python3.6", "runner.py"]

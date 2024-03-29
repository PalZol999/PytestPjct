FROM python:3.7

#= LOCAL_OPTS=-v $(shell pwd):/opt/restapi_testfwk
WORKDIR /opt/restapi_testfwk
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/restapi_testfwk
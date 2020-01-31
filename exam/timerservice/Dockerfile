FROM python:3
WORKDIR /myproject
COPY ./requirements.txt /myproject
RUN pip3 install -r requirements.txt
COPY myproject /myproject
ENTRYPOINT ["python", "timeservice.py"]

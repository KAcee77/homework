FROM python:3.8-slim

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

CMD ['python3', 'manage.py', 'runserver']

EXPOSE 8000
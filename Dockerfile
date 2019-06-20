FROM python:rc-alpine

WORKDIR /usr/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./visits .
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



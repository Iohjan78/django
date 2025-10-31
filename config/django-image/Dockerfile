FROM python:3.12-bookworm

RUN apt-get update && apt-get install python3-dev libgdal-dev graphviz graphviz-dev -y --force-yes

WORKDIR /usr/src/app

RUN pip install --upgrade pip setuptools

COPY requirements.txt ./

RUN pip install --no-cache -r requirements.txt

EXPOSE 8000

RUN django-admin startproject app ./

RUN chown -R 1000:1000 /usr/src/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
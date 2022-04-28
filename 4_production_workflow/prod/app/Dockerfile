FROM python:3.8

#update
RUN apt-get update

#install requirements
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "wsgi:app"]

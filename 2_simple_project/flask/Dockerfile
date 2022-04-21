# We copy just the requirements.txt first to leverage Docker cache
FROM ubuntu:20.04
RUN apt-get update && apt install -y python3.8 python3-pip
# COPY . . is a minimalist version of a docker file
# could also do ..
#WORKDIR /flask_app
COPY . .
# then all the code will be in the python-docker
RUN pip install -r requirements.txt
CMD ["python3", "app.py" ]

FROM python:3.9
WORKDIR /flask_app
# could remove this with volumes set up, but can make testing tough
COPY . . 
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

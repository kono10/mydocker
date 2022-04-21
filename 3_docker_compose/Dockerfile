FROM python:3.9
WORKDIR /flask_app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

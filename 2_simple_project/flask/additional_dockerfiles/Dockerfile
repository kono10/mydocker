FROM python:3.9
WORKDIR /flask_app
COPY . .
# this is not recommended, will change version without warning
RUN pip install Flask
CMD ["python", "app.py"]

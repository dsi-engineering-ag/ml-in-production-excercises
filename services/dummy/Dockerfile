FROM python:3.13

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind",  "0.0.0.0:9000", "ModelService:app"]

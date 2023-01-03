FROM python:3.10-buster

RUN pip install -Iv mlflow==2.1.1

ENTRYPOINT ["mlflow", "server", "-p", "5500", "-h", "0.0.0.0", "--default-artifact-root",  "./artifacts", "--backend-store-uri", "sqlite:///mlflow.db"]

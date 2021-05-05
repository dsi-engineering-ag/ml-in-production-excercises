FROM python:3-buster

RUN pip install mlflow

ENTRYPOINT ["mlflow", "server", "-p", "5500", "-h", "0.0.0.0", "--default-artifact-root",  "./artifacts", "--backend-store-uri", "sqlite:///mlflow.db"]

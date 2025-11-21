FROM python:3.13

RUN pip install -Iv mlflow==3.6.0

ENV MLFLOW_SERVER_ALLOWED_HOSTS *

ENTRYPOINT ["mlflow", "server", "-p", "5500", "--host", "0.0.0.0", "--allowed-hosts", "*", "--default-artifact-root",  "/tmp/artifacts", "--backend-store-uri", "sqlite:///mlflow.db"]

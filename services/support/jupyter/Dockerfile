FROM quay.io/jupyter/scipy-notebook:python-3.13

# RUN apt-get update && apt-get install graphwiz


# RUN conda install --file requirements.txt -y

RUN pip install 'dvc[gs]'

RUN curl -sSL https://sdk.cloud.google.com | bash -s -- \
    --disable-prompts \
    --install-dir=/home/jovyan

ENV PATH=$PATH:/home/jovyan/google-cloud-sdk/bin
RUN gcloud components install kubectl --quiet


COPY requirements.txt .
RUN pip install -r requirements.txt

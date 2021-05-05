FROM jupyter/scipy-notebook

# RUN apt-get update && apt-get install graphwiz

COPY requirements.txt .
RUN conda install --file requirements.txt -y

RUN pip install 'dvc[gs]'

RUN apt-get install curl
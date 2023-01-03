FROM jupyter/scipy-notebook:python-3.7.12

# RUN apt-get update && apt-get install graphwiz

COPY requirements.txt .
RUN conda install --file requirements.txt -y

RUN pip install 'dvc[gs]'

RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-412.0.0-linux-x86_64.tar.gz && \
    tar -xzf google-cloud-cli-412.0.0-linux-x86_64.tar.gz && rm google-cloud-cli-412.0.0-linux-x86_64.tar.gz && \
    ./google-cloud-sdk/install.sh --quiet && \
    echo "source '/home/jovyan/google-cloud-sdk/path.bash.inc'" >> /home/jovyan/.bashrc  && \
    ./google-cloud-sdk/bin/gcloud components install kubectl --quiet

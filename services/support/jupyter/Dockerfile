FROM jupyter/scipy-notebook

# RUN apt-get update && apt-get install graphwiz

COPY requirements.txt .
RUN conda install --file requirements.txt -y

RUN pip install 'dvc[gs]'

RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-339.0.0-linux-x86_64.tar.gz && \
    tar -xzf google-cloud-sdk-339.0.0-linux-x86_64.tar.gz && rm google-cloud-sdk-339.0.0-linux-x86_64.tar.gz && \
    ./google-cloud-sdk/install.sh --quiet && \
    echo "source '/home/jovyan/google-cloud-sdk/path.bash.inc'" >> /home/jovyan/.bashrc  && \
    ./google-cloud-sdk/bin/gcloud components install kubectl --quiet

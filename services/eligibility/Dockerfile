FROM python:3.7

COPY . /app
WORKDIR /app
RUN echo "test" > /tmp/test.txt
RUN pip install -r requirements.txt

ENV MODEL_NAME EligibilityModel
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE 
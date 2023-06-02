# build stage
FROM node:16-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM python:3.7

COPY --from=build-stage /app/dist /app/
COPY requirements.txt /app
COPY app.py /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind",  "0.0.0.0:8000", "app:app"]
from flask import jsonify, Flask, send_from_directory, request, Response, jsonify, request
import requests

import os

app = Flask(__name__)

PORT = os.environ.get("PORT", "5000")
API_ENDPOINT = os.environ.get("ELIGIBILITY_API_ENDPOINT", "http://localhost:8100")

@app.route("/api/v1/predict", methods=["GET", "POST"])
def predict():
    r = requests.get(url=API_ENDPOINT+'/predict', json=request.get_json())

    data = r.json()

    return jsonify(data)


@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_content(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
import logging
from flask import Flask, Response, request, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from DummyModel import DummyModel

model = DummyModel()


## Monitoring counters
ELIGIBLE_COUNTER = Counter(
    'eligible_total',
    'Total eligible prediction results',
    []
)
NOT_ELIGIBLE_COUNTER = Counter(
    'not_eligible_total',
    'Total not eligible prediction results',
    []
)

## Python Flask API
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('MODEL_SERVICE')

@app.route("/predict", methods=["GET", "POST"])
def predict():

    logger.debug(f"Serving request: {request.get_json(silent=True)}")

    request_data = request.get_json()

    predictions = model.predict(request_data['data']['ndarray'])

    # Update counters
    ELIGIBLE_COUNTER.inc(int(sum(predictions)))
    NOT_ELIGIBLE_COUNTER.inc(int(len(predictions)-sum(predictions)))

    # Prepare response
    resp = jsonify({
      "data": {
        "names": [],
        "ndarray": predictions.tolist()
      }
    })

    logger.debug(f"Writing response: [{resp.status}] {resp.get_data(as_text=True)}")

    return resp

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(port=9000)
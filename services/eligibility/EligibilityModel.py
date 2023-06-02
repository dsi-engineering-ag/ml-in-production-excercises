

from seldon_core.user_model import SeldonResponse
from joblib import dump, load

import logging

class EligibilityModel:

    def __init__(self):
        self.model = load('eligibility_pipeline.joblib')

    def predict(self, X, feature_names):
        logging.warn("HERE")

        Y = self.model.predict(X)

        runtime_metrics = [
            {"type": "COUNTER", "key": "eligible", "value": int(sum(Y))},
            {"type": "COUNTER", "key": "not_eligible", "value": int(len(Y)-sum(Y))}
        ]

        return SeldonResponse(data=Y, metrics=runtime_metrics)
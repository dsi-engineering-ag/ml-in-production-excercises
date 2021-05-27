
from sklearn.dummy import DummyClassifier

from seldon_core.user_model import SeldonResponse

class DummyModel:

    def __init__(self):
        self.model = DummyClassifier(strategy='constant', constant=1)
        self.model.fit([[0,0], [0,0]], [1, 0])

    def predict(self, X, feature_names):
        print(X)

        Y = self.model.predict(X)

        runtime_metrics = [
            {"type": "COUNTER", "key": "eligible", "value": int(sum(Y))},
            {"type": "COUNTER", "key": "not_eligible", "value": int(len(Y)-sum(Y))}
        ]

        return SeldonResponse(data=Y, metrics=runtime_metrics)
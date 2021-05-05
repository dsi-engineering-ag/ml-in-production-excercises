
from sklearn.dummy import DummyClassifier

class DummyModel:

    def __init__(self):
        self.model = DummyClassifier(strategy='constant', constant=1)
        self.model.fit([[0,0], [0,0]], [1, 0])

    def predict(self, X, feature_names):
        
        return self.model.predict(X)
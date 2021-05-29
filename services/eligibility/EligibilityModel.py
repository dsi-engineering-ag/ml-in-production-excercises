
from joblib import dump, load

from seldon_core.user_model import SeldonResponse

class EligibilityModel:

    def __init__(self):
        eligibility_model = load('eligibility_pipeline.joblib')

        self.model = eligibility_model

    def predict(self, X, feature_names):
        
        return self.model.predict(X)
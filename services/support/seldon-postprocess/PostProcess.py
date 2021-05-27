
from seldon_core.user_model import SeldonResponse

import numpy as np

import logging

class PostProcess:

    def predict(self, Xs, features_names=[]):
        logging.info("Post Process")
        logging.info(Xs)

        return [0]

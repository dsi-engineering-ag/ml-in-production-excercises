
from seldon_core.user_model import SeldonResponse

import numpy as np

import logging

class Combiner:

    def aggregate(self, Xs, features_names=[]):
        logging.info("Combiner")
        logging.info(Xs)

        return [ 1 if Xs[0] == Xs[1] and np.equal(1, Xs[0]) else 0 ]


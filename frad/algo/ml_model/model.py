import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

__all__ = [
    'Model',
]

class Model(object):
    def __init__(self):
        with open('./model.pickle', 'rb') as f:
            self.estimator = pickle.load(f)

        with open('./tfidf.pickle', 'rb') as f:
            self.tfidf = pickle.load(f)

    def predict(self, X):
        X = X.lower()
        X = np.array([X], dtype='U')
        X_tf = self.tfidf.transform(X)

        return self.estimator.predict(X_tf)[0]

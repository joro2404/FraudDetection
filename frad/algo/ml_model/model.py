import pickle
import numpy as np
import re

__all__ = [
    'Model',
]

class Model(object):
    def __init__(self):
        with open('/Users/victor/Documents/FraudDetection/frad/algo/ml_model/model.pickle', 'rb') as f:
            self.estimator = pickle.load(f)

        with open('/Users/victor/Documents/FraudDetection/frad/algo/ml_model/tfidf.pickle', 'rb') as f:
            self.tfidf = pickle.load(f)

    def predict(self, X):
        X = X.lower()
        X = re.sub(r'\s{2,}', '', X)
        X = X.replace('.', '')
        X = X.replace(',', '')
        X = X.replace('?', '')
        X = X.replace('!', '')

        numbers  = re.findall(r'\$\d+', X)
        if len(numbers) != 0:
            n=1
            for number in numbers:
                number  = number[1:]
                i = len(number)
                res = ''

                if i > 6:
                    number = number[0]
                    res = ' million '
                else:
                    number = number[:3]
                    res = ' thousand '

                X = re.sub(r'\$\d+', number + res + str('dollars'), X, n)
                n+=1

        print(X)

        X = np.array([X], dtype='U')
        X_tf = self.tfidf.transform(X)

        return self.estimator.predict(X_tf)[0]

from abc import ABCMeta, abstractmethod, abstractproperty
from Classifier import Classifier, FIGSIZE, COLORS, MARKERS
import numpy as np

class RegressionModel(Classifier) :
    __metaclass__ = ABCMeta

    @staticmethod
    def augment_matrix(X):
        num_samples, num_features = X.shape
        X_aug = np.hstack([np.ones((num_samples, 1)), X])
        return X_aug

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict_proba(self, X):
        pass

    def predict(self, X):
        return super(RegressionModel, self).predict(X)

    def missclassification(self, X, y):
        return super(RegressionModel, self).missclassification(X, y)

    @abstractmethod
    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        pass

from abc import ABCMeta, abstractmethod, abstractproperty
import numpy as np

FIGSIZE=(10,8)
COLORS = ["steelblue", "sandybrown"]
MARKERS = ["x", "o"]

class Classifier(object) :
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fit(self, **kwargs):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def missclassification(self, X, y):
        n = len(y)
        y_pred = self.predict(X)
        nr_missclassif = float(len(np.where(y_pred!=y)[0]))
        missclassification_rate = nr_missclassif/n
        return missclassification_rate

    @abstractmethod
    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        pass

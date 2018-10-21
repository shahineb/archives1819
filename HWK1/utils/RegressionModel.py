from abc import ABCMeta, abstractmethod, abstractproperty
from Classifier import Classifier, FIGSIZE, COLORS, MARKERS

class RegressionModel(Classifier) :
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def missclassification(self, X, y):
        return super(RegressionModel, self).missclassification(X, y)

    @abstractmethod
    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        pass

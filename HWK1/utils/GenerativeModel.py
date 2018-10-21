from abc import ABCMeta, abstractmethod, abstractproperty
from Classifier import Classifier, FIGSIZE, COLORS, MARKERS


class GenerativeModel(Classifier) :
    __metaclass__ = ABCMeta

    def __init__(self):
        self.pi_ = None
        self.mu_ = None
        self.sigma_ = None

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict_proba(self, X):
        pass

    def predict(self, X):
        return super(GenerativeModel, self).predict(X)

    def missclassification(self, X, y):
        return super(GenerativeModel, self).missclassification(X, y)

    @abstractmethod
    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        pass

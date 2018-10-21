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
        pred_proba = self.predict_proba(X)
        pred_proba[pred_proba>0.5]=1
        pred_proba[pred_proba!=1]=0
        return pred_proba

    def missclassification(self, X, y):
        return super(GenerativeModel, self).missclassification(X, y)

    @abstractmethod
    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        pass

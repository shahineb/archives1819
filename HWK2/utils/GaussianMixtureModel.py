from abc import ABCMeta, abstractmethod
from KMeans import KMeans
import numpy as np
from scipy import stats


class GaussianMixtureModel(object):
    __metaclass__ = ABCMeta

    def __init__(self, k, initialization):
        """
        Attributes:
        -----------
        k_: integer
            number of components
        initialization_: {"kmeans", "random"}
            type of initialization
        pi_: numpy.array
            (k_,)
            multinomial law vector
        mu_: numpy.array
            (k_, nr_feature)
            array containing means
        Sigma_: numpy.array
            (k_, nr_feature, nr_feature)
            array containing covariance matrix
        N_: numpy.array
            (n_sample, k_)
            matrix of gaussian pdf evaluation on each sample for each
            distribution
        cond_prob_: numpy.array
            (nr_sample, k_)
            conditional probabilities for all data points
        labels_: numpy.array
            (nr_sample,)
            labels for data points
        """
        self.k_ = k
        self.initialization_ = initialization
        self.mu_ = None
        self.N_ = None
        self.pi_ = None
        self.cond_prob_ = None
        self.labels_ = None

    def compute_condition_prob_matrix_(self, X):
        '''Compute the conditional probability matrix
        shape: (nr_sample, k_)
        '''
        n, p = X.shape
        self.N_ = np.array([stats.multivariate_normal(self.mu_[k], self.Sigma_[k]).pdf(X) for k in range(self.k_)]).T
        self.cond_prob_ = self.N_ * self.pi_
        for i in range(n):
            self.cond_prob_[i, :] = self.cond_prob_[i, :] / np.sum(self.cond_prob_[i, :])
        return self.cond_prob_

    def compute_expectation_(self):
        '''Compute the expectation to check increment'''
        E_log_likelihood = np.sum(self.cond_prob_ * np.log(self.N_)) + np.sum(self.cond_prob_ * np.log(self.pi_))
        return E_log_likelihood

    def initialize_(self, X):
        n, p = X.shape
        # kmeans initialization
        if self.initialization_ == 'kmeans':
            kmeans_clstr = KMeans(n_clusters=self.k_)
            kmeans_clstr.fit_predict(X)
            labels = kmeans_clstr.labels_
            self.cond_prob_ = np.zeros((n, self.k_))
            for i in range(n):
                self.cond_prob_[i, labels[i]] = 1
        # else randomly initialize them
        else:
            # TODO : make sure this is actually a probability matrix
            self.cond_prob_ = np.random.rand(n, self.k_)

    @abstractmethod
    def fit(self, X, eps=1e-4, max_iter=100):
        pass

    def predict_proba(self, X):
        """ Predict probability vector for X

        Parameters:
        -----------
        X: (n, p) np.array

        Returns:
        -----
        proba: (n, k) np.array
        """
        n, p = X.shape
        N_ = np.array([stats.multivariate_normal(self.mu_[k], self.Sigma_[k]).pdf(X) for k in range(self.k_)]).T
        cond_prob_ = N_ * self.pi_
        for i in range(n):
            cond_prob_[i, :] = cond_prob_[i, :] / np.sum(cond_prob_[i, :])
        return cond_prob_

    def predict(self, X):
        """ Predict labels for X

        Parameters:
        -----------
        X: numpy.array
            (nr_sample, nr_feature)
        Returns:
        -----
        label affectation
        """
        proba_cluster = self.predict_proba(X)
        labels = np.argmax(proba_cluster, axis=1)
        return labels

    def missclassification(self, X, labels):
        n = len(labels)
        labels_pred = self.predict(X)
        nr_missclassif = float(len(np.where(labels_pred != labels)[0]))
        missclassification_rate = nr_missclassif / n
        return missclassification_rate

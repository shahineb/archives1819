from GaussianMixtureModel import GaussianMixtureModel
import numpy as np


class GMM(GaussianMixtureModel):

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
        super(GMM, self).__init__(k, initialization)

    def fit(self, X, eps=1e-4, max_iter=100):
        """ Find the parameters pi_, mu_ and nu_
        that better fit the data

        Parameters:
        -----------
        X: (n, p) np.array
            Data matrix

        Returns:
        -----
        self
        """
        def compute_estimators_(X):
            '''Compute the MLE of the model parameters'''
            self.pi_ = np.mean(self.cond_prob_, axis=0)
            self.mu_ = [np.sum(X.T * self.cond_prob_[:, j], axis=1) / np.sum(self.cond_prob_[:, j]) for j in range(self.k_)]
            self.Sigma_ = []
            for j in range(self.k_):
                foo = np.array([tau * np.matmul((x - self.mu_[j]).reshape(-1, 1), (x - self.mu_[j]).reshape(1, -1))
                                for tau, x in zip(self.cond_prob_[:, j], X)])
                foo = np.sum(foo) / np.sum(self.cond_prob_[:, j])
                self.Sigma_ += [foo]

        # intialize
        super(GMM, self).initialize_(nr_clusters=self.k_)
        compute_estimators_(X)

        n_iter = 0
        l_c = 0
        conv_criteria = True

        while conv_criteria and n_iter < max_iter:
            conv_criteria = l_c

            super(GMM, self).compute_condition_prob_matrix_(X)
            l_c = super(GMM, self).compute_expectation_()
            compute_estimators_(X)

            conv_criteria = np.abs(conv_criteria - l_c) < eps

        self.labels_ = np.argmax(self.cond_prob_, axis=1)

    def predict_proba(self, X):
        """ Predict probability vector for X

        Parameters:
        -----------
        X: (n, p) np.array

        Returns:
        -----
        proba: (n, k) np.array
        """
        return super(GMM, self).predict_proba(X)

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
        return super(GMM, self).predict(X)

    def missclassification(self, X, y):
        return super(GMM, self).missclassification(X, y)

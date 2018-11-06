from KMeans import KMeans
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


FIGSIZE = (12, 8)
CMAP = plt.cm.Dark2
MARKER = 'D'
MARKER_SIZE = 150
MARKER_COLOR = 'crimson'
ALPHA = 0.4
QUANTILE = 0.9


class GaussianMixtureModel(object):

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
        self.Sigma_ = None
        self.N_ = None
        self.pi_ = None
        self.cond_prob_ = None
        self.labels_ = None
        
    def compute_multivariate_normal_matrix(self, X):
        """Computes the matrix of gaussian pdf evaluation on each sample for each
            distribution
        """
        self.N_ = np.array([stats.multivariate_normal(self.mu_[k], self.Sigma_[k]).pdf(X) for k in range(self.k_)]).T

    def compute_condition_prob_matrix_(self, X):
        '''Compute the conditional probability matrix
        shape: (nr_sample, k_)
        '''
        n, p = X.shape
        self.compute_multivariate_normal_matrix(X)
        self.cond_prob_ = self.N_ * self.pi_
        self.cond_prob_ = self.cond_prob_ / np.sum(self.cond_prob_, axis=1)[:, np.newaxis]
        return self.cond_prob_

    def compute_expectation_(self):
        '''Compute the expectation to check increment'''
        E_log_likelihood = np.sum(self.cond_prob_ * np.log(self.N_)) + np.sum(self.cond_prob_ * np.log(self.pi_))
        return E_log_likelihood
    
    def initialize_(self, X):
        n, p = X.shape
        # kmeans initialization
        if self.initialization_ == 'kmeans':
            kmeans_clstr = KMeans(nr_clusters=self.k_, n_init=1)
            kmeans_clstr.fit(X)
            labels = kmeans_clstr.labels_
            self.cond_prob_ = np.zeros((n, self.k_))
            for i in range(n):
                j = int(labels[i])
                self.cond_prob_[i, j] = 1
        # else randomly initialize them
        else:
            foo = np.random.rand(n, self.k_)
            self.cond_prob_ = foo / np.sum(foo, axis=1)[:, np.newaxis]

    def compute_estimators_(self, X):
        '''Compute the MLE of the model parameters'''
        self.pi_ = np.mean(self.cond_prob_, axis=0)
        self.mu_ = [np.sum(X.T * self.cond_prob_[:, j], axis=1) / np.sum(self.cond_prob_[:, j]) for j in range(self.k_)]
        self.Sigma_ = []
        for j in range(self.k_):
            foo = np.array([tau * np.matmul((x - self.mu_[j]).reshape(-1, 1), (x - self.mu_[j]).reshape(1, -1))
                            for tau, x in zip(self.cond_prob_[:, j], X)])
            foo = np.sum(foo, axis=0) / np.sum(self.cond_prob_[:, j])
            self.Sigma_ += [foo]

    def fit(self, X, eps=1e-6, max_iter=1000):
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
        # intialize
        self.initialize_(X)
        self.compute_estimators_(X)

        n_iter = 0
        l_c = 0
        conv_criteria = True

        while conv_criteria and n_iter < max_iter:
            conv_criteria = l_c

            self.compute_condition_prob_matrix_(X)
            l_c = self.compute_expectation_()
            self.compute_estimators_(X)

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

    def plot_pred(self, X, labels, title, plot_kwds, ax=None, figsize=FIGSIZE, cmap=CMAP, alpha=ALPHA, quantile=QUANTILE):
        """plots labeled data, centoids and confidence interval ellipses

        Parameters
        ----------
        X : numpy.array
            (nr_sample, nr_feature)
        title : str
            figure title
        level : float
            level for confidence interval, must be between 0 and 1
        ax : Axe
        figsize : tuple
        cmap : plt.cm
            discrete colormap to be used for labeling
        alpha : float
            max opacity level for ellipses
        quantile : float (>0 and <1)
            level for confidence interval, must be between 0 and 1
        """
        def gen_cmap(rgb_color, max_opacity):
            """Generates single-color cmap with decreasing opacity

            Parameters
            ----------
            rgb_color : tuple
                rgb color to use
            max_opacity : float
                highest level of opacity allowed

            Returns
            -------
            plt.cm
                color map
            """
            cdict = {'red': ((0., rgb_color[0], rgb_color[0]),
                             (1., rgb_color[0], rgb_color[0])),
                     'green': ((0., rgb_color[1], rgb_color[1]),
                               (1., rgb_color[1], rgb_color[1])),
                     'blue': ((0., rgb_color[2], rgb_color[2]),
                              (1., rgb_color[2], rgb_color[2])),
                     'alpha': ((0., max_opacity, max_opacity),
                               (1., 0.05, 0.05))
                     }
            cmap = LinearSegmentedColormap('my_cmap', cdict)
            return cmap

        if not ax:
            fig, ax = plt.subplots(figsize=figsize)

        # Set title
        ax.set_title(title, size=21)

        # Plot labeled data
        ax.grid(alpha=0.2)
        ax.scatter(*X.T, c=labels, cmap=cmap, **plot_kwds)

        # Retrieve colors used from cmap to plot labeled data
        len_cmap = len(cmap.colors)
        used_colors_idx = np.rint(np.linspace(0, len_cmap - 1, self.k_)).astype(int)

        # Create meshgrid for ellipse plotting
        x1_axis = np.linspace(*ax.get_xlim())
        x2_axis = np.linspace(*ax.get_ylim())
        granularity = len(x1_axis)
        x1_grid, x2_grid = np.meshgrid(x1_axis, x2_axis)
        x_1_2 = np.vstack([x1_grid.reshape(-1), x2_grid.reshape(-1)]).T

        for j in range(self.k_):
            # Add centroid
            ax.scatter(*self.mu_[j], marker=MARKER, s=MARKER_SIZE, color=MARKER_COLOR)

            # Compute ellipse equation
            inv_sigma = np.linalg.inv(self.Sigma_[j])
            z = np.diagonal(np.matmul(x_1_2 - self.mu_[j], np.matmul(inv_sigma, (x_1_2 - self.mu_[j]).T)))
            z = z.reshape(granularity, granularity)

            # Plot
            level = stats.chi2.ppf(q=quantile, df=len(self.mu_[j]))
            cluster_cmap = gen_cmap(cmap.colors[used_colors_idx[j]], max_opacity=alpha)
            ax.contourf(x1_axis, x2_axis, z, levels=np.linspace(0, level, 10), cmap=cluster_cmap)

from KMeans import KMeans
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from utils.KMeans import KMeans
from utils.GaussianMixtureModel import GaussianMixtureModel, FIGSIZE, MARKER, MARKER_COLOR, CMAP, MARKER_SIZE

FIGSIZE = (12, 8)
CMAP = plt.cm.Dark2
MARKER = 'D'
MARKER_SIZE = 150
MARKER_COLOR = 'crimson'
ALPHA = 0.4
QUANTILE = 0.9

class myHMM(object):

    def __init__(self, k, initialization):
        """
        Attributes:
        -----------
        k_: integer
            number of components
        initialization_: {"kmeans", "random"}
            type of initialization
        N_: numpy.array
            (nr_sample, k_)
            matrix of gaussian pdf evaluation on each sample for each
            distribution
        pi0_: numpy.array
            (k_,)
            multinomial law vector for first node
        A_: numpy.array
            (k_, k_)
            transition probability matrix
        mu_: numpy.array
            (k_, nr_feature)
            array containing means
        Sigma_: numpy.array
            (k_, nr_feature, nr_feature)
            array containing covariance matrix
        alpha_: numpy.array
            (nr_sample,)   #############
            alpha messages
        beta_: numpy.array
            (nr_sample,)        #######################
            beta messages
        cond_prob_: numpy.array
            (nr_sample, k_)
            probability matrix of latent variables given observed variables
        cond_prob_bis_: numpy.array
            (nr_sample - 1, k_ , k_)
            probability matrix of two successive latent variables given observed variables
        """
        self.k_ = k
        self.initialization_ = initialization
        self.N_ = None
        self.pi0_ = None
        self.A_ = None
        self.mu_ = None
        self.Sigma_ = None
        self.alpha_ = None
        self.beta_ = None
        self.cond_prob_ = None
        self.cond_prob_bis_ = None

    def compute_multivariate_normal_matrix(self, X):
        """Computes the matrix of gaussian pdf evaluation on each sample for each
            distribution
        """
        self.N_ = np.array([stats.multivariate_normal(self.mu_[k], self.Sigma_[k]).pdf(X) for k in range(self.k_)]).T

    ########################## Question 1 #######################
    def compute_messages(self, X):
        """Computes alpha and beta messages, stored as log for computation issues
        """
        nr_sample = np.shape(X)[0]

        alpha = np.zeros((nr_sample,self.k_))

        #alpha for the initial states
        alpha[0] = np.log(self.pi0_) + np.log(self.N_[0])

        #alpha for all the other states
        for t in range(nr_sample):
            va = np.log(self.A_) + alpha[t-1]
            max_va =  np.max(va, axis=1)
            alpha[t] = np.log(self.N_[t]) + max_va + np.log(np.sum(np.exp(va - max_va[:, np.newaxis]), axis=1))

        self.alpha_ = alpha

        #################################################

        beta = np.zeros((nr_sample,self.k_))

        #beta for the initial states
        beta[-1] = np.zeros(self.k_) #useless after the initialization

        #beta for all the other states
        for t in range(nr_sample-2, -1, -1):
            va = np.log(self.A_) + beta[t+1] + np.log(self.N_[t+1])
            max_va = np.max(va,axis=1)
            beta[t] = max_va + np.log(np.sum(np.exp(va - max_va[:, np.newaxis]), axis=1))

        self.beta_ = beta


    def compute_condition_prob_matrix_(self, X):
        '''Compute the conditional probability matrix cond_prob_ and cond_prob_bis_
        '''
        nr_sample = np.shape(X)[0]

        maxi = np.max(self.alpha_ + self.beta_) #maximum value on the whole array
        proba_y_log = maxi + np.log(np.sum(np.exp(self.alpha_+self.beta_-maxi)))

        self.cond_prob_ = np.exp(self.alpha_ + self.beta_ - proba_y_log)

        ##########################################

        for t in range(nr_sample-1):
            for i in range(self.k_): #i codes for z_t (and implicitely j for z_t+1)
                va = np.full(self.k_,self.alpha_[t,i]) + self.beta_[t+1] + np.log(self.A_[:,i]) + np.log(self.N_[t+1])
                self.cond_prob_bis_[t,i,:] = np.exp(va-proba_y_log)


    ########################## Question 4 ##################

    def viterbi(self,X): # we divide the algorithm in two steps in order to keep trace of the most likely states

        nr_sample = np.shape(X)[0]

        M = np.zeros((nr_sample, self.k_)) # is the array storing the maximum message's value
        S = np.zeros((nr_sample,self.k_)) # is the array storing the most likely states, depending on the max message

        M[0] = np.log(self.pi0_) + np.log(self.N_[0])

        # First part:
        for t in range(1, nr_sample):
            M[t] = np.log(self.N_[t]) + np.max(np.log(self.A_) + M[t-1], axis=1)
            S[t] = np.argmax(np.log(self.A_) + M[t-1], axis=1)

        # Second part:
        q = np.zeros(nr_sample, dtype=int) #proper array storing the most likely states
        q[-1] = np.argmax(M[nr_sample-1])

        for t in range(nr_sample-2, -1, -1):
            q[t] = S[t+1, q[t+1]]

        return q



    def compute_expectation_(self):
        '''Compute the expectation to check increment'''
        foo1 = np.inner(self.cond_prob_[0], np.log(self.pi0_))
        foo2 = np.sum(np.log(self.A_) * np.sum(self.cond_prob_bis_, axis=0))
        foo3 = np.sum(np.log(self.N_) * self.cond_prob_)
        E_log_likelihood = foo1 + foo2 + foo3
        return E_log_likelihood

    def compute_estimators_(self, X):
        '''Compute the MLE of the model parameters'''
        self.pi0_ = self.cond_prob_[0] / np.sum(self.cond_prob_[0])
        self.mu_ = [np.sum(X.T * self.cond_prob_[:, j], axis=1) / np.sum(self.cond_prob_[:, j]) for j in range(self.k_)]
        self.Sigma_ = []
        for j in range(self.k_):
            foo = np.array([tau * np.matmul((x - self.mu_[j]).reshape(-1, 1), (x - self.mu_[j]).reshape(1, -1))
                            for tau, x in zip(self.cond_prob_[:, j], X)])
            foo = np.sum(foo, axis=0) / np.sum(self.cond_prob_[:, j])
            self.Sigma_ += [foo]
        self.A_ = np.sum(self.cond_prob_bis_, axis=0) / np.sum(self.cond_prob_[1:], axis=0)

    def initialize_(self, X):
        gmm = GaussianMixtureModel(k=self.k_, initialization=self.initialization_)
        gmm.fit(X)
        self.mu_ = gmm.mu_
        self.Sigma_ = gmm.Sigma_

        self.A_ = np.ones((4,4)) * 1/6 + np.identity(4) * 1/3 ## initialization values
        self.pi0_ = np.array([1/4] * 4) ## initialization values
        self.compute_multivariate_normal_matrix(X)
        self.cond_prob_bis_ = np.zeros((np.shape(X)[0],self.k_,self.k_))


        self.compute_messages(X)
        self.compute_condition_prob_matrix_(X)
        self.A_ = np.sum(self.cond_prob_bis_, axis=0) / np.sum(self.cond_prob_[1:], axis=0)
        self.pi0_ = self.cond_prob_[0]

    def fit(self, X, eps=1e-6, max_iter=10000):
        """ Find the parameters pi0_, mu_ and nu_
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
        cond_prob_ = N_ * self.pi0_
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


    def plot_pred(self, X, labels, title, plot_kwds, ax=None, figsize=FIGSIZE, cmap=CMAP, alpha=ALPHA, quantile=QUANTILE):
        """plots labeled data, centroids and confidence interval ellipses

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

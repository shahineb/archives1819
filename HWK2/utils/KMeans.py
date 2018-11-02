import numpy as np


class KMeans(object):

    def __init__(self, nr_clusters, init='random', n_init=1, max_iter=300, eps=1e-4):
        """

        Parameters
        ----------
        nr_clusters : int
        init : str
            how to initialize the centroids
        n_init : int
            number of kmeans executions to take when fitting
        max_iter : int
            max number of iterations allowed
        eps : float
            threshold for convergence

        Attributes
        ----------
        centroids_ : numpy.array
            (nr_clusters_, nr_feature)
            where nr_features depends on the dataset fed for fitting
        labels_ : numpy.array
            (nr_sample)
            cluster affected to each sample
        distorsion_: float
        inertia_: float
            difference between two successive distorsion values
        n_iter_: int
            number of iterations to reach convergence
        """
        self.nr_clusters_ = nr_clusters
        self.init_ = init
        self.n_init_ = n_init
        self.max_iter_ = max_iter
        self.eps_ = eps
        self.centroids_ = None
        self.labels_ = None
        self.distorsion_ = None
        self.inertia_ = None
        self.n_iter_ = None

    def initialize_(self, X):
        """intializes loop variables such as centroids and labels wrt
        the initialization method chosen

        Parameters
        ----------
        X : numpy.array
            (nr_sample, nr_feature)
            dataset to fit
        """
        n, p = X.shape
        up_bound = np.max(X)
        low_bound = np.min(X)

        if self.init_ == 'random':
            centroids = (up_bound - low_bound) * np.random.rand(self.nr_clusters_, p) + low_bound
        elif self.init_ == 'k-means++':
            # TODO
            pass
        else:
            raise RuntimeError("Missing intialization method")

        self.n_iter_ = 0
        labels = np.zeros(n)
        return n, p, centroids, labels

    def fit(self, X):
        """Runs n_init times kmeans clustering algorithm and keeps best
        result in terms of distorsion

        Parameters
        ----------
        X : numpy.array
            (nr_sample, nr_feature)
            dataset to fit
        """
        self.inertia_ = np.inf
        self.distorsion_ = np.inf

        for init in range(self.n_init_):

            n, p, centroids, labels = self.initialize_(X)
            conv_criterion = True

            while conv_criterion and self.n_iter_ < self.max_iter_:

                # Affect each sample to the cluster owned by the closest centroid
                distorsion = 0
                for i, x in enumerate(X):
                    dist2centroids = np.linalg.norm(x - centroids, axis=1)
                    labels[i] = np.argmin(dist2centroids)
                    distorsion += np.min(dist2centroids)

                conv_criterion = centroids

                # Recompute centroids values given new samples repartition
                for k in range(self.nr_clusters_):
                    X[np.where(labels == k)[0]]
                    centroids[k] = np.mean(X[np.where(labels == k)[0]], axis=0)

                inertia = np.linalg.norm(conv_criterion - centroids, ord=np.inf)
                conv_criterion = inertia > self.eps_
                self.n_iter_ += 1

            # if last loop performed better than previous best performer
            if distorsion < self.distorsion_:
                self.inertia_ = inertia
                self.distorsion_ = distorsion
                self.centroids_ = centroids
                self.labels_ = labels

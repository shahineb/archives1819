import numpy as np


def gen_multivariate_normal(n_sample, mean, covariance):
    """Generates dataset of length n_sample of randomly drawn multivariate normal observations

    Parameters:
    ----------
    n_sample: int
        length wished for dataset
    mean: list[numpy.array]
        list of mean vectors for multivariate normal distribution,
        vectors being of size n_feature
    covariance: list[numpy.array]
        list of covariance matrix for multivariate normal distribution,
        the matrix being of size (n_feature, n_feature)
    """
    theta = list(zip(mean, covariance))
    X = np.array([np.random.multivariate_normal(theta[idx][0], theta[idx][1]) for idx in np.random.choice(len(theta), n_sample)])
    return X


def gen_random_multivariate_normal(n_sample, n_feature, n_cluster, seed=1):
    """Generates randomly drawn dataset out of randomly generated multivariate normal distributions

    Parameters:
    ----------
    n_sample: int
        length wished for dataset
    n_feature: int
        dimension of multivariate normal law
    n_cluster: int
        number of multivariate normal distributions to consider
    seed: int
        random seed
    """

    np.random.seed(seed)

    n = n_sample
    p = n_feature
    k = n_cluster

    mean = [10 * np.random.rand() * np.random.randn(p) + 10 * (np.random.rand() - 0.5) for i in range(k)]
    foo = [10 * np.random.rand() * np.random.randn(p, p) + 10 * (np.random.rand() - 0.5)for i in range(k)]
    covariance = [np.matmul(A.T, A) for A in foo]

    X = gen_multivariate_normal(n, mean, covariance)
    return X

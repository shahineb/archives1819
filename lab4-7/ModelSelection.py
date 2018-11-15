import numpy as np
from numpy.linalg import det


def AIC(model, X):
    """Returns Akaike Information Criterion

    Parameters:
    ----------
    model : my_GMM
    X : numpy.array
        (nr_sample, nr_feature)
    """
    nr_param = model.get_number_params()
    E_log_likelihood = model.expected_log_likelihood(X)
    akaike_criterion = E_log_likelihood - nr_param
    return akaike_criterion


def BIC(model, X):
    """Returns Bayesian Information Criterion

    Parameters:
    ----------
    model : my_GMM
    X : numpy.array
        (nr_sample, nr_feature)
    """
    nr_param = model.get_number_params()
    nr_sample = len(X)
    E_log_likelihood = model.expected_log_likelihood(X)
    bayesian_criterion = E_log_likelihood - 0.5 * nr_sample * nr_param
    return bayesian_criterion


def MML(model, X):
    """Returns Minimum Message Length

    Parameters:
    ----------
    model : my_GMM
    X : numpy.array
        (nr_sample, nr_feature)
    """
    # TODO : implement minimum message Length
    pass


def posterior_correlation(model, i, j):
    """Computes posterior correlation of 2 components

    Parameters
    ----------
    model : my_GMM
    i : int
        component i
    j : int
        component j

    Returns
    -------
    correlation : float
    """
    posterior_i = model.cond_prob_[:, i]
    posterior_j = model.cond_prob_[:, j]
    correlation = np.inner(posterior_i, posterior_j) / (np.linalg.norm(posterior_i) * np.linalg.norm(posterior_j))
    return correlation


def kullback_leibler_criterion(model, i, j):
    """Computes KL-based discrimination of 2 components

    Parameters
    ----------
    model : my_GMM
    i : int
        component i
    j : int
        component j

    Returns
    -------
    B : float
    """
    # Compute sum of posteriors for components to merge
    total_posteriors_i = np.sum(model.cond_prob_[:, i])
    total_posteriors_j = np.sum(model.cond_prob_[:, j])

    # Compute merged feature parameters
    merged_pi = model.pi_[i] + model.pi_[j]
    merged_Sigma = (model.Sigma_[i] * total_posteriors_i + model.Sigma_[j] * total_posteriors_j) / (total_posteriors_i + total_posteriors_j)

    # Compute criterion
    B = 0.5 * (merged_pi * np.log(det(merged_Sigma)) - model.pi_[i] * np.log(det(model.Sigma_[i])) - model.pi_[j] * np.log(det(model.Sigma_[j])))
    return B


def merge(model, i, j, X):
    """Merges 2 components and recomputes posteriors wrt dataset

    Parameters
    ----------
    model : my_GMM
    i : int
        component i
    j : int
        component j
    X : numpy.array
        (nr_sample, nr_feature)
    Returns
    -------
    model : my_GMM
        NB : Alters model
    """
    # make sure components are sorted descending (for deletion purpose after merge)
    if i < j:
        i, j = j, i
    # Compute sum of posteriors for components to merge
    total_posteriors_i = np.sum(model.cond_prob_[:, i])
    total_posteriors_j = np.sum(model.cond_prob_[:, j])

    # Compute merged feature parameters
    merged_pi = model.pi_[i] + model.pi_[j]
    merged_mu = (model.mu_[i] * total_posteriors_i + model.mu_[j] * total_posteriors_j) / (total_posteriors_i + total_posteriors_j)
    merged_Sigma = (model.Sigma_[i] * total_posteriors_i + model.Sigma_[j] * total_posteriors_j) / (total_posteriors_i + total_posteriors_j)

    # Update model
    model.k_ = model.k_ - 1

    new_pi = np.zeros(model.k_)
    new_pi[: -1] = np.delete(model.pi_, (i, j))
    new_pi[-1] = merged_pi
    model.pi_ = new_pi

    del model.mu_[i], model.mu_[j]
    model.mu_ += [merged_mu]

    del model.Sigma_[i], model.Sigma_[j]
    model.Sigma_ += [merged_Sigma]

    model.compute_condition_prob_matrix_(X)
    return model


def run_merging(model, X, criterion, threshold):
    """Runs merging model selection

    Parameters
    ----------
    model : my_GMM
    X : numpy.array
        (nr_sample, nr_feature)
    criterion : str
        {'correlation', 'kl'}
    threshold : float
        threshold for merging
        varies wrt criterion

    Returns
    -------
    model : my_GMM
        NB : Alters model
    """
    to_merge = [None]
    while to_merge:
        to_merge = []
        for i in range(model.k_):
            for j in range(model.k_):
                if j != i:
                    if criterion == "correlation":
                        J_merge = posterior_correlation(model, i, j)
                        if J_merge >= 1 - threshold:
                            to_merge += [(i, j, J_merge)]
                    elif criterion == "kl":
                        J_merge = kullback_leibler_criterion(model, i, j)
                        if J_merge <= threshold:
                            to_merge += [(i, j, J_merge)]
                    else:
                        raise RuntimeError("Criterion not implemented")
        if to_merge:
            to_merge.sort(key=lambda x: x[2], reverse=True)
            model = merge(model, to_merge[0][0], to_merge[0][1], X)
        else:
            continue
    return model

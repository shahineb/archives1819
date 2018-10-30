import numpy as np

def bellman_operator(r, P, V, gamma):
    """Computes Bellman Operator application on V

    Parameters
    ----------
    x : int
        state index
    r : numpy.array
        reward matrix (n_states_, n_actions_)
    P : numpy.array
        transition probability matrix
        (n_states_, n_actions_, n_states_)
    V : numpy.array
        state value function vector (n_states_,)
    gamma : float
        discount factor

    Returns
    -------
    float
        bellman_operator applied to V
    """
    foo = r + gamma*np.sum(P*V, axis=2)
    max_value = np.max(foo, axis=1)
    return max_value

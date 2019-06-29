import numpy as np
from linearmab_models import LinearMABModel, ToyLinearModel, ColdStartMovieLensModel


def linearUCB(model, lambda_=1., alpha=4., T=6000, nr_simu=50):
    # Store the regret at each iteration (in a simulation)
    regret = np.zeros((nr_simu, T))
    # Store ||theta_hat - theta|| at each iteration (in a simulation)
    norm_dist = np.zeros((nr_simu, T))

    # Number of features
    d = model.n_features

    for k in range(nr_simu):

        # Initialization (the first theta_hat is null)
        A = lambda_ * np.identity(d)
        b = np.zeros(d)

        for t in range(T):

            # Estimation of theta_hat
            theta_hat = np.linalg.inv(A).dot(b)

            # Optimal arm
            a_t = model.estimate_best_arm(A, alpha, theta_hat)

            # Get the observed reward
            r_t = model.reward(a_t)

            # Update A and b
            features_a_t = model.features[a_t, :].reshape(-1, 1)
            A += features_a_t.dot(features_a_t.T)
            b += r_t * features_a_t.flatten()

            # store regret
            regret[k, t] = model.best_arm_reward() - r_t
            norm_dist[k, t] = np.linalg.norm(theta_hat - model.real_theta, 2)

    # Compute average (over sim) of the algorithm performance
    mean_regrets = np.mean(regret, axis=0)
    mean_norms = np.mean(norm_dist, axis=0)

    return mean_regrets, mean_norms


def random_policy(model, lambda_=1, T=6000, nb_simu=50):
    regret = np.zeros((nb_simu, T))
    norm_dist = np.zeros((nb_simu, T))

    n_a = model.n_actions
    d = model.n_features

    for k in range(nb_simu):

        # Initialization (the first theta_hat is null)
        A = lambda_ * np.identity(d)
        b = np.zeros(d)

        for t in range(T):

            # Estimation of theta_hat
            theta_hat = np.linalg.inv(A).dot(b)

            # Chooses a random arm
            a_t = np.random.randint(n_a)

            # Get the observed reward
            r_t = model.reward(a_t)

            # Update A and b
            features_a_t = model.features[a_t, :].reshape(-1, 1)
            A += features_a_t.dot(features_a_t.T)
            b += r_t * features_a_t.flatten()

            # Store regret
            regret[k, t] = model.best_arm_reward() - r_t
            norm_dist[k, t] = np.linalg.norm(theta_hat - model.real_theta, 2)

    # Compute average (over sim) of the algorithm performance and plot it
    mean_regrets = np.mean(regret, axis=0)
    mean_norms = np.mean(norm_dist, axis=0)

    return mean_regrets, mean_norms


def greedy_policy(model, lambda_=1, T=6000, nb_simu=50, epsilon=0.1):

    regret = np.zeros((nb_simu, T))
    norm_dist = np.zeros((nb_simu, T))

    n_a = model.n_actions
    d = model.n_features

    for k in range(nb_simu):

        # Initialization (the first theta_hat is null)
        A = lambda_ * np.identity(d)
        b = np.zeros(d)

        for t in range(T):

            # Estimation of theta_hat
            theta_hat = np.linalg.inv(A).dot(b)

            # Chooses a random arm with probability epsilon and the arm with
            # the highest score estimate with probability 1-epsilon
            p = np.random.rand()
            if p < epsilon:
                a_t = np.random.randint(n_a)
            else:
                a_t = np.argmax(np.dot(model.features, theta_hat))

            # Get the observed reward
            r_t = model.reward(a_t)

            # Update A and b
            features_a_t = model.features[a_t, :].reshape(-1, 1)
            A += features_a_t.dot(features_a_t.T)
            b += r_t * features_a_t.flatten()

            # Store regret
            regret[k, t] = model.best_arm_reward() - r_t
            norm_dist[k, t] = np.linalg.norm(theta_hat - model.real_theta, 2)

    # Compute average (over sim) of the algorithm performance and plot it
    mean_norms = np.mean(norm_dist, axis=0)
    mean_regrets = np.mean(regret, axis=0)

    return mean_regrets, mean_norms

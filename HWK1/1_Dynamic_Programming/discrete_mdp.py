import numpy as np
from utils import *

class DiscreteMDP(object):

    def __init__(self, states_names, action_names, transition_proba, reward, optimal_policy=None, gamma=0.95):
        """

        Parameters
        ----------
        states_names : list[str]
            states titles
        action_names : list[str]
            actions names
        transition_proba : numpy.array
            (n_states_, n_actions_, n_states_) numpy.array attribute
            providing for each action taken from a given state, the
            probability to move to each state
        reward : numpy.array
            (n_states, n_actions_) numpy.array providing the reward
            for each action taken from a given state
        optimal_policy : list[int]
            len = n_states_, actions to be taken in each state wrt
            guessed optimal policy
        gamma : float
            discount factor
        """

        self.states_names_ = states_names
        self.action_names_ = action_names

        self.n_states_ = len(states_names)
        self.n_actions_ = len(action_names)

        self.transition_proba_ = transition_proba
        self.reward_ = reward
        self.optimal_policy_ = optimal_policy
        self.gamma_ = gamma

        self.value_ = None
        self.policy_ = None
        self.iteration_ = None



    def reset(self, initial_policy=None):
        """
        Returns:
        ---------
            An initial state randomly drawn
        """
        initial_state = np.random.choice(np.arange(self.n_states_))
        self.value_ = np.random.randn(self.n_states_)
        self.iteration_ = 0
        if initial_policy:
            self.policy_ = initial_policy
        else:
            self.policy_ = np.random.choice(np.arange(self.n_actions_), size=self.n_states_)
        return initial_state




    def compute_optimal_policy(self):
        """returns policy maximizing state value function
        """
        foo = self.reward_ + self.gamma_*np.sum(self.transition_proba_*self.value_, axis=2)
        optimal_policy = np.argmax(foo, axis=1)
        return optimal_policy


    def update_state_value(self):
        """Updates state value function by applying to it the
        optimal Bellman operator for value iteration
        """
        self.value_ = bellman_operator(self.reward_,
                                       self.transition_proba_,
                                       self.value_,
                                       self.gamma_)


    def update_policy(self):
        """Updates state value function and policy using direct computation
        for oplicy iteration
        """
        # get indexes wrt policy to retrieve appropriate reward and
        # transition matrix
        indexes = [np.arange(self.n_states_), self.policy_]

        reward = self.reward_[indexes]
        transition_proba = self.transition_proba_[indexes]

        # Compute updated value
        foo = np.eye(self.n_states_)-self.gamma_*transition_proba
        self.value_ = np.matmul(np.linalg.inv(foo), reward)

        # Compute new policy
        self.policy_ = self.compute_optimal_policy()



    def policy_evaluation(self, policy):
        """returns state value computed for a given policy
        """
        value = np.zeros(self.n_states_)

        for state, action in enumerate(policy):
            value[state] = self.reward_[state, action]
            value[state] += self.gamma_*np.sum(self.transition_proba_[state, action]*self.value_)
        return value


    def run_value_iteration(self, eps=0.01, max_iter=10000, track=False):
        """Runs value iteration

        Parameters
        ----------
        eps : float
            Threshold of stopping criterion
        max_iter : int
            maximum number of iterations allowed in case convergence is not
            reached
        track : boolean
            if True, keeps record of state values over iteration in order
            to compute uniform distance between optimal value at each step

        Returns
        -------
        optimal_policy : list[int]
            optimal policy reached

        distance_to_optimal : list[float]
            distances between guessed optimal value and value computed at
            each iteration

        n_iter : int
        """
        state = self.reset()

        conv_criterion = True
        n_iter = 0

        if track:
            values_history = []

        while conv_criterion and n_iter < max_iter:
            n_iter += 1
            conv_criterion = self.value_

            self.update_state_value()
            self.iteration_ += 1
            conv_criterion = np.linalg.norm(conv_criterion-self.value_, ord=np.inf) > eps

            if track:
                values_history += [self.value_]

        optimal_policy = self.compute_optimal_policy() # optimal policy obtained by VI

        if track :
            optimal_value = self.policy_evaluation(self.optimal_policy_) # optimal value wrt to guessed optimal policy
            distance_to_optimal = [np.linalg.norm(x-optimal_value, ord=np.inf) for x in values_history]
            return optimal_policy, distance_to_optimal, n_iter
        else:
            return optimal_policy




    def run_policy_iteration(self, initial_policy=None, eps=0.01, max_iter=10000):
        """Runs policy iteration

        Parameters
        ----------
        eps : float
            Threshold of stopping criterion
        max_iter : int
            maximum number of iterations allowed in case convergence is not
            reached
        """

        state = self.reset(initial_policy=initial_policy)

        conv_criterion = True
        n_iter = 0

        while conv_criterion and n_iter < max_iter :
            n_iter += 1
            conv_criterion = self.value_

            self.update_policy()
            self.iteration_ += 1
            conv_criterion = np.linalg.norm(conv_criterion-self.value_, ord=np.inf) > eps
        return self.policy_

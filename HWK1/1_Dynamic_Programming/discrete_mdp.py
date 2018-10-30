import numpy as np
from utils import *

class DiscreteMDP(object):

    def __init__(self, states_names, action_names, transition_proba, reward, policy, gamma=0.95):
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
        policy : list[int]
            len = n_states_, actions to be taken in each state
        gamma : float
            discount factor
        """

        self.states_names_ = states_names
        self.action_names_ = action_names

        self.n_states_ = len(states_names)
        self.n_actions_ = len(action_names)

        self.transition_proba_ = transition_proba
        self.reward_ = reward
        self.policy_ = policy

        self.gamma_ = gamma
        self.value_ = np.random.randn(self.n_states_)



    def reset(self):
        """
        Returns:
        ---------
            An initial state randomly drawn
        """
        initial_state = np.random.choice(np.arange(self.n_states_))
        self.value_ = np.random.randn(self.n_states_)
        return initial_state


    def step(self, state, action):
        """
        Parameters
        ----------
        state : int
            index of current state
        action : int
            index of taken action

        Returns
        -------
        next_state : ini
            index of next state
        step_reward : float
            reward for step move
        """

        self.iteration_ += 1

        p_dist = self.transition_proba_[state, action]
        next_state = np.random.choice(np.arange(self.n_states_), p=p_dist)

        step_reward = self.reward_[state, action]
        # self.value_ += (self.gamma_**self.iteration_)*step_reward

        return next_state



    def next_action(self, state):
        """Returns action to take from a given state wrt policy

        Parameters
        ----------
        state : int

        Returns
        -------
        int
            action
        """
        return self.policy_[state]


    def update_state_value(self):
        """Updates state value function by applying to it the
        optimal Bellman operator
        """
        self.value_ = bellman_operator(self.reward_,
                                       self.transition_proba_,
                                       self.value_,
                                       self.gamma_)


    def get_optimal_policy(self):
        """returns policy maximizing state value function
        """
        foo = self.reward_ + self.gamma_*np.sum(self.transition_proba_*self.value_, axis=2)
        optimal_policy = np.argmax(foo, axis=1)
        return optimal_policy


    def policy_evaluation(self, policy):
        """returns state value computed for a given policy
        """
        value = np.zeros(self.n_states_)

        for state, action in enumerate(policy):
            value[state] = self.reward_[state, action]
            value[state] += self.gamma_*np.sum(self.transition_proba_[state, action]*self.value_)
        return value


    def run_value_iteration(self, eps, max_iter=10000, track=False):
        state = self.reset()

        conv_criteria = True
        n_iter = 0

        if track:
            distance = []
            optimal_value = self.policy_evaluation(self.policy_)

        while conv_criteria and n_iter < max_iter:
            n_iter += 1
            conv_criteria = self.value_

            self.update_state_value()
            conv_criteria = np.linalg.norm(conv_criteria-self.value_, ord=np.inf) > eps

            if track:
                distance += [np.linalg.norm(self.value_-optimal_value, ord=np.inf)]

        optimal_policy = self.get_optimal_policy()
        if track :
            return optimal_policy, distance, n_iter
        else:
            return optimal_policy

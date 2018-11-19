from abc import ABCMeta, abstractmethod
import numpy as np
import arms
from MAB import SMAB


class ExplorationMAB(object):
    """General class for Multi-Armed Bandit exploration algorithms
    Attributes
    ----------
    MAB_ : SMAB
        Stochastic Multi-Armed Bandit object
    T_ : int
        horizon
    draws_ : numpy.array (MAB_.nr_arms, horizon)
        Array storing arm picked at each iteration
    rewards_ : numpy.array (MAB_.nr_arms, horizon)
        Array storing reward obtained at each iteration
    """
    __metaclass__ = ABCMeta

    def __init__(self, MAB, T):
        self.MAB_ = MAB
        self.T_ = T

        self.draws_ = None
        self.rewards_ = None

    @abstractmethod
    def init_variables_(self):
        pass

    @abstractmethod
    def iterate_(self):
        pass

    @abstractmethod
    def run(self):
        # TODO : check if run be promoted to super class
        pass

    def compute_mean_regret(self, nr_simulation):
        # Get mean of best arm
        mean_max = np.max([arm.mean for arm in self.MAB_.arms_])

        # compute regret array
        all_rew = []
        for i in range(nr_simulation):
            rew, _ = self.run()
            all_rew += [rew]
        all_rew = np.array(all_rew)
        reg = mean_max * np.arange(1, self.T_ + 1) - np.mean(np.cumsum(all_rew, axis=1), axis=0)
        return reg


class NaiveExploration(ExplorationMAB):

    def __init__(self, MAB, T):
        super(NaiveExploration, self).__init__(MAB, T)
        self.empiric_mean_ = None

    def init_variables_(self):
        nr_arms = len(self.MAB_.arms_)

        # initialize loop variables at t=0
        self.draws_ = np.zeros((nr_arms, self.T_))
        self.rewards_ = np.zeros((nr_arms, self.T_))
        self.empiric_mean_ = np.zeros(nr_arms)

    def iterate(self, t):
        # Compute empirical mean
        cum_reward_t = np.sum(self.rewards_[:, :t], axis=1)
        cum_draws_t = np.sum(self.draws_[:, :t], axis=1)
        self.empiric_mean_ = cum_reward_t / cum_draws_t

        # Select maximizing arm
        arm_idx = np.argmax(self.empiric_mean_)

        # Draw chosen arm
        arm_draw = self.MAB_.arms_[arm_idx].sample()

        # Update records
        self.draws_[arm_idx, t] = 1
        self.rewards_[arm_idx, t] = arm_draw

    def run(self):
        # Initialize Bandit
        self.init_variables_()

        # Iterate
        for t in range(self.T_):
            self.iterate(t)

        # Define output sequences
        rew_sequence = np.sum(self.rewards_, axis=0)
        draws_sequence = np.argmax(self.draws_, axis=0)

        return rew_sequence, draws_sequence


class UCB1(ExplorationMAB):

    @staticmethod
    def upper_confidence_bound(t, rho, empiric_mean, cum_draws):
        """Computes upped bound of confidence interval

        Parameters
        ----------
        t : int
            nr of iteration
        rho : float
            coefficient
        empiric_mean : numpy.array (MAB_.nr_arms, )
            vector of arms empirical means
        cum_draws : numpy.array (MAB_.nr_arms, )
            vector of arms number of draws
        """
        foo = rho * np.sqrt(np.log(t) / (2 * cum_draws))
        foo = empiric_mean + foo
        return foo

    def __init__(self, MAB, T, rho):
        super(UCB1, self).__init__(MAB, T)
        self.rho_ = rho
        self.empiric_mean_ = None
        self.nr_arms_ = len(self.MAB_.arms_)

    def init_variables_(self):
        nr_arms = len(self.MAB_.arms_)

        # initialize loop variables at t=0
        self.draws_ = np.zeros((nr_arms, self.T_))
        self.rewards_ = np.zeros((nr_arms, self.T_))

        # initialize empirical mean
        for i, arm in enumerate(self.MAB_.arms_):
            arm_draw = arm.sample()
            self.rewards_[i, i] = arm_draw
            self.draws_[i, i] = 1
        self.empiric_mean_ = np.sum(self.rewards_[:, :nr_arms], axis=1)  # no need to divide by nr_draws as = 1

    def iterate(self, t):
        # Compute list of upper confidence bound values
        cum_draws = np.sum(self.draws_[:, :t], axis=1)
        upper_confidence_bounds = self.upper_confidence_bound(t, self.rho_, self.empiric_mean_, cum_draws)

        # Select maximizing arm
        arm_idx = np.argmax(upper_confidence_bounds)

        # Draw chosen arm
        arm_draw = self.MAB_.arms_[arm_idx].sample()

        # Update records
        self.draws_[arm_idx, t] = 1
        self.rewards_[arm_idx, t] = arm_draw
        cum_reward_arm = np.sum(self.rewards_[arm_idx, :t + 1], axis=0)
        cum_draws_arm = np.sum(self.draws_[arm_idx, :t + 1], axis=0)
        self.empiric_mean_[arm_idx] = cum_reward_arm / cum_draws_arm

    def run(self):
        # Initialize Bandit
        self.init_variables_()

        # Iterate
        for t in range(self.nr_arms_, self.T_):
            self.iterate(t)

        # Define output sequences
        rew_sequence = np.sum(self.rewards_, axis=0)
        draws_sequence = np.argmax(self.draws_, axis=0)

        return rew_sequence, draws_sequence


class ThompsonSampling(ExplorationMAB):

    @staticmethod
    def get_bernoulli_posteriors(cum_draws, cum_rewards):
        """Computes posteriors of an arm for
        bernoulli-beta posterior

        Parameters
        ----------
        cum_draws : int
            cumulative nr of draws for the arm
        cum_rewards : float
            cumulative reward for the arm
        """
        a = cum_rewards + 1
        b = cum_draws - cum_rewards + 1
        posterior = np.random.beta(a, b)
        return posterior

    def __init__(self, MAB, T):
        super(ThompsonSampling, self).__init__(MAB, T)
        self.nr_arms_ = len(self.MAB_.arms_)

    def init_variables_(self):
        nr_arms = len(self.MAB_.arms_)
        # initialize loop variables at t=0
        self.draws_ = np.zeros((nr_arms, self.T_))
        self.rewards_ = np.zeros((nr_arms, self.T_))

    def get_arm_posterior_(self, arm_idx, t):
        cum_reward_t = np.sum(self.rewards_[arm_idx, :t])
        cum_draws_t = np.sum(self.draws_[arm_idx, :t])
        posterior = self.get_bernoulli_posteriors(cum_draws_t, cum_reward_t)
        return posterior

    def sample_reward_(self, arm_idx):
        if isinstance(self.MAB_.arms_[arm_idx], arms.ArmBernoulli):
            arm_draw = self.MAB_.arms_[arm_idx].sample()
        else:
            rew_observed = self.MAB_.arms_[arm_idx].sample()
            try:
                arm_draw = np.random.binomial(1, rew_observed)
            except ValueError:
                raise ValueError("Distribution support exceeds [0,1]")
        return arm_draw

    def iterate(self, t):
        # Compute posteriors
        posteriors = np.array([self.get_arm_posterior_(i, t) for i in range(self.nr_arms_)])

        # Select maximizing arm
        arm_idx = np.argmax(posteriors)

        # Draw chosen arm
        arm_draw = self.sample_reward_(arm_idx)

        # Update records
        self.draws_[arm_idx, t] = 1
        self.rewards_[arm_idx, t] = arm_draw

    def run(self):
        # Initialize Bandit
        self.init_variables_()

        # Iterate
        for t in range(self.T_):
            self.iterate(t)

        # Define output sequences
        rew_sequence = np.sum(self.rewards_, axis=0)
        draws_sequence = np.argmax(self.draws_, axis=0)

        return rew_sequence, draws_sequence

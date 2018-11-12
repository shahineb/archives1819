import numpy as np
import arms


class SMAB(object):
    """Stochastic Multi-Armed Bandit

    Parameters
    ----------
    arms : list[AbstractArm]
        Bandit's arm-set
    """

    def __init__(self, arms):
        self.arms_ = arms

    def get_arm(self, arm_index):
        try:
            return self.arms_[arm_index]
        except IndexError:
            raise IndexError("Unexisting arm")


class BernoulliBandit(SMAB):
    """Bernoulli Bandit

    Parameters
    ----------
    nr_arms : int
        Number of arms
    seed : int
        seed for reproducibility
    """

    def __init__(self, nr_arms, seed):
        """Initializes randomly Bernoulli arms given the number of arm
        """
        self.nr_arms_ = nr_arms
        self.seed_ = seed

        np.random.seed(self.seed_)
        bernoulli_param = [np.random.rand() for i in range(self.nr_arms_)]
        random_seed = [np.random.randint(1, 312414) for i in range(self.nr_arms_)]
        arms_ = [arms.ArmBernoulli(p=p, random_state=seed) for (p, self.seed_) in zip(bernoulli_param, random_seed)]
        super(BernoulliBandit, self).__init__(arms_)

    def get_arm(self, arm_index):
        try:
            return self.arms_[arm_index]
        except IndexError:
            raise IndexError("Unexisting arm")

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
        self.nr_arms_ = len(arms)

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

    def complexity(self):
        # Get mean of best arm
        arms_means = np.array([arm.mean for arm in self.arms_])
        max_arm_idx = np.argmax(arms_means)
        mean_max = self.arms_[max_arm_idx].mean

        # Compute complexity
        other_means = np.delete(arms_means, max_arm_idx)
        kl_div = other_means * np.log(other_means / mean_max) + (1 - other_means) * np.log((1 - other_means) / (1 - mean_max))
        C = np.sum((mean_max - other_means) / kl_div)
        return C

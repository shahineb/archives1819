from abc import ABCMeta, abstractmethod
import numpy as np
import arms


class SMAB(object):
    __metaclass__ = ABCMeta

    def __init__(self, nr_arm, seed):
        self.nr_arm_ = nr_arm
        self.seed_ = seed

    @abstractmethod
    def init_variables_(self):
        pass

    @abstractmethod
    def iterate_(self):
        pass

    @abstractmethod
    def run(self, horizon):
        pass


class Bernoulli_SMAP(SMAB):
    __metaclass__ = ABCMeta

    def __init__(self, nr_arm, seed):
        super(SMAB, self).__init__(nr_arm, seed)

        np.random.seed(self.seed_)
        bernoulli_param = [np.random.rand() for i in range(self.nr_arm_)]
        random_seed = [np.random.randint(1, 312414) for i in range(self.nr_arm_)]
        self.arms_ = [arms.ArmBernoulli(p=p, random_state=seed) for (p, self.seed_) in zip(bernoulli_param, random_seed)]

        self.draws_ = None
        self.rewards_ = None

        self.cum_rewards_ = None
        self.cum_draws_ = None

    def init_variables_(self):
        self.draws_ = []
        self.rewards_ = []

        for i, arm in enumerate(self.arms_):
            arm_draw = arm.sample()
            self.rewards_ += [arm_draw]
            self.draws_ += [i]

        self.cum_rewards_ = np.array(self.nr_arm_)
        self.cum_draws_ = np.ones(self.nr_arm_)

    def iterate_(self)

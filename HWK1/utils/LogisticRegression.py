from RegressionModel import RegressionModel, FIGSIZE, COLORS, MARKERS
from scipy.stats import  logistic
import matplotlib.pyplot as plt
import numpy as np


class LogisticRegression(RegressionModel):
    @staticmethod
    def log_likelihood(eta,X,y):
        l_w = np.sum(y*np.log(eta)) + np.sum((1-y)*np.log(1-eta))
        return l_w
    @staticmethod
    def grad_log_likelihood(eta,X,y):
        nabla_l_w = np.matmul(X.T,y-eta)
        return nabla_l_w
    @staticmethod
    def hess_log_likelihood(eta,X):
        diag_eta = np.diag(eta*(1-eta))
        Hl_w = -np.matmul(np.matmul(X.T, diag_eta),X)
        return Hl_w
    @staticmethod
    def augment_matrix(X):
        num_samples, num_features = X.shape
        X_aug = np.hstack([np.ones((num_samples, 1)), X])
        return X_aug

    def __init__(self):
        self.w_ = None
        self.eta_ = None

    def init_params_(self, X):
        num_samples, num_features = X.shape
        X = np.hstack([np.ones((num_samples, 1)), X])
        self.w_ = np.random.randn(num_features+1)
        self.eta_ = logistic.cdf(np.matmul(X,self.w_))
        return X, num_features


    def fit(self, X, y, beta=0.5, max_iter=400, eps=10e-6):
        X, num_features = self.init_params_(X)

        n_iter = 0
        conv_criterion = True

        l_w = LogisticRegression.log_likelihood(self.eta_, X, y)+beta*np.inner(self.w_, self.w_)/2

        while conv_criterion and n_iter < max_iter:
            nabla_l_w = LogisticRegression.grad_log_likelihood(self.eta_, X, y)+beta*self.w_
            Hl_w = LogisticRegression.hess_log_likelihood(self.eta_, X) + beta*np.eye(num_features+1)
            inv_Hl_w = np.linalg.inv(Hl_w)
            self.w_ = self.w_ - np.matmul(inv_Hl_w,nabla_l_w)

            n_iter +=1
            conv_criterion = l_w
            self.eta_ = logistic.cdf(np.matmul(X,self.w_))
            l_w = LogisticRegression.log_likelihood(self.eta_, X, y)+beta*np.inner(self.w_, self.w_)/2
            det_H = np.linalg.det(Hl_w)
            conv_criterion = (np.abs(conv_criterion-l_w)>eps) and (np.abs(det_H)>eps)

    def predict_proba(self, X):
        try :
            X = LogisticRegression.augment_matrix(X)
            proba_y = logistic.cdf(np.matmul(X,self.w_))
            return proba_y
        except TypeError:
            raise RuntimeError("Unfitted model")

    def missclassification(self, X, y):
        return super(LogisticRegression, self).missclassification(X, y)

    def predict(self, X):
        y_pred = self.predict_proba(X)
        y_pred[y_pred>0.5] = 1
        y_pred[y_pred!=1] = 0
        return y_pred

    def plot_pred(self, X, y, title="", figsize=FIGSIZE):
        fig, ax = plt.subplots(figsize=figsize)
        X_0 = X[y==0]
        X_1 = X[y==1]
        ax.scatter(*X_0.T, marker=MARKERS[0], label = r"$label=0$")
        ax.scatter(*X_1.T, marker=MARKERS[1], label = r"$label=1$")

        x1_axis = np.linspace(*ax.get_xlim())
        x2_axis = np.linspace(*ax.get_ylim())
        granularity = len(x1_axis)
        x1_grid, x2_grid = np.meshgrid(x1_axis, x2_axis)
        x_1_2 = np.vstack([x1_grid.reshape(-1), x2_grid.reshape(-1)]).T

        z = self.w_[0]*x1_grid + self.w_[1]*x2_grid
        z = z.reshape(granularity,granularity)
        ax.contourf(x1_axis, x2_axis, -z, levels=[0,np.inf], colors=COLORS[0], linestyles="dashed", alpha=0.05)
        ax.contourf(x1_axis, x2_axis, z, levels=[0,np.inf], colors=COLORS[1], linestyles="dashed", alpha=0.05)

        ax.grid(alpha=0.3)
        ax.set_title(title, fontsize=18)
        plt.tight_layout()
        plt.legend(fontsize=14)
        return ax

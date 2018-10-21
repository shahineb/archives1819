from GenerativeModel import GenerativeModel, FIGSIZE, COLORS, MARKERS
from scipy.stats import  multivariate_normal
import matplotlib.pyplot as plt
import numpy as np

class QDA(GenerativeModel):
    def __init__(self):
        super(QDA, self).__init__()

    def fit(self, X, y):
        self.pi_ = np.mean(y)
        X_0 = X[y==0]
        X_1 = X[y==1]
        mu_hat_0 = np.mean(X_0, axis=0)
        mu_hat_1 = np.mean(X_1, axis=0)
        self.mu_ = [mu_hat_0, mu_hat_1]
        X_centered_0 = X_0-self.mu_[0]
        X_centered_1 = X_1-self.mu_[1]
        sigma_hat_0 = np.matmul(X_centered_0.T, X_centered_0)/len(X_centered_0)
        sigma_hat_1 = np.matmul(X_centered_1.T, X_centered_1)/len(X_centered_1)
        self.sigma_ = [sigma_hat_0, sigma_hat_1]

    def predict_proba(self, X):
        try:
            multivariate_normal_ = [multivariate_normal(mu, sigma) for mu, sigma in zip(self.mu_, self.sigma_)]
            total_proba = (1-self.pi_)*multivariate_normal_[0].pdf(X) + self.pi_*multivariate_normal_[1].pdf(X)
            pred_proba = self.pi_*multivariate_normal_[1].pdf(X)/total_proba
            return pred_proba
        except TypeError:
            raise RuntimeError("Unfitted model")

    def predict(self, X):
        return super(QDA, self).predict(X)

    def missclassification(self, X, y):
        return super(QDA, self).missclassification(X, y)

    def plot_pred(self, X, y, title, figsize=(10,8)):
        fig, ax = plt.subplots(figsize=figsize)
        X_0 = X[y==0]
        X_1 = X[y==1]
        ax.scatter(*X_0.T, marker=MARKERS[0], color = COLORS[0], label = r"$label=0$")
        ax.scatter(*X_1.T, marker=MARKERS[1], color = COLORS[1], label = r"$label=1$")

        sigma_inv = [np.linalg.inv(sigma) for sigma in self.sigma_]

        x1_axis = np.linspace(*ax.get_xlim())
        x2_axis = np.linspace(*ax.get_ylim())
        granularity = len(x1_axis)
        x1_grid, x2_grid = np.meshgrid(x1_axis, x2_axis)
        x_1_2 = np.vstack([x1_grid.reshape(-1), x2_grid.reshape(-1)]).T

        foo = [-0.5*np.log(np.linalg.det(sigma))-0.5*np.diagonal(np.matmul(x_1_2-mu, np.matmul(sigma, (x_1_2-mu).T))) for mu, sigma in zip(self.mu_, sigma_inv)]
        z = foo[0]-foo[1]-np.log((1-self.pi_)/self.pi_)
        z = z.reshape(granularity,granularity)
        ax.contourf(x1_axis, x2_axis, z, levels=[0,np.inf], colors=COLORS[0], linestyles="dashed", alpha=0.07)
        ax.contourf(x1_axis, x2_axis, -z, levels=[0,np.inf], colors=COLORS[1], linestyles="dashed", alpha=0.07)

        ax.grid(alpha=0.3)
        ax.set_title(title, fontsize=18)
        plt.tight_layout()
        plt.legend(fontsize=14)
        return ax

from GenerativeModel import GenerativeModel, FIGSIZE, COLORS, MARKERS
from scipy.stats import  multivariate_normal
import matplotlib.pyplot as plt
import numpy as np

class LDA(GenerativeModel):
    def __init__(self):
        super(LDA, self).__init__()

    def fit(self, X, y):
        self.pi_ = np.mean(y)
        X_0 = X[y==0]
        X_1 = X[y==1]
        mu_hat_0 = np.mean(X_0, axis=0)
        mu_hat_1 = np.mean(X_1, axis=0)
        self.mu_ = [mu_hat_0, mu_hat_1]
        X_centered = np.concatenate([X_0-self.mu_[0], X_1-self.mu_[1]])
        self.sigma_ = np.matmul(X_centered.T, X_centered)/len(X_centered)

    def predict_proba(self, X):
        try:
            multivariate_normal_ = [multivariate_normal(mu, self.sigma_) for mu in self.mu_]
            proba_x = (1-self.pi_)*multivariate_normal_[0].pdf(X) + self.pi_*multivariate_normal_[1].pdf(X)
            pred_proba = self.pi_*multivariate_normal_[1].pdf(X)/proba_x
            return pred_proba
        except TypeError:
            raise RuntimeError("Unfitted model")

    def predict(self, X):
        return super(LDA, self).predict(X)

    def missclassification(self, X, y):
        return super(LDA, self).missclassification(X, y)

    def plot_pred(self, X, y, title, figsize=(10,8)):
        fig, ax = plt.subplots(figsize=figsize)
        X_0 = X[y==0]
        X_1 = X[y==1]
        ax.scatter(*X_0.T, marker=MARKERS[0], color = COLORS[0], label = r"$label=0$")
        ax.scatter(*X_1.T, marker=MARKERS[1], color = COLORS[1], label = r"$label=1$")

        sigma_inv = np.linalg.inv(self.sigma_)
        orthogonal_vec = np.matmul(sigma_inv, self.mu_[1]-self.mu_[0])

        x1_axis = np.linspace(*ax.get_xlim())
        x2_axis = np.linspace(*ax.get_ylim())
        granularity = len(x1_axis)
        x1_grid, x2_grid = np.meshgrid(x1_axis, x2_axis)
        x_1_2 = np.vstack([x1_grid.reshape(-1), x2_grid.reshape(-1)]).T

        z = orthogonal_vec[0]*x1_grid + orthogonal_vec[1]*x2_grid
        z = z.reshape(granularity,granularity)
        ax.contourf(x1_axis, x2_axis, -z, levels=[0,np.inf], colors=COLORS[0], linestyles="dashed", alpha=0.1)
        ax.contourf(x1_axis, x2_axis, z, levels=[0,np.inf], colors=COLORS[1], linestyles="dashed", alpha=0.1)

        ax.grid(alpha=0.3)
        ax.set_title(title, fontsize=18)
        plt.tight_layout()
        plt.legend(fontsize=14)
        return ax

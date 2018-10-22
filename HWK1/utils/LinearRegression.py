from RegressionModel import RegressionModel, FIGSIZE, COLORS, MARKERS
from scipy.stats import  logistic
import matplotlib.pyplot as plt
import numpy as np

class LinearRegression(RegressionModel):

    def __init__(self):
        self.w_=None
        self.sigma_=None

    def init_params_(self, X):
        num_samples, num_features = X.shape
        X = np.hstack([np.ones((num_samples, 1)), X])
        self.w_ = np.random.randn(num_features+1)
        return X


    def fit(self, X, y):
        X = self.init_params_(X)
        XT_X = np.matmul(X.T, X)
        try :
            XT_X_inv = np.linalg.inv(XT_X)
            XT_X_inv_XT = np.matmul(XT_X_inv, X.T)
            self.w_ = np.matmul(XT_X_inv_XT, y)
        except np.linalg.LinAlgError :
            raise np.linalg.LinAlgError("X not invertible")
        self.sigma_ = np.mean((y-np.matmul(X, self.w_))**2)

    def predict_proba(self, X):
        try :
            X = RegressionModel.augment_matrix(X)
            proba_y = np.matmul(X,self.w_)
            return proba_y
        except TypeError:
            raise RuntimeError("Unfitted model")


    def predict(self, X):
        return super(LinearRegression, self).predict(X)

    def missclassification(self, X, y):
        return super(LinearRegression, self).missclassification(X, y)

    def plot_pred(self, X, y, title="", figsize=FIGSIZE, ax=None):
        if not ax:
            fig, ax = plt.subplots(figsize=figsize)
        X_0 = X[y==0]
        X_1 = X[y==1]
        ax.scatter(*X_0.T, marker='o', label = r"$label=0$")
        ax.scatter(*X_1.T, marker='x', label = r"$label=1$")

        x1_axis = np.linspace(*ax.get_xlim())
        x2_axis = np.linspace(*ax.get_ylim())
        granularity = len(x1_axis)
        x1_grid, x2_grid = np.meshgrid(x1_axis, x2_axis)
        x_1_2 = np.vstack([x1_grid.reshape(-1), x2_grid.reshape(-1)]).T

        z = self.w_[0]*x1_grid + self.w_[1]*x2_grid-0.5
        z = z.reshape(granularity,granularity)

        ax.contourf(x1_axis, x2_axis, z, levels=[0,np.inf], colors="steelblue", linestyles="dashed", alpha=0.1)
        ax.contourf(x1_axis, x2_axis, -z, levels=[0,np.inf], colors="sandybrown", linestyles="dashed", alpha=0.1)

        ax.grid(alpha=0.3)
        ax.set_title(title, fontsize=18)
        plt.tight_layout()
        plt.legend(fontsize=14)
        return ax

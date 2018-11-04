import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.KMeans import KMeans
from utils.IsotropicGM import IsotropicGM
from utils.GaussianMixtureModel import GaussianMixtureModel, FIGSIZE
import warnings

warnings.filterwarnings("ignore")

plt.style.use('seaborn-notebook')
plot_kwds = {'alpha': 0.5, 's': 80, 'linewidths': 0}


train = pd.read_table("data/EMGaussian.data", sep=" ", header=None)
test = pd.read_table("data/EMGaussian.test", sep=" ", header=None)
train = train.values
test = test.values


# KMeans
n_row = 2
n_col = 3
seed = [1, 3, 7, 13, 17, 37]

fig, ax = plt.subplots(n_row, n_col, figsize=(18, 12))

for i in range(n_row):
    for j in range(n_col):
        np.random.seed(seed[n_col * i + j])
        kmeans = KMeans(nr_clusters=4, n_init=1)
        kmeans.fit(train)
        ax[i][j].scatter(*train.T, c=kmeans.labels_, cmap='Dark2', **plot_kwds)
        ax[i][j].scatter(*kmeans.centroids_.T, marker='p', s=150, color="crimson")
        distortion = str(round(kmeans.distorsion_, 3))
        nr_iterations = str(kmeans.n_iter_)
        ax[i][j].set_title(r"$J = $" + distortion + " | " + nr_iterations + " iterations", size=16)
        ax[i][j].grid(alpha=0.3)
plt.tight_layout()
plt.savefig("docs/img/kmeans.png")
plt.close()


# Iso GMM
iso_gmm = IsotropicGM(k=4, initialization="kmeans")
iso_gmm.fit(train)
fig, ax = plt.subplots(figsize=FIGSIZE)

title = "Training set | Isotropic MM with 90% confidence interval"
iso_gmm.plot_pred(X=train,
                  labels=iso_gmm.labels_,
                  title=title,
                  plot_kwds=plot_kwds,
                  ax=ax)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig("docs/img/3_b_isotropic_gm.png")
plt.close()


# GMM
gmm = GaussianMixtureModel(k=4, initialization="kmeans")
gmm.fit(train)

fig, ax = plt.subplots(figsize=FIGSIZE)

title = "Training set | GMM with 90% confidence interval"
gmm.plot_pred(X=train,
              labels=gmm.labels_,
              title=title,
              plot_kwds=plot_kwds,
              ax=ax)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig("docs/img/3_c_gmm.png")
plt.close()

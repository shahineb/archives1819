#!!~/anaconda/bin python
# -*- coding: utf-8 -*-
"""util.py
 utility functions for tp2&3.ipynb
 """

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def mat_to_mapping(mat, eps=1e-4):
    """Generates mapping out of float array
    If values lower than eps, value is set to 0
    Else set to 1

    Parameters
    ----------
    mat : numpy.array
        matrix of float values
    eps : float
        set to 0 threshold

    Returns
    -------
    numpy.array
        mapping matrix
    """
    n,p = mat.shape
    for i in range(n):
        for j in range(p):
            if mat[i,j] < eps:
                mat[i,j] = 0
            else :
                mat[i,j] = 1
    return mat

def plot_objet_casier(position_objet, position_casier, attribution, figsize=(20,12)):
    """Plots objet-casier mapping in R^2 plan

    Parameters
    ----------
    position_objet : numpy.array
        Objets' coordinates
    position_casier : numpy.array
        Casiers' coordinates
    attribution : numpy.array
        Mapping matrix
    figsize : tuple

    Returns
    -------
    None
    """
    n = len(position_objet)

    fig, ax = plt.subplots(1, figsize=figsize)

    labels_objets = [r"$O_{" + str(i)  + r"}$"for i in range(1, n+1)]
    plt.scatter(position_objet[:,0],position_objet[:,1] , color="tomato")

    labels_casier = [r"$B_{" + str(i)  + r"}$" for i in range(1, n+1)]
    plt.scatter(position_casier[:,0],position_casier[:,1] , color="c")

    for i in range(n):
        ax.annotate(labels_objets[i], (position_objet[i,0], position_objet[i,1]), fontsize=14)
        ax.annotate(labels_casier[i], (position_casier[i,0], position_casier[i,1]), fontsize=12)

        j = np.where(attribution[:,i]==1.)[0][0]
        plt.plot((position_casier[j,0], position_objet[i,0]),
                 (position_casier[j,1], position_objet[i,1]),
                 '--',
                 c='dimgrey',
                 label=r"$O_{" + str(i+1) + r"}\rightarrow B_{" + str(j+1) + r"}$")

    plt.legend(fontsize=15, loc='lower left')
    plt.show()

#!!~/anaconda/bin python
# -*- coding: utf-8 -*-
"""util_2.py
 utility functions for 2_2_optimisation_combinatoire.ipynb
 """

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph_mat, to_highlight=None, figsize=(16,12)):
    """Plots undirected weighted graph infered by input matrix

    Parameters
    ----------
    graph_mat : numpy.array
        graph_mat[i][j] represents weight of the edge between i and j
        if 0, then no edge
    to_highlight : list
        list of nodes to highlight on the plot

    Returns
    -------
    None

    """
    G = nx.DiGraph()
    plt.figure(figsize=figsize)
    for i, row in enumerate(graph_mat):
        spy_i = str(i+1)
        reachable_spies = np.where(row>0)[0]
        for j in reachable_spies:
            spy_j = str(j+1)
            G.add_edges_from({(spy_i,spy_j)}, weight=round(row[j],3))

    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

    if to_highlight:
        edge_colors = ['dimgrey' if not edge in to_highlight else 'red' for edge in G.edges()]
    else:
        edge_colors = ['dimgrey' for edge in G.edges()]

    pos=nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G,pos, node_size=800, node_color = 'salmon', edge_color=edge_colors)
    nx.draw_networkx_labels(G,pos)
    

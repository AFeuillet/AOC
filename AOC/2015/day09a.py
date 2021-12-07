import re
import numpy as np

import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall, shortest_path

def get_path(Pr, i, j):
    path = [j]
    k = j
    while Pr[i, k] != -9999:
        path.append(Pr[i, k])
        k = Pr[i, k]
    return path[::-1]

nfile = open('data/daytmp.txt', 'r')
nbl = nfile.read().split('\n')

G = [[0, 518, 464],
[0, 0, 141],
[0, 0, 0]]

G_eparse = csr_matrix(G)
dist_matrix, p = floyd_warshall ( csgraph = G_eparse, directed = True,
return_predecessors = True )
print(dist_matrix)
print(p)
D, Pr = shortest_path(G, directed=False, method='FW', return_predecessors=True)
print(D)
print(Pr)

print(get_path(Pr, 0,2))
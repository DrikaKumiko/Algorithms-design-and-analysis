# Algorithms - design and analysis (Stanford), Part II.
# Programming Assignment 1-2: Prim's MST

import random
import sys

infinity = sys.maxint

def prim(graph_adj_list):
    # Naive O(mn) version.
    # TODO: heap-based O(m*log(n)) version.
    
    n = len(graph_adj_list)
    MST = set()
    X = set()
    in_MST = [False for _ in xrange(n)]
    
    s = random.randint(0, n-1)
    X.add(s)
    in_MST[s] = True
    
    
    while len(X) < n:
        cheapest_edge = (-1, -1, infinity)
        for v1 in X:
            for (v1, v2, w) in graph_adj_list[v1]:
                if not in_MST[v2] and w < cheapest_edge[2]:
                    cheapest_edge = (v1, v2, w)
        X.add(cheapest_edge[1])
        in_MST[cheapest_edge[1]] = True
        MST.add(cheapest_edge)
        
    return MST
    
    
def main():
    
    f = open('edges.txt')
    
    n, m = [int(x) for x in f.readline().split()]
    graph_adj_list = [[] for _ in xrange(n)]
    for line in f:
        v1, v2, w = [int(x) for x in line.split()]
        graph_adj_list[v1-1].append((v1-1, v2-1, w))
        graph_adj_list[v2-1].append((v2-1, v1-1, w))
        
    tree_edges = prim(graph_adj_list)
    
    cost = sum([w for (_, _, w) in tree_edges])

    print 'MST cost = %i' % cost

main()

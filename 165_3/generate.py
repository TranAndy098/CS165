import math
import random
from graph import Graph

import time

def erdos_old(n):
    edges = set()
    p = 2 * (math.log(n)) / n
    picks = [0,1]
    probability = [1-p, p]

    for v in range(n):
        for w in range(v+1, n):
            r = random.choices(picks, probability)[0]
            if r == 1:
                edges.add((v, w))
    
    return Graph(n,edges)

def erdos(n):
    edges = set()
    p = 2 * (math.log(n)) / n
    v = 1
    w = -1

    while v < n:
        r = random.random()

        w += 1 + math.floor(math.log2(1-r)/math.log2(1-p))
        while w >= v and v < n:
            w -= v
            v += 1
        if v < n:
            edges.add((v, w))

    return Graph(n,edges)


def barabasi(n):
    pass



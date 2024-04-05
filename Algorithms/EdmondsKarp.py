from Builder.GraphCreator import Graph, NodeWColor, Node, FlowGraph
from Algorithms.BFS import BFS
from sys import gettrace

def capacity(Nf: FlowGraph, u: Node, v: Node):
    return Nf.c[(u, v)]

def check_exists_path(Nf: FlowGraph):
    path = get_path(Nf)
    if (len(path) == 0) or (Nf.s not in [x[0] for x in path]):
        return False
    else:
        return True

def get_path(Nf: FlowGraph):
    BFS(g=Nf.N, s=Nf.s)
    path = []
    t = Nf.t
    s = Nf.s
    while (t != s) and (t.pie is not None):
        path.append((t.pie, t))
        t = t.pie
    return path[::-1]

def get_minimum_capacity(Nf: FlowGraph, path):
    min_value = float('inf')
    for u, v in path:
        min_value = min(capacity(Nf, u, v), min_value)
    return min_value

def Edmonds_Karp(G: Graph, s: Node, t: Node, c=capacity):
    Nf = FlowGraph()
    for u, v in G.get_all_lines():
        Nf.f[(u, v)] = 0
        Nf.f[(v, u)] = 0
    Nf.copy(N=G, s=s, t=t)
    while check_exists_path(Nf):
        p = get_path(Nf)
        CfP = get_minimum_capacity(Nf, p)
        for u, v in p:
            Nf.f[(u, v)] = Nf.f[(u, v)] + CfP
            Nf.f[(v, u)] = Nf.f[(u, v)] * (-1)
            Nf.c[(u, v)] = Nf.c[(u, v)] - CfP
            Nf.c[(v, u)] = Nf.c[(v, u)] + CfP
        Nf.update_removed_edges()
        if gettrace() is not None:
            Nf.N.display()
    return Nf.f

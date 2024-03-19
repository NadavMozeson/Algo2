from Builder.GraphCreator import Graph, Node
from Classes.MinHeap import MinHeap


def weight_function(u: Node, v: Node):
    return u.adjacent_nodes[v]


def Relax(u, v, w):
    if v.d > u.d + w(u, v):
        v.d = u.d + w(u, v)
        v.pie = u


def Initialize_single_source(G: Graph, s: Node):
    for u in G.nodes:
        u.d = float('inf')
        u.pie = None
    s.d = 0


def Bellman_Ford(G: Graph, s: Node, w=weight_function):
    Initialize_single_source(G, s)
    for i in range(len(G.nodes) - 1):
        for u, v in G.get_all_lines():
            Relax(u, v, w(u, v))
    for u, v in G.get_all_lines():
        if v.d > u.d + w(u, v):
            return False
    return True

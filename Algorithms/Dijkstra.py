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


def Dijkstra(G: Graph, s: Node, w=weight_function):
    Initialize_single_source(G, s)
    T = set()
    Q = MinHeap(G.nodes.copy())
    while not Q.is_empty():
        u = Q.extract_min()
        T.add(u)
        for v in u.adjacent_nodes.keys():
            Relax(u, v, w)

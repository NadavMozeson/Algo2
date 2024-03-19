from Builder.GraphCreator import Graph, Node
from Classes.MinHeap import MinHeap


def Prim(G: Graph, r: Node):
    for u in G.nodes:
        u.pie = None
        u.d = float('inf')
    r.d = 0
    Q = MinHeap(G.nodes.copy())
    while not Q.is_empty():
        u = Q.extract_min()
        for v in u.adjacent_nodes.keys():
            if (Q.value_exists(v)) and (w(u, v) < v.d):
                v.pie = u
                v.d = w(u, v)

def w(u: Node, v: Node):
    return u.adjacent_nodes[v]

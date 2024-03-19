from Builder.GraphCreator import Graph, Node
from Classes.MinHeap import MinHeap

def weight_function(u: Node, v: Node):
    return u.adjacent_nodes[v]

def Prim(G: Graph, r: Node, w=weight_function):
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

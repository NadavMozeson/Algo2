from Builder.GraphCreator import Graph, Node
from Classes.MinHeap import MinHeap

def Relax(u, v, weight):
    if v.d > u.d + weight:
        v.d = u.d + weight
        v.pie = u

def Initialize_single_source(G: Graph, s: Node):
    for u in G.nodes:
        u.d = float('inf')
        u.pie = None
    s.d = 0

def Bellman_Ford(G: Graph, s: Node):
    Initialize_single_source(G, s)
    for i in range(len(G.nodes)-1):
        for u, v in G.get_all_lines():
            Relax(u, v, u.adjacent_nodes[v])
    for u, v in G.get_all_lines():
        if v.d > u.d + u.adjacent_nodes[v]:
            return False
    return True

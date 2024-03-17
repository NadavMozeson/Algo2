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

def Dijkstra(G: Graph, s: Node):
    Initialize_single_source(G, s)
    T = set()
    Q = MinHeap(G.nodes.copy())
    while not Q.is_empty():
        u = Q.extract_min()
        T.add(u)
        for v, weight in u.adjacent_nodes.items():
            Relax(u, v, weight)

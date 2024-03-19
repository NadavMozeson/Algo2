from Builder.GraphCreator import Graph, Node
from Algorithms.TopologicSort import topologic_sort


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


def DAG_Shortest_Path(G: Graph, s: Node, w=weight_function):
    topological_sort = topologic_sort(G)
    Initialize_single_source(G, s)
    for u in topological_sort:
        for v in u.adjacent_nodes.keys():
            Relax(u, v, w)

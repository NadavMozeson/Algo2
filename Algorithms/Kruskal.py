from Builder.GraphCreator import Graph, Node
from Classes.DDS import *


def weight_function(u: Node, v: Node):
    return u.adjacent_nodes[v]


def Kruskal(G: Graph, w=weight_function):
    dds = DDS()
    A = Graph(NodeClass=Node)
    for v in G.nodes:
        dds.make_set(v)
        A.add_node(v.label)
    E = get_sorted_edges(G, w)
    for u, v in E:
        x = dds.find(u)
        y = dds.find(v)
        if x != y:
            dds.merge(x, y)
            A.add_line(u.label, v.label)
    return A


def get_sorted_edges(G: Graph, w):
    return sorted(G.get_all_lines(), key=lambda tup: w(tup[0], tup[1]))

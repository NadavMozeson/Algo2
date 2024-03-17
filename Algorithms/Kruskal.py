from Builder.GraphCreator import Graph, Node
from Classes.DDS import *

def Kruskal(G: Graph):
    dds = DDS()
    A = Graph(NodeClass=Node)
    for v in G.nodes:
        dds.make_set(v)
        A.add_node(v.label)
    E = get_sorted_edges(G)
    for u, v in E:
        x = dds.find(u)
        y = dds.find(v)
        if x != y:
            dds.merge(x, y)
            A.add_line(u.label, v.label)
    return A


def get_sorted_edges(G: Graph):
    def get_weight_for_second_element(tup):
        return tup[0].adjacent_nodes[tup[1]]
    return sorted(G.get_all_lines(), key=get_weight_for_second_element)

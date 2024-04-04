from Builder.GraphCreator import Graph, Node

def capacity(u: Node, v: Node):
    return u.adjacent_nodes[v] if v in u.adjacent_nodes.keys() else 0

def create_flow_graph(G: Graph):
    F = Graph(directed=True, weighted=True, NodeClass=Node)
    for u in G.nodes:
        F.add_node(u.label)
    return F

def Ford_Flukerson(G: Graph, s: Node, t: Node, c=capacity):
    f = create_flow_graph(G)
    for u, v in G.get_all_lines():
        f.add_line(u.label, v.label, 0)
        f.add_line(v.label, u.label, 0)

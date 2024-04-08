from Builder.GraphCreator import Graph, Node
from Algorithms.TopologicSort import topologic_sort
from Classes.DDS import DDS

time = 0


def KosarajuSharir(G: Graph):
    set_nodes_white(G)
    stack = []
    for v in G.nodes:
        if v.color == "White":
            DFS_VISIT(v, stack)

    transposed_graph = transpose_graph(G)
    set_nodes_white(transposed_graph)

    trees = []
    while stack:
        v = transposed_graph.get_node(stack.pop().label)
        if v.color == "White":
            tree = []
            DFS_VISIT(v, tree)
            trees.append(tree)

    forest = Graph()
    forest.array_to_DDS(trees)
    return forest


def transpose_graph(G: Graph):
    new_graph = Graph(directed=G.directed, weighted=G.weighted, NodeClass=G.NodeClass)

    for node in G.nodes:
        new_graph.add_node(node.label)

    for line in G.get_all_lines():
        new_graph.add_line(line[1].label, line[0].label)

    return new_graph


def set_nodes_white(G: Graph):
    for node in G.nodes:
        node.color = "White"


def DFS_VISIT(u: Node, stack):
    global time
    u.color = "Gray"
    time += 1
    u.d = time
    for v in u.adjacent_nodes:
        if v.color == "White":
            v.pie = u
            DFS_VISIT(v, stack)
    time += 1
    u.f = time
    u.color = "Black"
    stack.append(u)

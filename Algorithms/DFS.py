from Builder.GraphCreator import Graph, Node

time = 0

def DFS(g: Graph):
    for v in g.nodes:
        v.pie = None
        v.color = "White"
    for v in g.nodes:
        if v.color == "White":
            DFS_VISIT(g, v)


def DFS_VISIT(g: Graph, u: Node):
    global time
    u.color = "Gray"
    time += 1
    u.d = time
    for v in u.adjacent_nodes:
        if v.color == "White":
            v.pie = u
            DFS_VISIT(g, v)
    time += 1
    u.f = time
    u.color = "Black"

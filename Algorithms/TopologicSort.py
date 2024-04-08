from Builder.GraphCreator import Graph, Node

time = 0


def topologic_sort(G: Graph):
    stack = []

    def DFS(g: Graph):
        for v in g.nodes:
            v.pie = None
            v.color = "White"
        for v in g.nodes:
            if v.color == "White":
                DFS_VISIT(g, v)

    def DFS_VISIT(g: Graph, u: Node):
        global time
        nonlocal stack
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
        stack.append(u)

    DFS(G)
    return [stack.pop() for _ in range(len(stack))]

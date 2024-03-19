from Builder.GraphCreator import Graph, Node
from Classes.MatrixOfNodes import MatrixOfNodes


def weight_function(u: Node, v: Node):
    return u.adjacent_nodes[v]


def Floyd_Warshall(G: Graph, w=weight_function):
    D = MatrixOfNodes(G)
    PIE = MatrixOfNodes(G)
    for i in G.nodes:
        for j in G.nodes:
            if G.has_line(i.label, j.label):
                D[i, j] = w(i, j)
                PIE[i, j] = i
            elif i == j:
                D[i, j] = 0
                PIE[i, j] = None
            else:
                D[i, j] = float('inf')
                PIE[i, j] = None
    for k in range(len(G.nodes)):
        for i in range(len(G.nodes)):
            for j in range(len(G.nodes)):
                if D[i, j] > D[i, k] + D[k, j]:
                    D[i, j] = D[i, k] + D[k, j]
                    PIE[i, j] = PIE[k, j]

    return D, PIE

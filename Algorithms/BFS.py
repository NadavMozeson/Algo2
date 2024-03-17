from Builder.GraphCreator import Graph, Node
from Classes.CustomQueue import CustomQueue

def BFS(g: Graph, s: Node):
    for v in g.nodes:
        v.d = float('inf')
        v.pie = None
        v.color = 'White'
    s.d = 0
    s.color = 'Gray'
    Q = CustomQueue()
    Q.enqueue(s)
    while not Q.is_empty():
        u = Q.dequeue()
        for v in u.adjacent_nodes:
            if v.color == 'White':
                v.d = u.d + 1
                v.pie = u
                v.color = 'Gray'
                Q.enqueue(v)
        u.color = 'Black'

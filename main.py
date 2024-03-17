from Builder.GraphCreator import *
from Algorithms.DFS import *
from Algorithms.BFS import *
from Builder.GraphBuilder import *

def build_graph(option, nodes_amount=5, is_directed=False, has_weights=False, node_class="BFS"):
    if option == 'random':
        return generate_random_graph(num_of_nodes=nodes_amount, is_directed=is_directed, has_weight=has_weights, NodeClass=node_class)
    elif option == 'draw':
        app = GraphBuilderApp(directed=is_directed, weighted=has_weights, node_class=node_class)
        app.run()
        return app.graph

graph = build_graph("random", is_directed=True, has_weights=False, node_class="DFS")
graph.print()
DFS(g=graph)
graph.print_matrix()
graph.display()


from Builder.GraphCreator import *
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.Dijkstra import Dijkstra
from Algorithms.BellmamFord import Bellman_Ford
from Builder.GraphBuilder import *

def build_graph(option, nodes_amount=5, is_directed=False, has_weights=False, node_class="BFS"):
    if option == 'random':
        return generate_random_graph(num_of_nodes=nodes_amount, is_directed=is_directed, has_weight=has_weights, NodeClass=node_class)
    elif option == 'draw':
        app = GraphBuilderApp(directed=is_directed, weighted=has_weights, node_class=node_class)
        app.run()
        return app.graph

graph = build_graph("random", is_directed=True, has_weights=True, node_class="Dijkstra")
# graph = Graph.load("test")
graph.print()
graph.display()
print(Bellman_Ford(graph, graph.nodes[0]))
graph.print_matrix()


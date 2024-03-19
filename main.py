from Builder.GraphCreator import *
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.TopologicSort import topologic_sort
from Algorithms.KosarajuSharir import KosarajuSharir
from Algorithms.Dijkstra import Dijkstra
from Algorithms.BellmamFord import Bellman_Ford
from Algorithms.Kruskal import Kruskal
from Algorithms.Prim import Prim
from Builder.GraphBuilder import *
import time

def build_graph(option, nodes_amount=5, is_directed=False, has_weights=False, node_class="Node", has_cycle=True):
    if option == 'random':
        return generate_random_graph(num_of_nodes=nodes_amount, is_directed=is_directed, has_weight=has_weights, NodeClass=node_class, has_cycle=has_cycle)
    elif option == 'draw':
        app = GraphBuilderApp(directed=is_directed, weighted=has_weights, node_class=node_class)
        app.run()
        return app.graph

# graph = build_graph("draw", is_directed=False, has_weights=True, node_class="Node", has_cycle=False)
# graph.print()
graph = Graph.load("PrimVideoExample")
graph.display()
Prim(graph, graph.nodes[0])
graph.print_matrix()
graph.display_mst_of_graph()

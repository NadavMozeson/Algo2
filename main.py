from Builder.GraphCreator import *
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.TopologicSort import topologic_sort
from Algorithms.KosarajuSharir import KosarajuSharir
from Algorithms.Dijkstra import Dijkstra
from Algorithms.BellmamFord import Bellman_Ford
from Algorithms.Kruskal import Kruskal
from Algorithms.Prim import Prim
from Algorithms.DAG_Shortest_Path import DAG_Shortest_Path
from Algorithms.Floyd_Warshall import Floyd_Warshall
from Builder.GraphBuilder import *
from Builder.GraphCreatorApp import GraphCreatorApp, UserInput
from Builder.AlgorithmRules import *
import time

def build_graph(option, nodes_amount=5, is_directed=False, has_weights=False, node_class=Node, has_cycle=True):
    if option == 'random':
        return generate_random_graph(num_of_nodes=nodes_amount, is_directed=is_directed, has_weight=has_weights,
                                     NodeClass=node_class, has_cycle=has_cycle)
    elif option == 'draw':
        drawApp = GraphBuilderApp(directed=is_directed, weighted=has_weights, node_class=node_class)
        drawApp.run()
        return drawApp.graph

def algo_call(G: Graph, algorithm: str):
    def bfs_call():
        BFS(g=G, s=G.nodes[0])
        G.print_matrix()

    def dfs_call():
        DFS(g=G)
        G.print_matrix()

    def topologic_call():
        print(topologic_sort(G=G))

    def kosaraju_sharir_call():
        result = KosarajuSharir(G=G)
        result.print_dds_tree()

    def kruskal_call():
        result = Kruskal(G=G)
        result.display()

    def prim_call():
        Prim(G=G, r=G.nodes[0])
        G.print_matrix()

    def dijkstra_call():
        Dijkstra(G=G, s=G.nodes[0])
        G.print_matrix()

    def bellman_ford_call():
        print(Bellman_Ford(G=G, s=G.nodes[0]))
        G.print_matrix()

    def floyd_warshall_call():
        D, PIE = Floyd_Warshall(G=G)
        D.print_matrix()

    def dag_shortest_path_call():
        DAG_Shortest_Path(G=G, s=G.nodes[0])
        G.print_matrix()

    functions_dict = {
        "BFS": bfs_call,
        "DFS": dfs_call,
        "Topologic Sort": topologic_call,
        "Kosaraju-Sharir": kosaraju_sharir_call,
        "Kruskal": kruskal_call,
        "Prim": prim_call,
        "Dijkstra": dijkstra_call,
        "Bellman-Ford": bellman_ford_call,
        "Floyd-Warshall": floyd_warshall_call,
        "DAG Shortest Path": dag_shortest_path_call
    }

    functions_dict[algorithm]()

"""
D, PIE = Floyd_Warshall(graph)
PIE.print_matrix()
graph.print_matrix()
graph.display_mst_of_graph()"""

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphCreatorApp(root)
    root.mainloop()
    user_input: UserInput = app.return_result()
    print(user_input)
    algo_roles: AlgoRule = get_rule(user_input.algorithm)

    graph = None

    if user_input.loaded_filename:
        graph = Graph.load(user_input.loaded_filename)
    else:
        graph = build_graph(option=user_input.generation_method, nodes_amount=user_input.nodes_amount,
                            is_directed=user_input.is_directed, has_weights=user_input.has_weight,
                            node_class=algo_roles.node_class, has_cycle=algo_roles.circular)
    if user_input.save:
        graph.save(user_input.filename)

    graph.print()
    graph.display()
    algo_call(G=graph, algorithm=user_input.algorithm)

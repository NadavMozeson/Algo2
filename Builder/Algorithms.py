from Builder.AlgorithmRules import *
from Builder.GraphCreator import Graph

class Algorithms:
    ALGOS = {
        "BFS": {
            "SCRIPT": SCRIPTS.bfs_call,
            "RULES": RULES.BFS
        },
        "DFS": {
            "SCRIPT": SCRIPTS.dfs_call,
            "RULES": RULES.DFS
        },
        "Topologic Sort": {
            "SCRIPT": SCRIPTS.topologic_call,
            "RULES": RULES.TopologicSort
        },
        "Kosaraju-Sharir": {
            "SCRIPT": SCRIPTS.kosaraju_sharir_call,
            "RULES": RULES.KosarajuSharir
        },
        "Kruskal": {
            "SCRIPT": SCRIPTS.kruskal_call,
            "RULES": RULES.Kruskal
        },
        "Prim": {
            "SCRIPT": SCRIPTS.prim_call,
            "RULES": RULES.Prim
        },
        "Dijkstra": {
            "SCRIPT": SCRIPTS.dijkstra_call,
            "RULES": RULES.Dijkstra
        },
        "Bellman-Ford": {
            "SCRIPT": SCRIPTS.bellman_ford_call,
            "RULES": RULES.BellmanFord
        },
        "Floyd-Warshall": {
            "SCRIPT": SCRIPTS.floyd_warshall_call,
            "RULES": RULES.FloydWarshall
        },
        "DAG Shortest Path": {
            "SCRIPT": SCRIPTS.dag_shortest_path_call,
            "RULES": RULES.DAGShortestPath
        },
        "Ford-Fulkerson": {
            "SCRIPT": SCRIPTS.ford_fulkerson_call,
            "RULES": RULES.FordFulkerson
        },
        "Edmonds-Karp": {
            "SCRIPT": SCRIPTS.edmonds_karp_call,
            "RULES": RULES.EdmondsKarp
        }
    }

    def run_algorithm(self, graph: Graph, algorithm: str):
        SCRIPTS.G = graph
        self.ALGOS[algorithm]["SCRIPT"]()

    def get_algo_rule(self, algorithm: str):
        return self.ALGOS[algorithm]["RULES"]

    def get_algorithms_names(self):
        return list(self.ALGOS.keys())

ALGORITHMS = Algorithms()

from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.TopologicSort import topologic_sort
from Algorithms.KosarajuSharir import KosarajuSharir
from Algorithms.Dijkstra import Dijkstra
from Algorithms.BellmamFord import Bellman_Ford
from Algorithms.Kruskal import Kruskal
from Algorithms.Prim import Prim
from Algorithms.DAG_Shortest_Path import DAG_Shortest_Path
from Algorithms.FloydWarshall import Floyd_Warshall
from Algorithms.FordFulkerson import Ford_Flukerson
from Algorithms.EdmondsKarp import Edmonds_Karp
from Builder.GraphCreator import Node, NodeWColor, NodeWColorFinish, Graph

class AlgoRule:
    def __init__(self, name, node_class, directional, circular, weights):
        """
        :param name: Algorithm name
        :param node_class: Node class used in the algorithm
        :param directional: True if the algorithm is directional, False if not directions, None for both options
        :param circular: True if the algorithm runs on circular graphs, False if not
        :param weights: True when the algorithm uses weights, False if not
        """
        self.name: str = name
        self.node_class = node_class
        self.directional: bool = directional
        self.circular: bool = circular
        self.weights: bool = weights

class AlgoRulesList:
    def __init__(self):
        self.BFS: AlgoRule = AlgoRule(name='BFS', node_class=NodeWColor, directional=None, circular=True, weights=False)
        self.DFS: AlgoRule = AlgoRule(name='DFS', node_class=NodeWColorFinish, directional=None, circular=True, weights=False)
        self.TopologicSort: AlgoRule = AlgoRule(name='Topologic Sort', node_class=NodeWColor, directional=True, circular=False, weights=False)
        self.KosarajuSharir: AlgoRule = AlgoRule(name='Kosaraju-Sharir', node_class=NodeWColorFinish, directional=True, circular=True, weights=False)
        self.Kruskal: AlgoRule = AlgoRule(name='Kruskal', node_class=Node, directional=False, circular=True, weights=True)
        self.Prim: AlgoRule = AlgoRule(name='Prim', node_class=Node, directional=False, circular=True, weights=True)
        self.Dijkstra: AlgoRule = AlgoRule(name='Dijkstra', node_class=Node, directional=None, circular=True, weights=True)
        self.BellmanFord: AlgoRule = AlgoRule(name='Bellman-Ford', node_class=Node, directional=True, circular=True, weights=True)
        self.FloydWarshall: AlgoRule = AlgoRule(name='Floyd-Warshall', node_class=Node, directional=True, circular=True, weights=True)
        self.DAGShortestPath: AlgoRule = AlgoRule(name='DAG Shortest Path', node_class=Node, directional=True, circular=False, weights=True)
        self.FordFulkerson: AlgoRule = AlgoRule(name='Ford-Fulkerson', node_class=NodeWColorFinish, directional=True, circular=True, weights=True)
        self.EdmondsKarp: AlgoRule = AlgoRule(name='Edmonds-Karp', node_class=NodeWColor, directional=True, circular=True, weights=True)

class AlgoScripts:
    def __init__(self, graph: Graph = None):
        self.G: Graph = graph

    def bfs_call(self):
        BFS(g=self.G, s=self.G.nodes[0])
        self.G.print_matrix()

    def dfs_call(self):
        DFS(g=self.G)
        self.G.print_matrix()

    def topologic_call(self):
        print(topologic_sort(G=self.G))

    def kosaraju_sharir_call(self):
        result = KosarajuSharir(G=self.G)
        result.print_dds_tree()

    def kruskal_call(self):
        result = Kruskal(G=self.G)
        result.display()

    def prim_call(self):
        Prim(G=self.G, r=self.G.nodes[0])
        self.G.print_matrix()

    def dijkstra_call(self):
        Dijkstra(G=self.G, s=self.G.nodes[0])
        self.G.print_matrix()

    def bellman_ford_call(self):
        print(Bellman_Ford(G=self.G, s=self.G.nodes[0]))
        self.G.print_matrix()

    def floyd_warshall_call(self):
        D, PIE = Floyd_Warshall(G=self.G)
        print("D Matrix:")
        D.print_matrix()
        print("PIE Matrix:")
        PIE.print_matrix()

    def dag_shortest_path_call(self):
        DAG_Shortest_Path(G=self.G, s=self.G.nodes[0])
        self.G.print_matrix()

    def ford_fulkerson_call(self):
        flow_function = Ford_Flukerson(G=self.G, s=self.G.nodes[0], t=self.G.nodes[-1])
        print(flow_function)
        flow_sum = 0
        for u, v in flow_function.keys():
            if v == self.G.nodes[-1]:
                flow_sum += flow_function[(u, v)]
        print(f"Flow = {flow_sum}")

    def edmonds_karp_call(self):
        flow_function = Edmonds_Karp(G=self.G, s=self.G.nodes[0], t=self.G.nodes[-1])
        print(flow_function)
        flow_sum = 0
        for u, v in flow_function.keys():
            if v == self.G.nodes[-1]:
                flow_sum += flow_function[(u, v)]
        print(f"Flow = {flow_sum}")

SCRIPTS = AlgoScripts()
RULES = AlgoRulesList()

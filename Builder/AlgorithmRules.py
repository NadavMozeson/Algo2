from Builder.GraphCreator import Node, NodeWColor, NodeWColorFinish

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


def get_rule(algo_name):
    rules_list = AlgoRulesList()
    algo_dict = {
        "BFS": rules_list.BFS,
        "DFS": rules_list.DFS,
        "Topologic Sort": rules_list.TopologicSort,
        "Kosaraju-Sharir": rules_list.KosarajuSharir,
        "Kruskal": rules_list.Kruskal,
        "Prim": rules_list.Prim,
        "Dijkstra": rules_list.Dijkstra,
        "Bellman-Ford": rules_list.BellmanFord,
        "Floyd-Warshall": rules_list.FloydWarshall,
        "DAG Shortest Path": rules_list.DAGShortestPath,
        "Ford-Fulkerson": rules_list.FordFulkerson,
        "Edmonds-Karp": rules_list.EdmondsKarp
    }

    return algo_dict[algo_name]

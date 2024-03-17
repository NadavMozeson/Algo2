import networkx as nx
import matplotlib.pyplot as plt
import random
import pickle
from tabulate import tabulate
from collections import OrderedDict

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


class Node:
    """
    Superclass for all node types

    params:
    label: string = name of the node
    adjacent_nodes: dictionary[Node, int] = list of all neighbors of the node with the field label being the node and
                                            value being the weight if there is one
    """

    def __init__(self, label):
        self.label: str = label
        self.adjacent_nodes: OrderedDict[Node, int] = OrderedDict()

    def __repr__(self):
        return f"Node '{self.label}'"

    def add_adj(self, node, weight=None):
        self.adjacent_nodes[node] = weight
        self.adjacent_nodes = OrderedDict(sorted(self.adjacent_nodes.items(), key=lambda item: item[0].label))

class BFSNode(Node):
    def __init__(self, label):
        super().__init__(label)
        self.color: str = None
        self.pie: Node = None
        self.d: int = None

class DFSNode(Node):
    def __init__(self, label):
        super().__init__(label)
        self.color: str = None
        self.pie: Node = None
        self.d: int = None
        self.f: int = None


class DijkstraNode(Node):
    def __init__(self, label):
        super().__init__(label)
        self.pie: Node = None
        self.d: int = None


class Graph:
    def __init__(self, directed=False, weighted=False, NodeClass=BFSNode):
        self.NodeClass = NodeClass
        self.nodes: List[Node] = []
        self.directed: bool = directed
        self.weighted: bool = weighted

    def __repr__(self):
        return f"Graph with Nodes:{self.nodes}"

    def add_node(self, node: str):
        """
        Add a node to the graph

        :param node: Node name
        """
        self.nodes.append(self.NodeClass(node))
        self.nodes.sort(key=lambda x: x.label)

    def add_line(self, node1: str, node2: str, weight: int = None):
        """
        Add a line to the graph between 2 nodes with or without weight

        :param node1: From node name
        :param node2: To node name
        :param weight: weight of the line if needed (Default: None)
        """
        node1 = self.get_node(node1)
        node2 = self.get_node(node2)
        node1.add_adj(node2, weight)
        if not self.directed:
            node2.add_adj(node1, weight)

    def get_node(self, label: str):
        """
        Returns a node from the graph

        :param label: node label
        :return: Node object of the wanted node
        """
        for node in self.nodes:
            if node.label == label:
                return node
        return None

    def has_line(self, node1: str, node2: str):
        """
        Returns if there is a line between the two given nodes

        :param node1: From node
        :param node2: To node
        :return: returns true if the line between the two given nodes exists else False
        """
        node1 = self.get_node(node1)
        node2 = self.get_node(node2)
        return node2 in node1.adjacent_nodes

    def get_all_lines(self):
        lines = set()
        for node in self.nodes:
            for line_node in node.adjacent_nodes.keys():
                lines.add((node, line_node))
        return list(lines)

    def display(self):
        """
        Displays the graph in an image form in SciView
        """
        graph = nx.DiGraph() if self.directed else nx.Graph()
        edge_labels = {}

        for node in self.nodes:
            graph.add_node(node.label)
            for adj_node, weight in node.adjacent_nodes.items():
                if self.weighted:
                    graph.add_edge(node.label, adj_node.label, weight=weight)
                    edge_labels[(node.label, adj_node.label)] = weight
                    if not self.directed:
                        edge_labels[(adj_node.label, node.label)] = weight  # Add weight for reverse edge
                else:
                    graph.add_edge(node.label, adj_node.label)

        pos = nx.circular_layout(graph)
        if self.directed:
            nx.draw(graph, pos=pos, with_labels=True, node_size=1000, width=3.0, arrowsize=25, font_size=20)
        else:
            nx.draw(graph, pos=pos, with_labels=True, node_size=1000, width=3.0, font_size=20)

        if self.weighted:
            if self.directed:
                nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, font_weight='bold', font_size=15,
                                             label_pos=0.75)
            else:
                nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, font_weight='bold', font_size=15)

        plt.show()

    def print(self):
        """
        Prints the graph in the way the code is originally written

        :return: Prints the array of neighbors for each node in the graph
        """
        output = ""
        for node in self.nodes:
            output += f"[{node.label}]"
            for adj_node, weight in node.adjacent_nodes.items():
                output += f" -> [{adj_node.label}]"
            output += '\n'
        print(output)

    def print_matrix(self):
        """
        Prints the matrix of the nodes in the graph with the field's values of each node
        """
        field_names = [key for key in self.NodeClass('temp').__dict__.keys() if key not in ['label', 'adjacent_nodes']]
        header_row = ['']
        header_row.extend([node.label for node in self.nodes])

        matrix = [header_row]
        for field in field_names:
            row = [field]
            for node in self.nodes:
                if field in node.__dict__.keys():
                    if isinstance(node.__dict__[field], Node):
                        row.append(node.__dict__[field].label)
                    else:
                        row.append(node.__dict__[field])
                else:
                    row.append('')
            matrix.append(row)
        print(tabulate(matrix, headers="firstrow", tablefmt="fancy_grid"))

    def save(self, filename: str):
        """
        Save the graph to a file to load later

        :param filename: a name of the file without extension
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename: str):
        """
        Load the graph from a file that was created with the save function

        :param filename: a name of the file without extension
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)


NODE_CLASSES = {
    "Node": Node,
    "BFS": BFSNode,
    "DFS": DFSNode,
    "Dijkstra": DijkstraNode
}


def generate_random_graph(num_of_nodes, is_directed=False, has_weight=False, NodeClass="BFS", min_weight=0,
                          max_weight=10, lines_multiplier=3):
    """
    The function generate random graph from the given parameters and returns it as a Graph object

    :param num_of_nodes: amount of nodes to generate
    :param is_directed: is the graph directed (Default: False)
    :param has_weight: does the graph have weight for each line (Default: False)
    :param NodeClass: a string from the NODE_CLASSES dictionary of what node type to generate (Default: "BFS")
    :param min_weight: minimum weight for each line (Default: 0)
    :param max_weight: maximum weight for each line (Default: 10)
    :param lines_multiplier: a multiplier of amount of lines to generate (Default: 3)
    :return: returns a random generated graph as Graph object
    """
    graph = Graph(directed=is_directed, weighted=has_weight, NodeClass=NODE_CLASSES[NodeClass])

    for i in range(num_of_nodes):
        graph.add_node(LETTERS[i])

    num_of_lines = random.randint(num_of_nodes, num_of_nodes * lines_multiplier)
    for i in range(num_of_lines):
        node1 = LETTERS[random.randint(0, num_of_nodes - 1)]
        node2 = LETTERS[random.randint(0, num_of_nodes - 1)]
        if (not graph.has_line(node1, node2)) and (node1 != node2):
            if has_weight:
                weight = random.randint(min_weight, max_weight)
                graph.add_line(node1, node2, weight=weight)
            else:
                graph.add_line(node1, node2)
    return graph

import networkx as nx
import matplotlib.pyplot as plt
import random
import pickle
from tabulate import tabulate
from collections import OrderedDict
from copy import deepcopy

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
        self.pie: Node = None
        self.d: int = None

    def __repr__(self):
        return f"{circle_value(self.label)}"

    def __str__(self):
        return f"{self.label}"

    def add_adj(self, node, weight=None):
        self.adjacent_nodes[node] = weight
        self.adjacent_nodes = OrderedDict(sorted(self.adjacent_nodes.items(), key=lambda item: item[0].label))

    def remove_adj(self, node):
        self.adjacent_nodes.pop(node)
        self.adjacent_nodes = OrderedDict(sorted(self.adjacent_nodes.items(), key=lambda item: item[0].label))


class NodeWColor(Node):
    def __init__(self, label):
        super().__init__(label)
        self.color: str = None


class NodeWColorFinish(NodeWColor):
    def __init__(self, label):
        super().__init__(label)
        self.f: int = None


class Graph:
    def __init__(self, directed=False, weighted=False, flow=False, NodeClass=Node):
        self.NodeClass = NodeClass
        self.nodes: List[Node] = []
        self.directed: bool = directed
        self.weighted: bool = weighted
        self.flow: bool = flow

    def __repr__(self):
        return f"Graph with Nodes:{self.nodes}"

    def add_node(self, node: str):
        """
        Add a node to the graph

        :param node: Node name
        """
        self.nodes.append(self.NodeClass(node))
        self.nodes.sort(key=lambda x: (x.label.lower() != 's', x.label.lower()))

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

    def remove_line(self, node1: str, node2: str):
        node1.remove_adj(node2)
        if not self.directed:
            node2.remove_adj(node1)

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
                    edge_labels[(node.label, adj_node.label)] = f'{"0/" if self.flow else ""}{weight}'
                    if not self.directed:
                        edge_labels[(adj_node.label, node.label)] = weight
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
        with open('Graphs/' + filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename: str):
        """
        Load the graph from a file that was created with the save function

        :param filename: a name of the file without extension
        """
        with open('Graphs/' + filename, 'rb') as file:
            return pickle.load(file)

    def has_cycle(self):
        for start_node in self.nodes:
            stack = [(start_node, None)]
            visited = set()

            while stack:
                current_node, parent = stack.pop()

                if current_node in visited:
                    return True
                visited.add(current_node)

                for neighbour in current_node.adjacent_nodes:
                    if neighbour != parent:
                        stack.append((neighbour, current_node))

        return False

    def display_mst_of_graph(self):
        mst = Graph()
        for v in self.nodes:
            mst.add_node(v.label)
        for v in self.nodes:
            if v.pie:
                mst.add_line(v.label, v.pie.label)
        mst.display()


class FlowGraph:
    def __init__(self):
        self.N: Graph = None
        self.f = {}
        self.c = {}
        self.s: Node = None
        self.t: Node = None

    def copy(self, N, s, t):
        self.N = N
        self.s = s
        self.t = t
        self.set_c()

    def set_c(self):
        for u in self.N.nodes:
            for v in self.N.nodes:
                if v in u.adjacent_nodes.keys():
                    self.c[(u, v)] = u.adjacent_nodes[v]
                else:
                    self.c[(u, v)] = 0

    def update_removed_edges(self):
        for u, v in self.N.get_all_lines():
            if self.c[(u, v)] <= 0:
                self.N.remove_line(u, v)

    def display(self):
        """
        Displays the graph in an image form in SciView
        """
        graph = nx.DiGraph() if self.N.directed else nx.Graph()
        edge_labels = {}

        for node in self.N.nodes:
            graph.add_node(node.label)
            for adj_node, weight in node.adjacent_nodes.items():
                if self.N.weighted:
                    graph.add_edge(node.label, adj_node.label, weight=weight)
                    edge_labels[(node.label, adj_node.label)] = f'{self.f[(node, adj_node)]}/{weight}'
                    if not self.N.directed:
                        edge_labels[(adj_node.label, node.label)] = weight
                else:
                    graph.add_edge(node.label, adj_node.label)

        pos = nx.circular_layout(graph)
        if self.N.directed:
            nx.draw(graph, pos=pos, with_labels=True, node_size=1000, width=3.0, arrowsize=25, font_size=20)
        else:
            nx.draw(graph, pos=pos, with_labels=True, node_size=1000, width=3.0, font_size=20)

        if self.N.weighted:
            if self.N.directed:
                nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, font_weight='bold', font_size=15,
                                             label_pos=0.75)
            else:
                nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, font_weight='bold', font_size=15)

        plt.show()


def generate_random_graph(num_of_nodes, is_directed=False, has_weight=False, flow=False, NodeClass=Node, min_weight=0,
                          max_weight=10, lines_multiplier=3, has_cycle=True):
    """
    The function generate random graph from the given parameters and returns it as a Graph object

    :param num_of_nodes: amount of nodes to generate
    :param is_directed: is the graph directed (Default: False)
    :param has_weight: does the graph have weight for each line (Default: False)
    :param flow: does the graph represent a flow graph (Default: False)
    :param NodeClass: Node class to generate (Default: Node)
    :param min_weight: minimum weight for each line (Default: 0)
    :param max_weight: maximum weight for each line (Default: 10)
    :param lines_multiplier: a multiplier of amount of lines to generate (Default: 3)
    :param has_cycle: can the graph have a cycle (Default: True)
    :return: returns a random generated graph as Graph object
    """
    graph = Graph(directed=is_directed, weighted=has_weight, NodeClass=NodeClass, flow=flow)

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
    if not has_cycle:
        if not graph.has_cycle():
            return graph
        else:
            return generate_random_graph(num_of_nodes=num_of_nodes, is_directed=is_directed, has_weight=has_weight,
                                         flow=flow, NodeClass=NodeClass,
                                         min_weight=min_weight, max_weight=max_weight,
                                         lines_multiplier=lines_multiplier, has_cycle=has_cycle)
    else:
        return graph


def circle_value(input_char):
    if isinstance(input_char, str) and len(input_char) == 1:
        char_code = ord(input_char.lower())
        if ord('a') <= char_code <= ord('z'):
            return chr(0x24B6 + (char_code - ord('a')))
        elif ord('0') <= char_code <= ord('9'):
            return chr(0x2460 + (char_code - ord('0')))
        else:
            return input_char
    elif isinstance(input_char, int) and 0 <= input_char <= 9:
        return chr(0x2460 + input_char)
    else:
        return input_char

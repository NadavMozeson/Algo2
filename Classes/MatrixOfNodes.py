from Builder.GraphCreator import Node, Graph
from tabulate import tabulate


class MatrixOfNodes:
    def __init__(self, graph=None):
        self.nodesIndexes = {}
        count = 0
        for node in graph.nodes:
            self.nodesIndexes[node] = count
            count += 1
        self.size = len(self.nodesIndexes)
        self.matrix = [[None] * self.size for _ in range(self.size)]

    def __repr__(self):
        return f"MatrixOfNodes: {list(self.nodesIndexes.keys())}"

    def __getitem__(self, index):
        x, y = index
        if isinstance(x, int) and isinstance(y, int):
            return self.matrix[x][y]
        elif isinstance(x, Node) and isinstance(y, Node):
            return self.matrix[self.nodesIndexes[x]][self.nodesIndexes[y]]

    def __setitem__(self, index, value):
        x, y = index
        if isinstance(x, int) and isinstance(y, int):
            self.matrix[x][y] = value
        elif isinstance(x, Node) and isinstance(y, Node):
            self.matrix[self.nodesIndexes[x]][self.nodesIndexes[y]] = value

    def print_matrix(self):
        header_row = [node.label for node in self.nodesIndexes.keys()]
        print(tabulate(self.matrix, headers=header_row, showindex=header_row, tablefmt="fancy_grid"))

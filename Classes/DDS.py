class DDS:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def __repr__(self):
        return f"DDS with parents: {set(self.parent.values())}"

    def __str__(self):
        return f"DDS with parents: {self.parent}"

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1

    def print_dds_tree(self):
        print("DDS Tree:")
        roots = {key for key, value in self.parent.items() if key == value}
        visited = set()  # Track visited nodes
        for root in roots:
            self._print_tree(root, "", visited)

    def _print_tree(self, node, prefix, visited):
        if node in visited:
            return
        visited.add(node)
        children = [key for key, value in self.parent.items() if value == node]
        if children:
            print(prefix + "╭── " + str(node))
            for i, child in enumerate(children):
                self._print_tree(child, prefix + ("│   " if i != len(children) - 1 else "    "), visited)
        else:
            print(prefix + "╰── " + str(node))

    def array_to_DDS(self, trees):
        for tree in trees:
            root = tree[0]
            self.make_set(root)
            for node in tree[1:]:
                self.make_set(node)
                self.merge(root, node)

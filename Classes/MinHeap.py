from Builder.GraphCreator import Node

def compare_nodes(node1, node2):
    return node1.d < node2.d

class MinHeap:
    def __init__(self):
        self.heap = []
        self.compare = compare_nodes

    def __init__(self, array):
        self.heap = array
        self.compare = compare_nodes
        self._build_heap()

    def __repr__(self):
        return f"MinHeap with values: {self.heap}"

    def insert(self, node):
        self.heap.append(node)
        self._percolate_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        self._build_heap()
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._percolate_down(0)
        return min_val

    def is_empty(self):
        return len(self.heap) == 0

    def _build_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._percolate_down(i)

    def _percolate_up(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return
        if self.compare(self.heap[parent_idx], self.heap[idx]):
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._percolate_up(parent_idx)

    def _percolate_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest = idx

        if left_child_idx < len(self.heap) and self.compare(self.heap[left_child_idx], self.heap[smallest]):
            smallest = left_child_idx
        if right_child_idx < len(self.heap) and self.compare(self.heap[right_child_idx], self.heap[smallest]):
            smallest = right_child_idx

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._percolate_down(smallest)

    def peek_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def __str__(self):
        return str(self.heap)

    def value_exists(self, value):
        return value in self.heap

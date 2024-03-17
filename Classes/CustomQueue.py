class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("CustomQueue is empty")

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the queue.
        """
        return len(self.items)

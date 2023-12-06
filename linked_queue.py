class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None
    
    def is_empty(self):
        return self._front is None
    
    def enqueue(self, item):
        """Add an item in the queue in O(1) steps."""
        if self.is_empty():
            self._front = self.Node(item)
            self._back = self._front
        else:
            self._back.next = self.Node(item)
            self._back = self._back.next
    
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
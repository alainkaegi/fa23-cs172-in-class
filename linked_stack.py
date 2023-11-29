class LinkedStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None
    
    def push(self, item):
        self._top = self.Node(item, self._top)

    def pop(self):
        item = self._top._item
        self._top = self._top._next
        return item

    class Node:
        def __init__(self, item, next):
            self._item = item
            self._next = next

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

    def __eq__(self, other):
        if self is other:
            return True
        selfn = self._top
        othern = other._top
        while not (selfn is None) and not (othern is None):
            if selfn._item != othern._item:
                return False
            selfn = selfn._next
            othern = othern._next
        return selfn is None and othern is None

    def __iter__(self):
        self._iter_next_node = self._top
        return self

    def __next__(self):
        if not (self._iter_next_node is None):
            item = self._iter_next_node._item
            self._iter_next_node = self._iter_next_node._next
            return item
        else:
            raise StopIteration

    class Node:
        def __init__(self, item, next):
            self._item = item
            self._next = next

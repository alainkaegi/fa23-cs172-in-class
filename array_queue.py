from array_1 import Array

class EmptyQueueException(Exception):
    pass

class ArrayQueue:
    def __init__(self):
        self._data = Array(1)
        self._front = None
        self._back = None  # Not strictly necessary to initialize
                           # but useful to see listed as an instance variable
    
    def is_empty(self):
        return self._front is None

    def enqueue(self, item):
        """Add an item in the queue in O(1) steps."""
        if not self.is_empty() and self._front == self._back:
            self._resize(len(self._data)*2)
        if self.is_empty():
            self._front = 0
            self._back = 0
        self._data[self._back] = item
        self._back = (self._back + 1) % len(self._data)

    def dequeue(self):
        """Remove and return the oldest item in the queue in O(1) steps."""
        if self.is_empty():
            raise EmptyQueueException
        item = self._data[self._front]
        self._data[self._front] = None  # Tidy up
        self._front = (self._front + 1) % len(self._data)
        if self._front == self._back:
            self._front = None
        return item
    
    def _resize(self, newsize):
        newdata = Array(newsize)
        for i in range(len(self._data)):
            newdata[i] = self._data[self._front]
            self._front = (self._front + 1) % len(self._data)
        self._front = 0
        self._back = len(self._data)
        self._data = newdata

from array_1 import Array

class ArrayStack:
    def __init__(self):
        self._data = Array(1)
        self._count = 0

    def push(self, item):
        self._data[self._count] = item
        self._count += 1

    def pop(self):
        item = self._data[self._count - 1]
        self._data[self._count - 1] = None
        self._count -= 1
        return item


    def is_empty(self):
        pass

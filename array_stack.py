from array_1 import Array

class ArrayStack:
    def __init__(self):
        self._data = Array(1)
        self._count = 0

    def push(self, item):
        if self._count == len(self._data):
            self._resize(len(self._data) * 2)
        self._data[self._count] = item
        self._count += 1

    def pop(self):
        item = self._data[self._count - 1]
        self._data[self._count - 1] = None
        self._count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def _resize(self, new_size):
        new_data = Array(new_size)
        for i in range(self._count):
            new_data[i] = self._data[i]
        self._data = new_data

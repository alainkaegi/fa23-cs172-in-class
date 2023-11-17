class Vector:

    def __init__(self, a):
        self._coords = a[:]    # defensive copy

    def __str__(self):
        s = '['
        for i in range(len(self._coords) - 1):
            s += str(self._coords[i]) + ', '
        return s + str(self._coords[-1]) + ']'

    def __add__(self, other):
        r = Vector([0.0]*len(self._coords))
        for i in range(len(self._coords)):
            r._coords[i] = self._coords[i] + other._coords[i]
        return r
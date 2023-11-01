class Complex:

    def __init__(self, r, i):
        self._r = r
        self._i = i

    def __str__(self):
        return str(self._r) + ' + ' + str(self._i) + 'i'

    def add(self, other):
        return Complex(self._r + other._r, self._i + other._i)
    
    def __add__(self, other):
        return self.add(other)

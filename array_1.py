class Array:
    def __init__(self, capacity):
        self.__data = [0] * capacity

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Array index must be an int')
        return self.__data[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError('Array index must be an int')
        self.__data[index] = value

    def __repr__(self):
        return self.__data.__repr__()

    def __str__(self):
        return self.__data.__str__()

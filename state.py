from typing import Optional


class State:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[State] = None
        self.g = 0
        self.length = 0

    def __hash__(self):
        if isinstance(self.data, list):
            if isinstance(self.data[0], set):
                return hash(tuple(map(frozenset, self.data)))
            return hash(tuple(self.data))
        return hash(self.data)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

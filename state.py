from typing import Optional


class State:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[State] = None
        self.g = 0

    def __hash__(self):
        if isinstance(self.data, list):
            return hash(tuple(self.data))
        return hash(self.data)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

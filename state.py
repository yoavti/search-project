from typing import Optional


class State:
    def __init__(self, data):
        self.data = data
        self.prev: Optional[State] = None
        self.g = 0

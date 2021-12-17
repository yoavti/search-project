from algorithms import AStar
from state import State


class AStarTieBreaking(AStar):
    def insert_to_open(self, s):
        self.open_list.put((self.f(s), self.tau(s), s))

    def tau(self, s: State) -> float:
        raise NotImplemented

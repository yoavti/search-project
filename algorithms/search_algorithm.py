from queue import PriorityQueue
from state import State
from util import timed


class SearchAlgorithm:
    def __init__(self, search_space):
        self.search_space = search_space
        self.open_list = PriorityQueue()

    @timed
    def until_goal(self):
        self.open_list = PriorityQueue()
        closed_list = set()
        self.insert_to_open(self.search_space.get_start())
        while not self.open_list.empty():
            s: State = self.open_list.get()[-1]
            if s in closed_list:
                continue
            if self.search_space.is_goal(s):
                return len(closed_list)
            for neighbor, cost in self.search_space.get_neighbors(s):
                if neighbor in closed_list:
                    continue
                neighbor.g = s.g + cost
                self.insert_to_open(neighbor)
            closed_list.add(s)
        raise RuntimeError('did not reach goal')

    @timed
    def all_states(self):
        self.open_list = PriorityQueue()
        closed_list = set()
        self.insert_to_open(self.search_space.get_goal())
        while not self.open_list.empty():
            s: State = self.open_list.get()[-1]
            if s in closed_list:
                continue
            for neighbor, cost in self.search_space.get_neighbors(s):
                if neighbor in closed_list:
                    continue
                neighbor.g = s.g + cost
                neighbor.length = s.length + 1
                self.insert_to_open(neighbor)
            closed_list.add(s)
        return {s: s.g for s in closed_list}, {s: s.length for s in closed_list}

    def insert_to_open(self, s: State):
        self.open_list.put((self.f(s), s))

    def f(self, s: State) -> float:
        raise NotImplemented

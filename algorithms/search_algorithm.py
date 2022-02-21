from queue import PriorityQueue
from time import time
from state import State


class SearchAlgorithm:
    def __init__(self, search_space):
        self.search_space = search_space
        self.open_list = PriorityQueue()

    def until_goal(self):
        start_time = time()
        self.open_list = PriorityQueue()
        closed_list = set()
        self.insert_to_open(self.search_space.get_start())
        while not self.open_list.empty():
            s: State = self.open_list.get()[-1]
            if s in closed_list:
                continue
            if self.search_space.is_goal(s):
                runtime = time() - start_time
                expanded_states = len(closed_list)
                return runtime, expanded_states
            for neighbor, cost in self.search_space.get_neighbors(s):
                if neighbor in closed_list:
                    continue
                neighbor.g = s.g + cost
                self.insert_to_open(neighbor)
            closed_list.add(s)
        raise RuntimeError('did not reach goal')

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

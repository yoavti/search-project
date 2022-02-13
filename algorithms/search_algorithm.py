from queue import PriorityQueue
from time import time
from search_spaces import SearchSpace
from state import State


class SearchAlgorithm:
    def __init__(self, search_space: SearchSpace):
        self.search_space = search_space
        self.open_list = PriorityQueue()

    def run(self):
        start_time = time()
        self.open_list = PriorityQueue()
        closed_list = set()
        self.insert_to_open(self.search_space.get_start())
        while not self.open_list.empty():
            s: State = self.open_list.get()[-1]
            if s in closed_list:
                continue
            if self.search_space.is_goal(s):
                print('Runtime:', time() - start_time)
                print('Expanded States:', len(closed_list))
            for neighbor, cost in self.search_space.get_neighbors(s):
                if neighbor in closed_list:
                    continue
                neighbor.g = s.g + cost
                self.insert_to_open(neighbor)
            closed_list.add(s)

    def insert_to_open(self, s: State):
        self.open_list.put((self.f(s), s))

    def f(self, s: State) -> float:
        raise NotImplemented
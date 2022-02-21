from typing import List
import random
from algorithms.ucs import UCS
from search_spaces.search_space import SearchSpace
from state import State
import copy


def flip(array, i: int) -> List[int]:
    start = 0
    arr = copy.deepcopy(array)
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
    return arr


class Pancake(SearchSpace):
    def __init__(self, graph_size):
        assert graph_size >= 2
        self.graph_size = graph_size
        self.start_state = State(list(range(1, self.graph_size + 1)))
        self.shuffle_start()
        self.h_dict = {}

    def shuffle_start(self):
        random.shuffle(self.start_state.data)

    def get_start(self):
        return self.start_state

    def generate_h(self):
        self.h_dict = UCS(self).all_states()

    def get_neighbors(self, s):
        neighbors = []
        for i in range(1, self.graph_size):
            neighbors.append((State(flip(s.data, i)), 1))
        return neighbors

    def h(self, s):
        return self.h_dict[s]

    def h_cap(self, s):
        return self.h_dict[s]

    def h_cost_adapted(self, c, s):
        return self.h_dict[s] + c

    def operator_costs(self):
        return {1}

    def get_goal(self):
        pancake_array = list(range(1, self.graph_size + 1))
        return State(pancake_array)

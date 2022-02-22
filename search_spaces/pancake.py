import copy
from typing import List

from search_spaces.search_space import SearchSpace
from state import State
from util import is_ge


def flip(array: List[int], i: int) -> List[int]:
    start = 0
    arr = copy.deepcopy(array)
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
    return arr


def sub_lists(arr):
    lists = [[]]
    for i in range(len(arr) + 1):
        for j in range(i):
            lists.append(arr[j: i])
    return lists


class Pancake(SearchSpace):
    def __init__(self, pancakes):
        is_ge(pancakes, 'pancakes', 2)
        super().__init__()
        self.pancakes = pancakes
        self.start_state = State(list(range(self.pancakes)))

    def reset_start(self):
        max_h = max(self.h_dict.values())
        for s, h in self.h_dict.items():
            if h == max_h:
                self.start_state = s
                return

    def generate_h(self):
        super().generate_h()
        self.reset_start()

    def get_neighbors(self, s):
        neighbors = []
        for i in range(1, self.pancakes):
            neighbors.append((State(flip(s.data, i)), s.data[i]))
        return neighbors

    def operator_costs(self):
        return set(map(sum, sub_lists(self.start_state.data)))

    def get_goal(self):
        pancake_array = list(range(self.pancakes))
        return State(pancake_array)

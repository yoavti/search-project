from typing import List, Tuple, Set
import random
from search_spaces import SearchSpace
from state import State
import numpy as np
import copy


def flip(array, i) -> List[int]:
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
    def __init__(self, graph_size=int(input("enter pancake problem size"))):
        self.graph_size = graph_size

    def get_start(self) -> State:
        """Returns the start state for the search"""
        pancake_array = list(range(1, self.graph_size + 1))
        random.shuffle(pancake_array)
        return State(pancake_array)

    def is_goal(self, s: State) -> bool:
        """Returns whether the given state is a goal"""
        return np.array_equal(s.data, np.array(list(range(1, self.graph_size + 1))))

    def get_neighbors(self, s: State) -> List[Tuple[State, float]]:
        """Returns all neighbor states of the given state, as well as the cost to reach them"""
        neighbors = []
        for i in range(1, self.graph_size):
            neighbors.append((State(flip(s.data, i)), 1))
        return neighbors

    def h(self, s: State) -> float:
        """Returns the heuristic value of the given state"""
        raise NotImplemented

    def h_cap(self, s: State) -> float:
        """Returns the heuristic value of the given state as if all operator costs were 1"""
        raise NotImplemented

    def h_cost_adapted(self, c: float, s: State):
        """The same algorithm to compute h, but adds a constant c to each operator cost."""
        raise NotImplemented

    def operator_costs(self) -> Set[float]:
        """Returns a set of all operator costs"""
        raise NotImplemented

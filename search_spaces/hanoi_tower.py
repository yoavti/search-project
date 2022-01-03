from typing import List, Tuple, Set
import numpy as np
from search_spaces import SearchSpace
from state import State
import copy


def first_nonzero(arr, invalid_val=-1):
    mask = arr != 0
    return np.where(mask.any(axis=0), mask.argmax(axis=0), invalid_val)


class HanoiTower(SearchSpace):
    def __init__(self, disks=int(input("enter how many disks to put on the peg"))):
        self.disks = disks

    def get_start(self) -> State:
        """Returns the start state for the search"""
        hanoi_towers = np.zeros((10, self.disks))
        first_tower = np.array(list(range(1, self.disks + 1)))
        hanoi_towers[0] = first_tower
        return State(hanoi_towers)

    def is_goal(self, s: State) -> bool:
        """Returns whether the given state is a goal"""
        hanoi_towers_sorted = np.zeros((10, self.disks))
        last_tower = np.array(list(range(1, self.disks + 1)))
        hanoi_towers_sorted[9] = last_tower
        return np.array_equal(s.data, hanoi_towers_sorted)

    def get_neighbors(self, s: State) -> List[Tuple[State, float]]:
        """Returns all neighbor states of the given state, as well as the cost to reach them"""
        neighbors = []
        for i in range(10):
            j = first_nonzero(s.data[i], 0)
            if j != -1:
                for k in range(0, 9):
                    if k != i:
                        non_zero_index = first_nonzero(s.data[k])
                        if non_zero_index != -1:
                            if s.data[i][j] < s.data[k][non_zero_index]:
                                non_zero_index -= 1
                            else:
                                continue
                        hanoi_copy = copy.deepcopy(s.data)
                        hanoi_copy[k][non_zero_index] = s.data[i][j]
                        hanoi_copy[i][j] = 0
                        neighbors.append((State(hanoi_copy), 1))
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
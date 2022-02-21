from typing import List, Tuple, Set
from state import State
from algorithms.ucs import UCS


class SearchSpace:
    def __init__(self):
        self.start_state = State(None)
        self.h_dict = {}
        self.length_dict = {}

    def get_start(self) -> State:
        """Returns the start state for the search"""
        return self.start_state

    def generate_h(self):
        """Generates the perfect heuristic function"""
        self.h_dict, self.length_dict = UCS(self).all_states()

    def is_goal(self, s: State) -> bool:
        """Returns whether the given state is a goal"""
        return s.data == self.get_goal().data

    def get_neighbors(self, s: State) -> List[Tuple[State, float]]:
        """Returns all neighbor states of the given state, as well as the cost to reach them"""
        raise NotImplemented

    def h(self, s: State) -> float:
        """Returns the heuristic value of the given state"""
        return self.h_dict[s]

    def h_cap(self, s: State) -> float:
        """Returns the heuristic value of the given state as if all operator costs were 1"""
        return self.length_dict[s]

    def h_cost_adapted(self, c: float, s: State) -> float:
        """The same algorithm to compute h, but adds a constant c to each operator cost."""
        return self.h_dict[s] + c * self.length_dict[s]

    def operator_costs(self) -> Set[float]:
        """Returns a set of all operator costs"""
        raise NotImplemented

    def get_goal(self) -> State:
        """Returns the goal state of the search"""
        raise NotImplemented

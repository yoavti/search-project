from typing import List, Tuple, Set
from state import State


class SearchSpace:
    def get_start(self) -> State:
        """Returns the start state for the search"""
        raise NotImplemented

    def generate_h(self):
        """Generates the perfect heuristic function"""
        raise NotImplemented

    def is_goal(self, s: State) -> bool:
        """Returns whether the given state is a goal"""
        raise NotImplemented

    def get_neighbors(self, s: State) -> List[Tuple[State, float]]:
        """Returns all neighbor states of the given state, as well as the cost to reach them"""
        raise NotImplemented

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

    def get_goal(self) -> State:
        """Returns the goal state of the search"""
        raise NotImplemented

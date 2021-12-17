from typing import List, Tuple
from state import State


class SearchSpace:
    def get_start(self) -> State:
        """Returns the start state for the search"""
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

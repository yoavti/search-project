from algorithms.tie_breaking.a_star_tie_breaking import AStarTieBreaking
from search_spaces.search_space import SearchSpace


class FCostAdaptedTieBreaking(AStarTieBreaking):
    def __init__(self, search_space: SearchSpace, c: float):
        super().__init__(search_space)
        self.c = c

    def tau(self, s):
        return s.g + self.search_space.h_cost_adapted(self.c, s)

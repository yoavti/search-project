from a_star_tie_breaking import AStarTieBreaking
from search_spaces import SearchSpace


class HCostAdaptedTieBreaking(AStarTieBreaking):
    def __init__(self, search_space: SearchSpace, c: float):
        super().__init__(search_space)
        self.c = c

    def tau(self, s):
        return self.search_space.h_cost_adapted(self.c, s)

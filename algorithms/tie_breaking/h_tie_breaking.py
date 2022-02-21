from algorithms.tie_breaking.a_star_tie_breaking import AStarTieBreaking


class HTieBreaking(AStarTieBreaking):
    def tau(self, s):
        return self.search_space.h(s)

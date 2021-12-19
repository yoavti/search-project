from a_star_tie_breaking import AStarTieBreaking


class HCapTieBreaking(AStarTieBreaking):
    def tau(self, s):
        return self.search_space.h_cap(s)

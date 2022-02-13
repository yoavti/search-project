from search_algorithm import SearchAlgorithm


class AStar(SearchAlgorithm):
    def f(self, s):
        return s.g + self.search_space.h(s)

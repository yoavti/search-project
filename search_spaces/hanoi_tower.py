import numpy as np
from algorithms.ucs import UCS
from search_spaces.search_space import SearchSpace
from state import State
import copy


def first_nonzero(arr, invalid_val=-1):
    mask = arr != 0
    return np.where(mask.any(axis=0), mask.argmax(axis=0), invalid_val)


class HanoiTower(SearchSpace):
    def __init__(self, pegs, disks):
        assert pegs >= 3
        assert disks >= 2
        self.pegs = pegs
        self.disks = disks
        hanoi_towers = [set() for _ in range(self.pegs)]
        first_tower = set(range(self.disks))
        hanoi_towers[0] = first_tower
        self.start_state = State(hanoi_towers)
        self.h_dict = {}

    def get_start(self):
        return self.start_state

    def generate_h(self):
        self.h_dict = UCS(self).all_states()

    def calc_smallest_disc(self, s, peg):
        tower = s.data[peg]
        if len(tower) > 0:
            return min(tower)
        return self.disks

    def get_neighbors(self, s):
        neighbors = []
        smallest_discs = [self.calc_smallest_disc(s, peg) for peg in range(self.pegs)]
        for src in range(self.pegs):
            src_smallest = smallest_discs[src]
            if src_smallest == self.disks:
                continue
            for dst in range(self.pegs):
                if src == dst:
                    continue
                dst_smallest = smallest_discs[dst]
                if src_smallest >= dst_smallest:
                    continue
                to_add = copy.deepcopy(s.data)
                to_add[src].remove(src_smallest)
                to_add[dst].add(src_smallest)
                neighbors.append((State(to_add), 1))
        return neighbors

    def h(self, s):
        return self.h_dict[s]

    def h_cap(self, s):
        return self.h_dict[s]

    def h_cost_adapted(self, c, s):
        return self.h_dict[s] + c

    def operator_costs(self):
        return {1}

    def get_goal(self):
        hanoi_towers_sorted = [set() for _ in range(self.pegs)]
        last_tower = set(range(self.disks))
        hanoi_towers_sorted[-1] = last_tower
        return State(hanoi_towers_sorted)

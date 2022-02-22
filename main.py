from algorithms.a_star import AStar
from algorithms.tie_breaking.f_cost_adapted_tie_breaking import FCostAdaptedTieBreaking
from algorithms.tie_breaking.h_cap_tie_breaking import HCapTieBreaking
from algorithms.tie_breaking.h_cost_adapted_tie_breaking import HCostAdaptedTieBreaking
from algorithms.tie_breaking.h_tie_breaking import HTieBreaking
from search_spaces.hanoi_tower import HanoiTower
from search_spaces.pancake import Pancake


MULT_FACTOR = 2


def initialize_search_space(search_space):
    operator_costs = search_space.operator_costs()
    epsilon = min(operator_costs) / MULT_FACTOR
    M = max(operator_costs) * MULT_FACTOR
    print('generating h*')
    search_space.generate_h()
    print('finished')
    return epsilon, M


def compare_algorithms(search_space, algorithm_constructors):
    epsilon, M = initialize_search_space(search_space)
    for algorithm_constructor in algorithm_constructors:
        algorithm = algorithm_constructor(search_space, epsilon, M)
        print(algorithm.__class__.__name__)
        runtime, expanded_states = algorithm.until_goal()
        print('runtime:', runtime)
        print('expanded_states:', expanded_states)
        print()
    print()


def pancake_experiments(sizes, algorithm_constructors):
    for graph_size in sizes:
        print(f'{graph_size=}')
        search_space = Pancake(graph_size)
        compare_algorithms(search_space, algorithm_constructors)


def hanoi_experiments(peg_disk_combinations, algorithm_constructors):
    for pegs, disks in peg_disk_combinations:
        print(f'{pegs=} {disks=}')
        search_space = HanoiTower(pegs, disks)
        compare_algorithms(search_space, algorithm_constructors)


def non_cost_adapted(algorithm):
    def ret(search_space, _, __):
        return algorithm(search_space)

    return ret


def epsilon_cost_adapted(algorithm):
    def ret(search_space, epsilon, _):
        print('epsilon')
        return algorithm(search_space, epsilon)

    return ret


def M_cost_adapted(algorithm):
    def ret(search_space, _, M):
        print('M')
        return algorithm(search_space, M)

    return ret


if __name__ == '__main__':
    _algorithm_constructors = [non_cost_adapted(AStar),
                               non_cost_adapted(HCapTieBreaking),
                               non_cost_adapted(HTieBreaking),
                               epsilon_cost_adapted(FCostAdaptedTieBreaking),
                               epsilon_cost_adapted(HCostAdaptedTieBreaking),
                               M_cost_adapted(FCostAdaptedTieBreaking),
                               M_cost_adapted(HCostAdaptedTieBreaking)]
    _peg_disk_combinations_backup = [(3, 10), (4, 8), (5, 6), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5)]
    _peg_disk_combinations = [(3, 10), (4, 8), (5, 6)]
    hanoi_experiments(_peg_disk_combinations, _algorithm_constructors)
    _sizes = list(range(2, 10))
    pancake_experiments(_sizes, _algorithm_constructors)

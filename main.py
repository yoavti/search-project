from algorithms.a_star import AStar
from algorithms.tie_breaking.f_cost_adapted_tie_breaking import FCostAdaptedTieBreaking
from algorithms.tie_breaking.h_cap_tie_breaking import HCapTieBreaking
from algorithms.tie_breaking.h_cost_adapted_tie_breaking import HCostAdaptedTieBreaking
from algorithms.tie_breaking.h_tie_breaking import HTieBreaking
from search_spaces.hanoi_tower import HanoiTower
from search_spaces.pancake import Pancake


def initialize_search_space(search_space):
    print('generating h*')
    search_space.generate_h()
    operator_costs = search_space.operator_costs()
    operator_costs = {cost for cost in operator_costs if cost > 0}
    max_length = search_space.max_length()
    epsilon = min(operator_costs) / (max_length + 1)
    M = max(operator_costs) * (max_length + 1)
    return epsilon, M


def compare_algorithms(search_space, algorithm_constructors):
    epsilon, M = initialize_search_space(search_space)
    for algorithm_constructor in algorithm_constructors:
        algorithm = algorithm_constructor(search_space, epsilon, M)
        print(algorithm.__class__.__name__)
        print('expanded_states:', algorithm.until_goal())
        print()
    print()


def pancake_experiment(pancakes, algorithm_constructors):
    print('Pancake')
    search_space = Pancake(pancakes)
    compare_algorithms(search_space, algorithm_constructors)
    print()


def hanoi_experiments(peg_disk_combinations, algorithm_constructors):
    print('HanoiTower')
    for pegs, disks in peg_disk_combinations:
        print(f'{pegs=} {disks=}')
        search_space = HanoiTower(pegs, disks)
        compare_algorithms(search_space, algorithm_constructors)
    print()


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


def one_cost_adapted(algorithm):
    def ret(search_space, _, __):
        print(1)
        return algorithm(search_space, 1)

    return ret


if __name__ == '__main__':
    _algorithm_constructors = [non_cost_adapted(AStar),
                               non_cost_adapted(HCapTieBreaking),
                               non_cost_adapted(HTieBreaking),
                               epsilon_cost_adapted(FCostAdaptedTieBreaking),
                               epsilon_cost_adapted(HCostAdaptedTieBreaking),
                               M_cost_adapted(FCostAdaptedTieBreaking),
                               M_cost_adapted(HCostAdaptedTieBreaking),
                               one_cost_adapted(FCostAdaptedTieBreaking),
                               one_cost_adapted(HCostAdaptedTieBreaking)]
    _peg_disk_combinations = [(3, 13), (4, 10), (5, 8)]
    hanoi_experiments(_peg_disk_combinations, _algorithm_constructors)
    _pancakes = 10
    pancake_experiment(_pancakes, _algorithm_constructors)

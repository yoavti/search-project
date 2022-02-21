from algorithms.a_star import AStar
from algorithms.tie_breaking.f_cost_adapted_tie_breaking import FCostAdaptedTieBreaking
from algorithms.tie_breaking.h_cap_tie_breaking import HCapTieBreaking
from algorithms.tie_breaking.h_cost_adapted_tie_breaking import HCostAdaptedTieBreaking
from algorithms.tie_breaking.h_tie_breaking import HTieBreaking
from search_spaces.hanoi_tower import HanoiTower
from search_spaces.pancake import Pancake


def start_experiment(search_space, algorithm_constructor):
    operator_costs = search_space.operator_costs()
    epsilon = min(operator_costs) / 2
    M = max(operator_costs) * 2
    algorithm = algorithm_constructor(search_space, epsilon, M)
    print(algorithm.__class__.__name__)
    print('generating h*')
    search_space.generate_h()
    print('finished')
    return algorithm


def pancake_experiment(graph_size, algorithm_constructor, num_runs=100, print_runs=False):
    search_space = Pancake(graph_size)
    algorithm = start_experiment(search_space, algorithm_constructor)
    runtime_sum = 0
    expanded_states_sum = 0
    for i in range(num_runs):
        search_space.shuffle_start()
        runtime, expanded_states = algorithm.until_goal()
        if print_runs:
            print(i)
            print(search_space.get_start().data)
            print('runtime:', runtime)
            print('expanded_states:', expanded_states)
        runtime_sum += runtime
        expanded_states_sum += expanded_states
    print('avg runtime:', runtime_sum / num_runs)
    print('avg expanded_states:', expanded_states_sum / num_runs)


def hanoi_experiment(pegs, disks, algorithm_constructor):
    search_space = HanoiTower(pegs, disks)
    algorithm = start_experiment(search_space, algorithm_constructor)
    runtime, expanded_states = algorithm.until_goal()
    print('runtime:', runtime)
    print('expanded_states:', expanded_states)


def pancake_experiments(sizes, algorithm_constructors):
    for graph_size in sizes:
        print(f'{graph_size=}')
        for algorithm_constructor in algorithm_constructors:
            pancake_experiment(graph_size, algorithm_constructor)
            print()
        print()


def hanoi_experiments(peg_disk_combinations, algorithm_constructors):
    for pegs, disks in peg_disk_combinations:
        print(f'{pegs=} {disks=}')
        for algorithm_constructor in algorithm_constructors:
            hanoi_experiment(pegs, disks, algorithm_constructor)
            print()
        print()


def non_cost_adapted(algorithm):
    def ret(search_space, epsilon, M):
        return algorithm(search_space)

    return ret


def epsilon_cost_adapted(algorithm):
    def ret(search_space, epsilon, M):
        return algorithm(search_space, epsilon)

    return ret


def M_cost_adapted(algorithm):
    def ret(search_space, epsilon, M):
        return algorithm(search_space, M)

    return ret


if __name__ == '__main__':
    algorithm_constructors = [non_cost_adapted(AStar),
                              non_cost_adapted(HCapTieBreaking),
                              non_cost_adapted(HTieBreaking),
                              epsilon_cost_adapted(FCostAdaptedTieBreaking),
                              epsilon_cost_adapted(HCostAdaptedTieBreaking),
                              M_cost_adapted(FCostAdaptedTieBreaking),
                              M_cost_adapted(HCostAdaptedTieBreaking)]
    peg_disk_combinations_backup = [(3, 10), (4, 8), (5, 6), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5)]
    peg_disk_combinations = [(3, 10), (4, 8), (5, 6)]
    hanoi_experiments(peg_disk_combinations, algorithm_constructors)
    sizes = list(range(2, 10))
    # pancake_experiments(sizes, algorithm_constructors)

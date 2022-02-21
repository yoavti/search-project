from algorithms.a_star import AStar
from algorithms.tie_breaking.f_cost_adapted_tie_breaking import FCostAdaptedTieBreaking
from algorithms.tie_breaking.h_cap_tie_breaking import HCapTieBreaking
from algorithms.tie_breaking.h_cost_adapted_tie_breaking import HCostAdaptedTieBreaking
from algorithms.tie_breaking.h_tie_breaking import HTieBreaking
from search_spaces.hanoi_tower import HanoiTower
from search_spaces.pancake import Pancake


def pancake_experiment(graph_size, algorithm_constructor, num_runs=100, print_runs=False):
    search_space = Pancake(graph_size)
    algorithm = algorithm_constructor(search_space)
    print('generating h*')
    search_space.generate_h()
    print('finished')
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
    algorithm = algorithm_constructor(search_space)
    print('generating h*')
    search_space.generate_h()
    print('finished')
    runtime, expanded_states = algorithm.until_goal()
    print('runtime:', runtime)
    print('expanded_states:', expanded_states)


def pancake_experiments(sizes, algorithm_constructors):
    for graph_size in sizes:
        print(f'{graph_size=}')
        for algorithm_constructor in algorithm_constructors:
            print(algorithm_constructor.__name__)
            pancake_experiment(graph_size, algorithm_constructor)


def hanoi_experiments(peg_disk_combinations, algorithm_constructors):
    for pegs, disks in peg_disk_combinations:
        print(f'{pegs=} {disks=}')
        for algorithm_constructor in algorithm_constructors:
            print(algorithm_constructor.__name__)
            hanoi_experiment(pegs, disks, algorithm_constructor)


if __name__ == '__main__':
    def f_cost_adapted_tie_breaking(search_space):
        return FCostAdaptedTieBreaking(search_space, 1)


    def h_cost_adapted_tie_breaking(search_space):
        return HCostAdaptedTieBreaking(search_space, 1)


    algorithm_constructors = [AStar, f_cost_adapted_tie_breaking, HCapTieBreaking, h_cost_adapted_tie_breaking,
                              HTieBreaking]
    peg_disk_combinations_backup = [(3, 10), (4, 8), (5, 6), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5)]
    peg_disk_combinations = [(3, 10), (4, 8), (5, 6)]
    hanoi_experiments(peg_disk_combinations, algorithm_constructors)
    sizes = list(range(2, 10))
    # pancake_experiments(sizes, algorithm_constructors)

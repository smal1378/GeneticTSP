# Run this file to run genetic algorithm for solving traveling salesman problem
# By Esmail Mahjoor

# All cities coordinates
from typing import List, Tuple

from tsp import TSP

cities: List[Tuple[int, int]] = [
    (35, 51),
    (113, 213),
    (82, 280),
    (322, 340),
    (256, 352),
    (160, 24),
    (322, 145),
    (12, 349),
    (282, 20),
    (241, 8),
    (398, 153),
    (182, 305),
    (153, 257),
    (275, 190),
    (242, 75),
    (19, 229),
    (303, 352),
    (39, 309),
    (383, 79),
    (226, 343),
]
instance = TSP(
    cities=cities,
    population_size=300,
    generation_count=100
)

if __name__ == '__main__':
    instance.run(use_progressbar=True)
    solution = instance.best()
    print(solution.way)
    print(solution.fitness, solution.total_distance())

    import matplotlib.pyplot as pyplot
    from matplotlib.figure import Figure
    from matplotlib.axes import Axes
    fig: Figure = pyplot.figure()

    axes = fig.subplots(1, 2)
    ax: Axes = axes[0]
    ax.plot(instance.plot_avg_fitness, label='AVG Fit')
    ax.plot(instance.plot_best_fitness, label="Best Fit")
    ax.plot(instance.plot_min_fitness, label="Min Fit")

    ax2: Axes = axes[1]
    x = [city[0] for city in cities]
    y = [city[1] for city in cities]
    ax2.scatter(x, y, label="Map")
    for i in range(len(cities)-1):
        ax2.plot((solution.way[i][0], solution.way[i+1][0]),
                 (solution.way[i][1], solution.way[i+1][1]))
    for i in range(len(cities)):
        ax2.annotate(i+1, (solution.way[i][0]+2, solution.way[i][1]+5))

    fig.legend()
    pyplot.show()


# implementation of TSA API
# run `run.py` instead of this file
import random
from typing import List, Tuple

import tqdm

if __name__ == '__main__':
    raise ValueError("This module is not meant to be executed directly")

CitiesType = List[Tuple[int, int]]
PopulationType = List["Solution"]


class Solution:
    def __init__(self, cities: CitiesType):
        self.way: CitiesType = cities.copy()
        self.fitness = self._fitness_function()

    @classmethod
    def random_instance(cls, cities: CitiesType) -> 'Solution':
        result = []
        cities = cities.copy()
        for i in range(len(cities)):
            city = random.choice(cities)
            cities.remove(city)
            result.append(city)
        return Solution(result)

    def _fitness_function(self) -> float:
        total = self.total_distance()
        return max(0, 5000 - total)

    def total_distance(self):
        total = 0
        for i in range(len(self.way)-1):
            total += self._distance(i, i+1)
        return total

    def _distance(self, i, j):
        return ((self.way[i][0]-self.way[j][0])**2 + (self.way[i][1]-self.way[j][1])**2)**0.5

    def crossover(self, other: "Solution") -> Tuple['Solution', 'Solution']:
        # fitness based crossover
        point = random.randint(0, len(self.way)-1)
        way1 = self.way[:point]
        way2 = other.way[:point]

        for city1, city2 in zip(self.way[point:], other.way[point:]):
            # city1 most go to way2 - because it's in self
            # city2 wise versa
            if city1 not in way2:
                way2.append(city1)
            else:
                way1.append(city1)
            if city2 not in way1:
                way1.append(city2)
            else:
                way2.append(city2)
        return Solution(way1), Solution(way2)

    def mutate(self):
        i = random.randint(0, len(self.way)-1)
        j = random.randint(0, len(self.way)-1)
        if j == i:
            j = (j + 1) % len(self.way)
        self.way[i], self.way[j] = self.way[j], self.way[i]


class TSP:
    def __init__(self,
                 cities: CitiesType,
                 population_size: int,
                 generation_count: int):
        self.size = population_size
        self.count = generation_count
        self.cities = cities
        self.current = 0
        self.population: PopulationType = []
        self.plot_best_fitness: List[float] = []
        self.plot_avg_fitness: List[float] = []
        self.plot_min_fitness: List[float] = []

    @property
    def pm(self) -> float:
        return 0.10

    @property
    def pc(self) -> float:
        return 0.90

    def _create_initial_population(self):
        for i in range(self.size):
            sol = Solution.random_instance(self.cities)
            self.population.append(sol)

    def run(self, use_progressbar=False):
        self._create_initial_population()
        if use_progressbar:
            trange = tqdm.trange
        else:
            trange = range
        for i in trange(self.count):
            self.current += 1
            # Parent Selection
            self.plot_best_fitness.append(self.best().fitness)
            self.plot_avg_fitness.append(sum(s.fitness for s in self.population)/len(self.population))
            self.plot_min_fitness.append(min(self.population, key=lambda e: e.fitness).fitness)
            pool = self._parent_selection()
            offsprings = self._crossover(pool)
            self.population = offsprings
            self._mutate()

    def _parent_selection(self) -> PopulationType:
        # K tournament
        k = 2
        result: PopulationType = []
        for i in range(len(self.population)):
            tournament = []
            for j in range(k):
                tournament.append(random.choice(self.population))
            result.append(max(tournament, key=lambda e: e.fitness))
        return result

    def _crossover(self, mutation_pool: PopulationType) -> PopulationType:
        offsprings: PopulationType = []
        while mutation_pool:
            parent1 = random.choice(mutation_pool)
            mutation_pool.remove(parent1)
            parent2 = random.choice(mutation_pool)
            mutation_pool.remove(parent2)
            chance = random.random()
            if chance < self.pc:
                child1, child2 = parent1.crossover(parent2)
                offsprings.append(child1)
                offsprings.append(child2)
            else:
                offsprings.append(parent1)
                offsprings.append(parent2)
        return offsprings

    def _mutate(self):
        for solution in self.population:
            chance = random.random()
            if chance < self.pm:
                solution.mutate()

    def best(self):
        return max(self.population, key=lambda s: s.fitness)

from random import randint
from .Chromosome import Chromosome


class GeneticAlgorithm:
    def run(self, m, P, V, products, population_size=50):
        products = products.copy()
        weights = []
        volumes = []
        profits = []
        for product in products:
            weights.append(product[0])
            volumes.append(product[1])
            profits.append(product[2])
        self.weights = weights
        self.volumes = volumes
        self.profits = profits
        self.knapsack_sizes = P
        self.max_volumes = V
        self.population_size = population_size

        self.chromosomes = [Chromosome(weights, volumes, profits, P, V, m, products.copy()) for _ in
                            range(population_size)]
        self.chromosomes.sort(key=lambda x: x.fitness(), reverse=True)
        solution = self.evolve(500, m, products.copy())

        max_selected_products = [[] * len(products) for _ in range(len(solution.genes))]

        for rowIndex in range(len(solution.genes)):
            for columnIndex in range(len(solution.genes[rowIndex])):
                if (solution.genes[rowIndex][columnIndex] == 1):
                    max_selected_products[rowIndex].append(products[columnIndex])
        return solution.fitness(), max_selected_products

    def crossover(self, parents, m, products):
        return parents[0].single_point_crossover(parents[1], m, products)

    def mutation(self, offsprings):
        for offspring in offsprings:
            offspring.mutate()
        return offsprings

    def next_generation(self, m, products):
        n_selection = int(self.population_size * 0.4)
        offsprings = []

        for _ in range(n_selection):
            parent1_index = randint(0, self.population_size - 1)
            parent2_index = randint(0, self.population_size - 1)
            parent1 = self.chromosomes[parent1_index]
            parent2 = self.chromosomes[parent2_index]
            offsprings.extend(self.crossover([parent1, parent2], m, products))

        offsprings = self.mutation(offsprings)
        offsprings = [offspring for offspring in offsprings if offspring.fitness() > 0]

        self.chromosomes.extend(offsprings)
        self.chromosomes.sort(key=lambda x: x.fitness(), reverse=True)
        self.chromosomes = self.chromosomes[:self.population_size]

    def evolve(self, generations, m, products):
        for _ in range(0, generations):
            self.next_generation(m, products)
        return self.chromosomes[0]

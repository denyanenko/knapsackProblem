from random import choice, randint, random

MUTATION_PROBABILITY = 0.5


class Chromosome:
    def population_generator(self, m, P, V, products):
        all_products = products.copy()
        products_to_genes = []
        selected_list = [0] * len(products)

        for i in range(m):
            knapsack_capacity = P[i]
            knapsack_volume = V[i]
            products_in_knapsack = [0] * len(all_products)
            available_products = []

            for product in products:
                weight, volume, _ = product
                if (weight <= knapsack_capacity and volume <= knapsack_volume):
                    available_products.append(product)

            while len(available_products) > 0:
                selected_product = choice(available_products)
                weight, volume, _ = selected_product

                for j, product in enumerate(all_products):
                    if product == selected_product and selected_list[j] == 0:
                        products_in_knapsack[j] = 1
                        selected_list[j] = 1
                        break

                knapsack_capacity -= weight
                knapsack_volume -= volume
                products.remove(selected_product)
                available_products.remove(selected_product)

                for product in available_products[:]:
                    weight, volume, _ = product
                    if (weight > knapsack_capacity or volume > knapsack_volume):
                        available_products.remove(product)

            products_to_genes.append(products_in_knapsack)
        return products_to_genes

    def __init__(self, weights, volumes, profits, P, V, m, products):
        self.weights = weights
        self.volumes = volumes
        self.profits = profits
        self.knapsack_sizes = P
        self.max_volumes = V

        generatedGenes = self.population_generator(m, P, V, products.copy())
        self.genes = generatedGenes

    def fitness(self):
        total_profits = [0] * len(self.knapsack_sizes)
        for k in range(len(self.knapsack_sizes)):
            total_weight = 0
            total_volume = 0
            for i in range(len(self.genes[k])):
                if self.genes[k][i] == 1:
                    total_weight += self.weights[i]
                    total_volume += self.volumes[i]
                    total_profits[k] += self.profits[i]
            if total_weight > self.knapsack_sizes[k] or total_volume > self.max_volumes[k]:
                total_profits[k] = 0
                return 0
        return sum(total_profits)

    def single_point_crossover(self, chromosome, m, products):
        crossover_point = randint(1, len(self.genes[0]) - 1)
        offspring1 = Chromosome(self.weights, self.volumes, self.profits, self.knapsack_sizes, self.max_volumes, m,
                                products)
        offspring2 = Chromosome(self.weights, self.volumes, self.profits, self.knapsack_sizes, self.max_volumes, m,
                                products)

        for k in range(len(self.knapsack_sizes)):
            offspring1.genes[k] = self.genes[k][:crossover_point] + chromosome.genes[k][crossover_point:]
            offspring2.genes[k] = chromosome.genes[k][:crossover_point] + self.genes[k][crossover_point:]

        return offspring1, offspring2

    def mutate(self):
        def clean_column(matrix, columnIndex, rowIndex):
            for idx in range(len(matrix)):
                if rowIndex != idx:
                    matrix[idx][columnIndex] = 0
            return matrix

        for rowIndex in range(len(self.genes)):
            index_to_mutate = randint(0, len(self.genes[rowIndex]) - 1)
            if random() < MUTATION_PROBABILITY:
                self.genes = clean_column(self.genes, index_to_mutate, rowIndex)
                self.genes[rowIndex][index_to_mutate] = 1

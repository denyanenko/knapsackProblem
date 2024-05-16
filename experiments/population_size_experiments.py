from application.Application import experiments_input, print_and_save
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm


def population_size_experiments():
    count_experiments = 20
    sizes = [2, 5, 10, 15, 20, 25, 30, 35, 40, 50, 100]
    n = 50
    totals = [0] * len(sizes)
    for _ in range(count_experiments):
        m, P, V, products = experiments_input(n)
        for idx in range(len(sizes)):
            total_value, selected_products = GeneticAlgorithm().run(m, P, V, products, sizes[idx])
            totals[idx] += total_value
    avgs = [total / count_experiments for total in totals]
    for i, avg in enumerate(avgs):
        print_and_save(f"Розмір популяції {sizes[i]} - середнє значення {avg}")


def main():
    population_size_experiments()


if __name__ == "__main__":
    main()

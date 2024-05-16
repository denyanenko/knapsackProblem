from greedy_algorithm.GreedyAlgorithm import GreedyAlgorithm
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from application.Application import experiments_input, print_and_save
import time


def dimension_experiments():
    for n in range(10, 101, 10):
        greedy_times = []
        greedy_values = []
        probabilistic_times = []
        probabilistic_values = []
        ga_times = []
        ga_values = []
        for _ in range(20):
            m, P, V, products = experiments_input(n)

            start_time = time.time()
            greedy_total, _ = GreedyAlgorithm.run(m, P, V, products)
            end_time = time.time()
            greedy_times.append(end_time - start_time)
            greedy_values.append(greedy_total)

            start_time = time.time()
            probabilistic_total, _ = ProbabilisticAlgorithm.run(m, P, V, products)
            end_time = time.time()
            probabilistic_times.append(end_time - start_time)
            probabilistic_values.append(probabilistic_total)

            ga = GeneticAlgorithm()
            start_time = time.time()
            ga_total, _ = ga.run(m, P, V, products)
            end_time = time.time()
            ga_times.append(end_time - start_time)
            ga_values.append(ga_total)

        greedy_avg_time = sum(greedy_times) / len(greedy_times)
        greedy_avg_value = sum(greedy_values) / len(greedy_values)
        probabilistic_avg_time = sum(probabilistic_times) / len(probabilistic_times)
        probabilistic_avg_value = sum(probabilistic_values) / len(probabilistic_values)
        ga_avg_time = sum(ga_times) / len(ga_times)
        ga_avg_value = sum(ga_values) / len(ga_values)

        print_and_save(f"Для {n} товарів:")
        print_and_save(f"ЖАДІБНИЙ АЛГОРИТМ - Середній час роботи: {greedy_avg_time}, Середнє значення ЦФ: {greedy_avg_value}")

        print_and_save(f"ЙМОВІРНІСНИМ АЛГОРИТМОМ - Середній час роботи: {probabilistic_avg_time}, Середнє значення ЦФ: {probabilistic_avg_value}")

        print_and_save(f"ГЕНЕТИЧНИЙ АЛГОРИТМ - Середній час роботи: {ga_avg_time}, Середнє значення ЦФ: {ga_avg_value}\n")


def main():
    dimension_experiments()


if __name__ == "__main__":
    main()

from greedy_algorithm.GreedyAlgorithm import GreedyAlgorithm
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from application.Application import experiments_input
import time


def run_experiments():
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

        print(f"Для {n} товарів:")
        print(f"ЖАДІБНИЙ АЛГОРИТМ - Сердній час роботи: {greedy_avg_time}, Середнє значення ЦФ: {greedy_avg_value}")

        print(f"ЙМОВІРНІСНИМ АЛГОРИТМОМ - Сердній час роботи: {probabilistic_avg_time}, Середнє значення ЦФ: {probabilistic_avg_value}")

        print(f"ГЕНЕТИЧНИЙ АЛГОРИТМ - Сердній час роботи: {ga_avg_time}, Середнє значення ЦФ: {ga_avg_value}")


def main():
    run_experiments()


if __name__ == "__main__":
    main()

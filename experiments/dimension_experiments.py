from greedy_algorithm.GreedyAlgorithm import GreedyAlgorithm
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from application.Application import experiments_input, print_and_save
import time
import matplotlib.pyplot as plt


def dimension_experiments():
    dimensions = list(range(10, 101, 10))
    greedy_times = []
    greedy_values = []
    probabilistic_times = []
    probabilistic_values = []
    ga_times = []
    ga_values = []

    for n in dimensions:
        temp_greedy_times = []
        temp_greedy_values = []
        temp_probabilistic_times = []
        temp_probabilistic_values = []
        temp_ga_times = []
        temp_ga_values = []

        for _ in range(20):
            m, P, V, products = experiments_input(n)

            start_time = time.time()
            greedy_total, _ = GreedyAlgorithm.run(m, P, V, products)
            end_time = time.time()
            temp_greedy_times.append(end_time - start_time)
            temp_greedy_values.append(greedy_total)

            start_time = time.time()
            probabilistic_total, _ = ProbabilisticAlgorithm.run(m, P, V, products)
            end_time = time.time()
            temp_probabilistic_times.append(end_time - start_time)
            temp_probabilistic_values.append(probabilistic_total)

            ga = GeneticAlgorithm()
            start_time = time.time()
            ga_total, _ = ga.run(m, P, V, products)
            end_time = time.time()
            temp_ga_times.append(end_time - start_time)
            temp_ga_values.append(ga_total)

        greedy_avg_time = sum(temp_greedy_times) / len(temp_greedy_times)
        greedy_avg_value = sum(temp_greedy_values) / len(temp_greedy_values)
        probabilistic_avg_time = sum(temp_probabilistic_times) / len(temp_probabilistic_times)
        probabilistic_avg_value = sum(temp_probabilistic_values) / len(temp_probabilistic_values)
        ga_avg_time = sum(temp_ga_times) / len(temp_ga_times)
        ga_avg_value = sum(temp_ga_values) / len(temp_ga_values)

        greedy_times.append(greedy_avg_time)
        greedy_values.append(greedy_avg_value)
        probabilistic_times.append(probabilistic_avg_time)
        probabilistic_values.append(probabilistic_avg_value)
        ga_times.append(ga_avg_time)
        ga_values.append(ga_avg_value)

        print_and_save(f"Для {n} товарів:")
        print_and_save(
            f"ЖАДІБНИЙ АЛГОРИТМ - Середній час роботи: {greedy_avg_time}, Середнє значення ЦФ: {greedy_avg_value}")
        print_and_save(
            f"ЙМОВІРНІСНИЙ АЛГОРИТМ - Середній час роботи: {probabilistic_avg_time}, Середнє значення ЦФ: {probabilistic_avg_value}")
        print_and_save(
            f"ГЕНЕТИЧНИЙ АЛГОРИТМ - Середній час роботи: {ga_avg_time}, Середнє значення ЦФ: {ga_avg_value}\n")

    # Побудова графіків
    plt.figure(figsize=(12, 6))

    # Графік часу виконання
    plt.subplot(1, 2, 1)
    plt.plot(dimensions, greedy_times, marker='o', label='Жадібний алгоритм')
    plt.plot(dimensions, probabilistic_times, marker='o', label='Ймовірнісний алгоритм')
    plt.plot(dimensions, ga_times, marker='o', label='Генетичний алгоритм')
    plt.title('Час виконання алгоритмів')
    plt.xlabel('Кількість товарів')
    plt.ylabel('Час виконання (секунди)')
    plt.legend()
    plt.grid(True)

    # Графік значення цільової функції
    plt.subplot(1, 2, 2)
    plt.plot(dimensions, greedy_values, marker='o', label='Жадібний алгоритм')
    plt.plot(dimensions, probabilistic_values, marker='o', label='Ймовірнісний алгоритм')
    plt.plot(dimensions, ga_values, marker='o', label='Генетичний алгоритм')
    plt.title('Значення цільової функції')
    plt.xlabel('Кількість товарів')
    plt.ylabel('Значення цільової функції')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()



def main():
    dimension_experiments()


if __name__ == "__main__":
    main()

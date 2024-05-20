from application.Application import experiments_input, print_and_save
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
import matplotlib.pyplot as plt


def iterations_count_experiments():
    count_experiments = 10
    N = [10, 25, 50, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 5000, 7000, 10000, 15000, 25000, 30000]
    n = 50
    totals = [0] * len(N)
    for i in range(count_experiments):
        m, P, V, products = experiments_input(n)
        for i in range(len(N)):
            total_value, selected_products = ProbabilisticAlgorithm.run(m, P, V, products, N[i])
            totals[i] += total_value
    avgs = [total / count_experiments for total in totals]
    for i, avg in enumerate(avgs):
        print_and_save(f"Кількість ітерацій {N[i]} - середнє значення {avg}")

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(N, avgs, marker='o', linestyle='-', color='b')

    # Додавання підписів та заголовка
    plt.title('Залежність середнього значення від кількості ітерацій')
    plt.xlabel('Кількість ітерацій')
    plt.ylabel('Середнє значення')
    plt.grid(True)

    # Показати графік
    plt.show()


def main():
    iterations_count_experiments()


if __name__ == "__main__":
    main()

from application.Application import experiments_input
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm


def test_population_size():
    count_experiments = 1000
    N = [10, 25, 50, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 5000, 7000, 10000]
    n = 50
    totals = [0] * len(N)
    for _ in range(count_experiments):
        m, P, V, products = experiments_input(n)
        for i in range(len(N)):
            total_value, selected_products = ProbabilisticAlgorithm.run(m, P, V, products, N[i])
            totals[i] += total_value
    avgs = [total / count_experiments for total in totals]
    for i, avg in enumerate(avgs):
        print(f"Кількість ітерацій {N[i]} - середнє значення {avg}")


def main():
    test_population_size()


if __name__ == "__main__":
    main()

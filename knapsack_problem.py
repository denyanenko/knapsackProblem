from greedy_algorithm.GreedyAlgorithm import GreedyAlgorithm
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from application.Application import *
from experiments import dimension_experiments, iterations_count_experiments, population_size_experiments


def main():
    print("Головне меню")
    while True:
        print("1 - Робота з ІЗ")
        print("2 - Провести експерименти")
        print("0 - Завершити роботу")
        choice = int(input("Введіть ваш вибір (1/2/0): "))

        if choice == 1:
            n, m, P, V, products = choose_input_method()()
            print_individual_task(m, P, V, products)

            print_and_save("\nРОЗВ'ЯЗОК ЖАДІБНИМ АЛГОРИТМОМ\n")
            total_value, selected_products = GreedyAlgorithm.run(m, P, V, products)
            print_solution(total_value, selected_products, products)

            print_and_save("\nРОЗВ'ЯЗОК ЙМОВІРНІСНИМ АЛГОРИТМОМ\n")
            total_value, selected_products = ProbabilisticAlgorithm.run(m, P, V, products)
            print_solution(total_value, selected_products, products)

            print_and_save("\nРОЗВ'ЯЗОК ГЕНЕТИЧНИЙ АЛГОРИТМОМ\n")
            total_value, selected_products = GeneticAlgorithm().run(m, P, V, products)
            print_solution(total_value, selected_products, products)
            return

        elif choice == 2:
            experiments = {
                1: dimension_experiments,
                2: iterations_count_experiments,
                3: population_size_experiments
            }

            while True:
                print("\nОберіть експеримент:")
                print("1. Розмірність задачі")
                print("2. Кількість ітерацій ймовірнісного алгоритму")
                print("3. Розмір популяції генетичного алгоритму")
                choice = input("Введіть ваш вибір (1/2/3): ")
                if choice in ['1', '2', '3']:
                    experiments[int(choice)]()
                    return
                else:
                    print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")

        elif choice == 0:
            return
        else:
            print("Невірний вибір. Будь ласка, введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()

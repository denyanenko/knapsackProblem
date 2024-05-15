from greedy_algorithm.GreedyAlgorithm import GreedyAlgorithm
from probabilistic_algorithm.ProbabilisticAlgorithm import ProbabilisticAlgorithm
from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from application.Application import *


def main():
    n, m, P, V, products = choose_input_method()()
    print_individual_task(m, P, V, products)

    print("\nРОЗВ'ЯЗОК ЖАДІБНИМ АЛГОРИТМОМ\n")
    total_value, selected_products = GreedyAlgorithm.run(m, P, V, products)
    print_solution(total_value, selected_products, products)

    print("\nРОЗВ'ЯЗОК ЙМОВІРНІСНИМ АЛГОРИТМОМ\n")
    total_value, selected_products = ProbabilisticAlgorithm.run(m, P, V, products)
    print_solution(total_value, selected_products, products)

    print("\nРОЗВ'ЯЗОК ГЕНЕТИЧНИЙ АЛГОРИТМОМ\n")
    total_value, selected_products = GeneticAlgorithm().run(m, P, V, products)
    print_solution(total_value, selected_products, products)


if __name__ == "__main__":
    main()

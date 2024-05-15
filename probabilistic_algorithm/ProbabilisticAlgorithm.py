from random import random


class ProbabilisticAlgorithm:
    @staticmethod
    def probability_calculator(products):
        probability_estimates = []
        total_estimate = 0
        for product in products:
            weight, volume, value = product
            probability_estimate = value / (weight * volume)
            probability_estimates.append(probability_estimate)
            total_estimate += probability_estimate
        probabilities = []
        probability = 0
        for i in range(len(probability_estimates) - 1):
            probability += probability_estimates[i] / total_estimate
            probabilities.append(probability)
        return probabilities

    @staticmethod
    def calculate_number_of_product(probabilities):
        new_random = random()
        for i in range(len(probabilities)):
            if new_random < probabilities[i]:
                return i
        return len(probabilities)

    @staticmethod
    def probabilistic_algorithm(m, P, V, products):
        total_value = 0  # Загальна вартість товарів на складі
        selected_products = []  # Список вибраних товарів для кожного стелажу

        # Перебираємо всі стелажі
        for i in range(m):
            shelf_capacity = P[i]  # Максимальна вага на даному стелажі
            shelf_volume = V[i]  # Максимальний об'єм на даному стелажі
            shelf_value = 0  # Вартість товарів на даному стелажі
            products_on_shelf = []  # Товари на даному стелажі
            available_products = []

            for product in products:
                weight, volume, _ = product
                if (weight <= shelf_capacity and volume <= shelf_volume):
                    available_products.append(product)

            while len(available_products) > 0:
                probabilities = ProbabilisticAlgorithm.probability_calculator(available_products)
                selected_product = available_products[ProbabilisticAlgorithm.calculate_number_of_product(probabilities)]
                weight, volume, value = selected_product
                products_on_shelf.append(selected_product)
                shelf_capacity -= weight
                shelf_volume -= volume
                shelf_value += value
                products.remove(selected_product)
                available_products.remove(selected_product)

                for product in available_products[:]:
                    weight, volume, _ = product
                    if (weight > shelf_capacity or volume > shelf_volume):
                        available_products.remove(product)

            total_value += shelf_value
            selected_products.append(products_on_shelf)
        return total_value, selected_products

    @staticmethod
    def run(m, P, V, products, N=500):
        max_value = 0
        max_selected_products = []
        for i in range(N):
            total_value, selected_products = ProbabilisticAlgorithm.probabilistic_algorithm(m, P, V, products.copy())
            if max_value < total_value:
                max_value = total_value
                max_selected_products = selected_products
        return max_value, max_selected_products

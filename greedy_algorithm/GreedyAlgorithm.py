class GreedyAlgorithm:
    @staticmethod
    def run(m, P, V, products):
        products = products.copy()
        products.sort(key=lambda x: x[2], reverse=True)  # Сортуємо товари за вартістю

        total_value = 0  # Загальна вартість товарів на складі
        selected_items = []  # Список вибраних товарів для кожного стелажу

        # Перебираємо всі стелажі
        for i in range(m):
            shelf_capacity = P[i]  # Максимальна вага на даному стелажі
            shelf_volume = V[i]  # Максимальний об'єм на даному стелажі
            shelf_value = 0  # Вартість товарів на даному стелажі
            items_on_shelf = []  # Товари на даному стелажі

            # Додаємо товари на стелаж, починаючи з найбільш вигідних
            for product in products:
                weight, volume, value = product
                if weight <= shelf_capacity and volume <= shelf_volume:
                    items_on_shelf.append(product)
                    shelf_capacity -= weight
                    shelf_volume -= volume
                    shelf_value += value
                    products.remove(product)

            total_value += shelf_value
            selected_items.append(items_on_shelf)

        return total_value, selected_items

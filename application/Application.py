from random import uniform, randint


class Application:
    def manual_input(self):
        m = int(input("Введіть кількість полиць (m): "))
        P = [float(input(f"Введіть максимальну вагу для полиці {i + 1}: ")) for i in range(m)]
        V = [float(input(f"Введіть максимальний об'єм для полиці {i + 1}: ")) for i in range(m)]
        n = int(input("Введіть кількість товарів (n): "))
        products = []
        for i in range(n):
            weight, volume, value = map(float, input(
                f"Введіть вагу, об'єм та вартість для товару {i + 1} (через пробіл): ").split())
            products.append((weight, volume, value))
        return n, m, P, V, products

    def random_input(self):
        m = int(input("Введіть кількість стелажів (m): "))
        n = int(input("Введіть кількість товарів (n): "))
        P = [(round(uniform(5 * n / 1.1 ** m, 15 * n / 1.1 ** m), 1)) for _ in range(m)]
        V = [(round(uniform(0.5 * n / 1.1 ** m, 1.5 * n / 1.1 ** m), 1)) for _ in range(m)]
        products = [(round(uniform(10, 50), 1), round(uniform(1, 5), 1), randint(30, 70)) for _ in
                    range(n)]  # Випадкові товари
        return n, m, P, V, products

    def experiments_input(self, n):
        m = 4
        P = [(round(uniform(5 * n / 1.1 ** m, 15 * n / 1.1 ** m), 1)) for _ in range(m)]
        V = [(round(uniform(0.5 * n / 1.1 ** m, 1.5 * n / 1.1 ** m), 1)) for _ in range(m)]
        products = [(round(uniform(10, 50), 1), round(uniform(1, 5), 1), randint(30, 70)) for _ in
                    range(n)]  # Випадкові товари
        return m, P, V, products

    def read_input_from_file(self):
        filename = input("Введіть назву файлу для зчитування даних: ")
        with open(filename, 'r') as file:
            m = int(file.readline().strip())
            P = list(map(float, file.readline().strip().split()))
            V = list(map(float, file.readline().strip().split()))
            n = int(file.readline().strip())
            products = []
            for _ in range(n):
                weight, volume, value = map(float, file.readline().strip().split())
                products.append((weight, volume, value))
        return n, m, P, V, products

    def choose_input_method(self):

        input_methods = {
            1: self.manual_input,
            2: self.random_input,
            3: self.read_input_from_file
        }

        while True:
            print("\nОберіть метод введення даних:")
            print("1. Введення вручну")
            print("2. Випадкове генерування")
            print("3. Зчитування з файлу")
            choice = input("Введіть ваш вибір (1/2/3): ")
            if choice in ['1', '2', '3']:
                return input_methods[int(choice)]
            else:
                print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")

    def print_products(self, products):
        for i, product in enumerate(products):
            self.print_product(product, i)

    def print_product(self, product, num):
        weight, volume, value = product
        self.print_and_save("Товар ", num + 1, ": вага ", weight, ", об'єм ", volume, ", вартість ", value, sep="")

    def print_individual_task(self, m, P, V, products):
        self.print_and_save("\nІндивідуальна задача:")
        self.print_and_save("Товари:")
        self.print_products(products)
        self.print_and_save("\nСтелажі:")
        for i in range(m):
            self.print_and_save("Стелаж ", i + 1, ": Вантажомісткість ", P[i], ", Об'єм ", V[i], sep="")

    def print_solution(self, total_value, selected_products, products):
        selected_list = [0] * len(products)
        self.print_and_save("Загальна вартість товарів:", total_value)
        self.print_and_save("\nРозподіл товарів по стелажам:")
        for i, shelf in enumerate(selected_products):
            self.print_and_save("\nСтелаж ", i + 1, ":", sep='')
            for product in shelf:
                for j, prod in enumerate(products):
                    if prod == product and selected_list[j] == 0:
                        self.print_product(product, j)
                        selected_list[j] = 1
                        break

    def print_and_save(self, *args, sep=' ', end='\n'):
        with open('output.txt', 'a') as f:
            text = sep.join(map(str, args))
            print(text, end=end)
            print(text, end=end, file=f)


open("output.txt", "w")
ap = Application()
manual_input = ap.manual_input
random_input = ap.random_input
read_input_from_file = ap.read_input_from_file
choose_input_method = ap.choose_input_method
print_products = ap.print_products
print_product = ap.print_product
print_individual_task = ap.print_individual_task
print_solution = ap.print_solution
experiments_input = ap.experiments_input
print_and_save = ap.print_and_save

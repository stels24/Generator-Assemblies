# Полагаю, что не совсем правильно оформил..... просто эксперементирую...

def get_perform_calculations(arithmetic_operations):  # Вызываем математический модуль

    print("                Задание 1 Фабрика функций")

    if arithmetic_operations == "addition":
        def addition(a, b):
            return a + b

        return addition
    elif arithmetic_operations == "subtraction":
        def subtraction(a, b):
            return a - b

        return subtraction
    elif arithmetic_operations == "multiplication":
        def multiplication(a, b):
            return a * b

        return multiplication
    elif arithmetic_operations == "division":
        def division(a, b):
            try:
                result = a / b
            except ZeroDivisionError as errors_division:
                return errors_division
            else:
                return result

        return division


my_addition = get_perform_calculations("addition")
my_division = get_perform_calculations("division")
my_subtraction = get_perform_calculations("subtraction")
my_multiplication = get_perform_calculations("multiplication")

print("Деление : {}".format(my_division(10, 5)))
print("Сложение : {}".format(my_addition(5, 6)))
print("Вычитание : {}".format(my_subtraction(7, 5)))
print("Умножение : {}".format(my_multiplication(5, 6)))
print("Деление : {}".format(my_division(5, 0)))

print("                Задание 2 лямбда")


def to_square_def(x, y):
    return x ** y


to_square = lambda x, y: x ** y

print(f'Результат возведения в степень с помощью def :->{to_square_def(3, 6)}')
print(f'Результат возведения в степень с помощью lambda :->{to_square(1, 3)}')

print("                Задание 3 Вызываемые объекты")

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area_of_rectangle = Rectangle(4, 7)

print(f"Площадь прямоугольника со сторонами"
      f" {area_of_rectangle.a} и {area_of_rectangle.b} -> {area_of_rectangle.__call__()}")
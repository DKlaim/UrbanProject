# Для реализации простых одноразовых функций используют lambda-функции
# Пример 1: lambda-функция

my_func = lambda x: x + 10

print(type(my_func))
print(my_func(x=12))
print()

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(my_numbers)

result = map(lambda x: x + 10, my_numbers)
print(list(result))
print()

# Пример 2: lambda-функция может принимать как несколько параметров, так и не одного
they_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))
print()

# Лямбда форма функции имеет ограниченное применение:
# - Она создаётся в процессе выполнения кода (а не при компиляции) и может просадить быстродействие
# - Она плохо сериализуется - могут быть проблемы в крупных фреймворках
# - Не надо пытаться записать в лямбду сложные выражения: если там 3-5 операций - надо делать def
# - Лямбда-функция не имеет имени кроме <lambda>, поэтому на неё нельзя сослаться
print(my_func.__name__)
print()


# Пример 3: Создание функции внутри функции
def get_multiplier_v1(n):  # get_multiplier_v1 - функция высшего порядка, она вызывает другие функции
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Я могу сделать умножители только на 2 или 3!')

    return multiplier


by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)

result = map(by_2, my_numbers)
print(list(result))

result = map(by_3, my_numbers)
print(list(result))
print()


# Пример 4: Создание функции внутри функции с замыканием переменных
# Замыкание в Python - это функциональный объект, который запоминает значения во внешних областях, даже если они отсутствуют в памяти
def get_multiplier_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


by_5 = get_multiplier_v2(5)
print(by_5(x=12))

by_10 = get_multiplier_v2(10)
by_100 = get_multiplier_v2(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))
print()

# Пример 5: Не стоит передавать в аргументы функций изменяемые объекты и замыкать их
from pprint import pprint


def matrix(some_list):
    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column


matrix_on_my_numbers = matrix(my_numbers)

result = map(matrix_on_my_numbers, they_numbers)
pprint(list(result))
print()

my_numbers.extend([10, 20, 30])  # Если мы захотим увеличить список, то не вызовется никакая ошибка!
result = map(matrix_on_my_numbers, they_numbers)
pprint(list(result))


# Пример 6: Создание объекта, который можно вызвать
class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если есть такой метод у класса, то его объект можно "вызвать" как функцию
        return x * self.n


by_100500 = Multiplier(n=100500)
result = by_100500(x=12)
print(result)

result = map(by_100500, my_numbers)
print(list(result))
print()

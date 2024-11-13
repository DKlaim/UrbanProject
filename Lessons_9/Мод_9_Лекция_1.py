# 1. Функция это объект, принадлежащий классу function
def get_russian_names():
    return ['Ваня', 'Коля', 'Маша', ]

print(type(get_russian_names))

print(get_russian_names.__name__)
print(get_russian_names())


print()
# 2. Функцию можно присвоить переменной
my_func = get_russian_names
print(my_func())
print(my_func.__name__)


print()
# 3. С функцией можно работать как с обычными объектами
def get_british_names():
    return ['Oliver', 'Jack', 'Harry', ]

name_getters = [get_russian_names, get_british_names]

for name_getter in name_getters:
    print(name_getter())


print()
# 4. *Функции*, принимающие на вход другие функции с аргументами - *Функции высшего порядка*
def adder(args):
    res = 0
    for number in args:
        res += number
    return res

def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res

def process_numbers(function, numbers):
    result = function(numbers)
    print(f'Получилось: {result}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

process_numbers(function=adder, numbers=my_numbers)
process_numbers(function=multiplier, numbers=my_numbers)


print()
# 5. *Функция* map - применяет функцию к каждому аргументу последовательности и формирует список её результатов
def mul_by_2(x):
    return x * 2

result = map(mul_by_2, my_numbers)
print(result)  # класс объекта
print(list(result))


print()
# 6. *Функция* filter - вычисляет функцию для каждого элемента и добавляет элемент в список результатов, только если функция вернёт True
def is_odd(x):
    return x % 2

result = filter(is_odd, my_numbers)
print(result)  # класс объекта
print(list(result))

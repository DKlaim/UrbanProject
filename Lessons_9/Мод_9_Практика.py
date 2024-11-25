# 1 - написать функцию, которая возвращает функцию повторения двух первых символов n раз
# 2 - создать массив функций и применить все функции поочерёдно к аргументу
# 3 - применить все функции поочерёдно к массиву аргументов


animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

print(('# 1'))
def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)
print(test_1(animal))
print(test_2(animal))
print()


print(('# 2'))
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)
print()


print(('# 3'))
fin_result_1 = [func(x) for func in repetitions for x in animals]  # порядок перебора имеет значение
fin_result_2 = [func(x) for x in animals for func in repetitions]

print(fin_result_1)
print(fin_result_2)
print()


# ЗАДАЧА - Есть функция, которая возвращает результат возведения числа a в степень b.
# Необходимо её ускорить, чтобы она не делала повторные вычисления.

def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}, внутренняя память={mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась! Ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше! Ответ = {mem[args]}'

    return wrapper


@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 3), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')

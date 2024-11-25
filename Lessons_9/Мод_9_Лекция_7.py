# Пример 1: Создание простого декоратора
def null_decorator(
        func):  # декоратор - это функция высшего порядка, которая принимает в качестве параметра другую функцию
    return func  # и возвращает третью


def greet():
    return 'Hello!'


greet = null_decorator(greet)  # переменной greet присваиваем значение задекорированной функции greet()
print(greet())

print('-------------------------')


# Пример 2: Для декорирования за один шаг, можно использовать синтаксис Python
def null_decorator_2(func):
    return func


@null_decorator_2
def greet_2():  # в данном случае функция greet_2 всегда будет работать как задекорированная
    return 'Hello!'


print(greet_2())

print('-------------------------')


# Пример 3: Почему внутри декоратора необходимо определять ещё одну функцию?
def uppercase(func):
    def wrapper():  # шаблон правильной конструкции декоратора...
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper  # ...чтобы всегда возвращать результатом функцию


# если декоратор вернёт не функцию, то в дальнейшем функция greet_3 перестанет вызываться как функция


# @uppercase  # оставляем возможность вызывать функцию без декорирования
def greet_3():
    return 'Hello!'


greet_dec = uppercase(greet)  # при декорировании функции через переменную, мы оставляем возможность...
print(greet_dec())
print(greet_3())  # ...вызывать функцию без декорирования

print('-------------------------')

# Пример 4:
import time
import sys


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работает {elapsed} секунд(ы)')
        return result

    return surrogate


@time_track
def digits(*args):
    total = 1
    for number in args:
        total += number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10**5)

result = digits(3141, 5926, 2718, 2818)
print(result)

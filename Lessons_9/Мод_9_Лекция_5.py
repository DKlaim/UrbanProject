# Пример 1: библиотека itertools
import sys
from itertools import repeat

ex_iterator = repeat('4', 100_000)
print(ex_iterator)  # переменная ex_iterator на данном этапе хранит в себе только "repeat('4', 100000)", без вычисления
print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')  # вычисление будет происходить только в моменте вызова

ex_str = '4' * 100_000  # а переменная ex_str на данном этапе уже хранит в себе вычисленное выражение
print(f'Размер списка - {sys.getsizeof(ex_str)}')  # соответственно занимает гораздо больше памяти

print('---------------------------')


# Пример 2: создаём свой собственный итератор
class Iter:

    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        # обнуляем счётчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя, т.к. сам объект должен быть итератором
        return self

    def __next__(self):
        # этот метод возвращает значения по требованию python (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return 'Подсчёт закончен'
        raise StopIteration()  # признак того, что возвращать больше нечего


obj = Iter()
print(obj)

for value in obj:
    print(value)

# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# Если в __next__ возникает исключение StopIteration, то значит в объекте больше нет элементов и цикл прекращается

print('---------------------------')


# Пример 3: функция ряда Фибоначчи и её реализация в собственном итераторе
def fibonacci(n):
    result = []  # результат будет сохраняться в список, что будет занимать больше памяти при бОльших значениях
    a, b, = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value)

print('---------------------------')


class Fibonacci:
    ''' Итератор последовательности Фибоначчи до N элементов '''

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b  # в данном же случае результат будет вычисляться в моменте
        return self.a


fibo_iterator = Fibonacci(10)
print(fibo_iterator)

for value in fibo_iterator:
    print(value)  # каждое значение вычисляется в момент вызова

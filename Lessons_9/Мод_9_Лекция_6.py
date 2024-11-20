# Пример 1: Создание простого генератора
def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1

obj = func_generator(10)
print(obj)


for i in obj:
    print(i)

print('-------------------------')

# Пример 2: Создание функции Фибоначчи
def fibonacci_v1(n):  # обычная функция
    result = []
    a, b, = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b  # сначала происходит вычисление и сохранение в список (занимает память)
    return result  # после всех вычислений возвращается результат


def fibonacci_v2(n):  # генератор
    a, b, = 0, 1
    for _ in range(n):
        yield a  # результат возвращается только в момент обращения к генератору
        a, b = b, a + b  # вычисление происходит только в моменте вызова генератора (в памяти ничего нет)


fib_1 = fibonacci_v1(10)
print(fib_1)

for value in fib_1:
    print(value)


fib_2 = fibonacci_v2(10)
print(fib_2)

for value in fib_2:
    print(value)


print('-------------------------')

# Пример 3: Можно сделать бесконечный вывод значений
def func_generator_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for value in func_generator_v3():
    print(value)
    if value > 10**6:  # вывод до определённого (большого) значения, но все расчёты очень быстрые
        break


# Пример 4: Пример скорости работы генератора
import time

start = time.time()

def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

for line in read_large_file('large_file.txt'):
    print(line)

fin = time.time()
print((fin-start) * 1000)

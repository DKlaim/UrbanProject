# Пример 1: Создание генератора декораторов
import time
import sys


def gen_dec(precision):  # 2. при обращении к генератору декоратора, создается генератор декоратора gen_dec
    def dec(func):
        def wrapper(*args, **kwargs):  # 5. при обращении к декоратору создается обработчик wrapper
            started_at = time.time()

            result = func(*args, **kwargs)

            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работает {elapsed} секунд(ы)')
            return result  # 8. после всех преобразований возвращаем результат

        return wrapper  # 6. возвращаем созданный обработчик wrapper

    return dec  # 3. возвращаем созданный декоратор


def digits(*args):  #
    total = 1
    for number in args:
        total += number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10 ** 5)  # функция расширяющая возможную длину строки

time_track_precision_4 = gen_dec(precision=4)  # 1. создаём декоратор с указанием количества знаков после запятой
digits = time_track_precision_4(digits)  # 4. создаём переменную - функцию, обёрнутую в декоратор
result = digits(3141, 5926, 2718, 2818)  # 7. при вызове обёрнутой в декоратор функции digits, данные передаются в обработчик wrapper
print(result)  # 9. вывод результата

print('-------------------------')


# Пример 2: Декорирование функции сразу при создании с помощью генератора декоратора
@gen_dec(precision=10)  # параметры для декоратора указываем при обращении к генератору декоратора
def digits_2(*args):
    total = 1
    for number in args:
        total += number ** 5000
    return len(str(total))

result_2 = digits_2(3141, 5926, 2718, 2818)
print(result_2)

print('-------------------------')

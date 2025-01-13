'''
- 'Exception': базовый класс для всех исключений.
- 'ValueError': возникает при некорректном значении.
- 'TypeError': возникает при несоответствии типов.
- 'IndexError': возникает при обращении к несуществующему индексу списка.
- 'KeyError': возникает при обращении к несуществующему ключу словаря.
- 'IOError': возникает при ошибках ввода/вывода.
'''

# Обработка общей ошибки, например: x = 1 / 0
# try:
#     x = 1 / 0
# except Exception:
#     print('Ошибка!')


# Обработка ошибки при неверном значении, например: x = int('abc')
# try:
#     x = int('abc')
# except ValueError:
#     print('Некорректное значение!')


# Обработка нескольких ошибок на примере: x = int('abc')
# try:
#     x = int('abc')
#     y = 'a' + 1
# except ValueError:
#     print('Некорректное значение!')
# except TypeError:
#     print('Некорректный тип!')


# try:
#     x = int('1')
# except ValueError:
#     print('Некорректное значение!')
# else:  # выполняется если ошибки нет
#     print('Ошибки нет.')


# try:
#     x = int('abc')
# except ValueError:
#     print('Некорректное значение!')
# finally:  # выполняется в любом случае
#     print('Обработка ошибок завершена.')


# Логирование при обработке ошибок (используется для обратной связи при разработке)
# import logging
#
# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     logging.exception('Произошла ошибка')


# Цепочка исключений (для сохранения контекста ошибки)
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Деление на ноль невозможно')
#     return a / b
#
# try:
#     result = divide(10, 0)
# except ZeroDivisionError as e:
#     print(e)


# Создание собственных классов исключений
# class MyCustomError(Exception):  # Создаём свой обработчик ошибки (унаследованный от базового класса Exception)
#     pass
#
# def do_smyh(value):
#     if value < 0:
#         raise MyCustomError('Значение не должно быть меньше нуля')
#     print(value)
#
# try:
#     do_smyh(-10)
# except MyCustomError as e:
#     print(e)

import math


class NegativeNumberError(Exception):
    """ Исключение для обработки отрицательных чисел. """
    pass


def get_square_root(value):
    if value < 0:
        raise NegativeNumberError('Квадратный корень из отрицательного числа не определён.')
        # Искусственно вызываем другое исключение для демонстрации
    if value == 13:
        raise RuntimeError('Непредвиденная ошибка для числа 13.')
    return math.sqrt(value)


def main():
    try:
        user_input = input('Введите число для вычисления квадратного корня: ')
        value = float(user_input)
        result = get_square_root(value)
    except ValueError:
        print('Ошибка: Введено некорректное значение. Пожалуйста, введите числовое значение.')
    except NegativeNumberError as e:
        print(f'Ошибка: {e}')
    except Exception as e:
        print(f'Неизвестная ошибка: {e}')
    else:
        print(f'Квадратный корень из {value} равен {result}')
    finally:
        print('Программа завершена.')


if __name__ == '__main__':
    main()

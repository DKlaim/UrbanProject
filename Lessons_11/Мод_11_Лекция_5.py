''' Системный пакет sys '''

import sys

# pprint(dir(sys))
print()

print('Операционная система:', sys.platform)
print('Путь к интерпретатору Python:', sys.executable)
print('Текущая версия Python:', sys.version)
print('Дополнительная информация об интерпретаторе:', sys.version_info)
print()
print('Список параметров командной строки:', *sys.argv)  # если она была задана
print()
print('Список адресов каталогов для поиска модулей во время импорта:', *sys.path, sep='\n')
print()
print('Словарь имён всех загруженных объектов модулей:', sys.modules, sep='\n')
print()

# __builtins__ - псевдо-модуль, содержащий встроенные в интерпретатор объекты (константы, исключения, функции)
print(__builtins__)


# pprint(dir(__builtins__))  # вывод списка всех переменных встроенных в Python


# Пример функции контроля версии интерпретатора Python
def func(x):
    if sys.version.split(' ')[0] == '3.12.5':
        return x + 10
    else:
        raise Exception('Недопустимая версия')


# print(func(10))


# sys используется не только для того, чтобы узнавать системную информацию, но и для решения ресурсоёмких задач
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


sys.setrecursionlimit(5000)  # расширяет стек рекурсии
sys.set_int_max_str_digits(5819)  # расширяет длину выводимой строки
print(factorial(2025))  # выдаст ошибку "maximum recursion depth exceeded"
print(sys.getsizeof(factorial))  # возвращает размер объекта (функции factorial) в байтах

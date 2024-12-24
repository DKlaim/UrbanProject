''' Интроспекция - способность объекта во время выполнения получить тип, доступные атрибуты и методы, а также другую
информацию, необходимую для выполнения дополнительных операций с объектом '''

import requests
import inspect
from pprint import pprint

# Встроенная помощь - help
# help(requests)  # документация библиотеки requests
# help(requests.get)  # документация метода get библиотеки requests

some_string = 'строка'
some_number = 123
some_list = [some_string, some_number]


def some_function(param, param_2='n/a'):
    print('Мои параметры:', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 321

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()
func = some_function


# Пример 1 - Атрибут класса __name__
print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(func.__name__)
print()


# Пример 2 - Тип объекта
print(type(some_number))
print(type(some_number) is int)
print(type(some_number) is list)
print(type(requests))
print(type(requests.get))
print()


# Пример 3 - Функция dir - возвращает отсортированный список атрибутов и методов, доступных для указанного объекта
print('=== some_number ===')
pprint(dir(some_number))

print()
print('=== some_list ===')
pprint(dir(some_list))

print()
print('=== some_function ===')
pprint(dir(some_function))

print()
print('=== SomeClass ===')
pprint(dir(SomeClass))

print()
print('=== some_object ===')
pprint(dir(some_object))

print()
print('=== requests ===')
pprint(dir(requests))

print()
print('=== Локальные атрибуты и методы ===')
# Без указания аргумента dir() выводит доступные в локальной области видимости
pprint(dir())
print()


# Пример 4 - Функция hasattr() - проверка на существование атрибута
attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))  # у объекта some_object нет атрибута attr_name - вывод False
print(hasattr(some_object, 'attribute_1'))  # у объекта some_object есть атрибут attribute_1 - вывод True
pprint(dir(some_object))  # посмотрим список атрибутов и методов объекта some_object
print()


# Пример 5 - Функция getattr() - получение атрибута
print(getattr(some_object, 'attribute_1'))
print()

print(help(getattr))  # посмотрим, что мы ещё можем использовать с функцией getattr
''' When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case. '''
print(getattr(some_object, 'attribute_2', 'Такого атрибута здесь нет!'))  # если атрибута нет, то выводится строка
print()

# Выведем типы всех атрибутов и методов библиотеки requests
for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))
print()


# Пример 6 - Функция callable() - проверка на возможность вызова объекта
print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))
print()


# Пример 7 - Функция isinstance() - проверка объекта на принадлежность указанному классу (является ли его экземпляром)
print(isinstance(some_number, str))
print(isinstance(some_number, int))
print(isinstance(some_number, SomeClass))
print(isinstance(some_object, SomeClass))
print()


# Пример 8 - Модуль inspect - модуль собирает удобные методы и классы для отображения интроспективной информации
# https://docs.python.org/3/library/inspect.html
print(inspect.ismodule(requests))  # проверка является ли requests модулем
print(inspect.ismodule(some_object))  # проверка является ли some_object модулем
print(inspect.isclass(requests))  # проверка является ли requests классом
print(inspect.isfunction(requests))  # проверка является ли requests функцией
print(inspect.isbuiltin(requests))  # проверка является ли requests встроенной функцией в Python

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)

a = 5  # a - глобальная переменная пространства модуля namespaces
print(a)

import math

print(math.sqrt(a))

print('Атрибуты глобального пространства имён модуля namespaces: ', globals())
'''
функция globals возвращает список атрибутов в глобальном пространстве имён
при выводе мы увидим, что в списке глобальных имён присутствует две переменных (помимо встроенных): a и math
но если импортировать math глобально (from math import *), то в глобальном пространстве имён появится огромное количество значений
таким образом мы из глобального пространства имён другого модуля переместим всё в глобальное пространство имён модуля namespaces
'''


def square(x):
    # global a  # если с помощью оператора global определить переменную a внутри функции, то локальная переменная a станет глобальной
    a = x ** 2  # в данном случае переменная a - локальная переменная и относится только к функции square
    print('Атрибуты локального пространства имён (функции square): ', locals())
    print('Атрибуты глобального пространства имён модуля namespaces: ', globals())
    return a

def square2(x):
    return a ** 2  # если внутри функции локальная переменная не определена, то функция будет брать значение переменной из глобального пространства имён


b = square(2)
c = square2(2)
print(a)  # a глобальная не равна a локальной из функции square
print(b)
print(c)
print('Атрибуты глобального пространства имён модуля namespaces: ', globals())
print()


'''
Существует 4 области видимости:
    локальная - пространство имён внутри функции;
    объемлющая - пространство имён внутри функции, которая имеет внутри себя другие функции;
    глобальная - пространство имён вне функции;
    встроенная (системная) - пространство имён вне модуля
'''
from Lessons_4.mod_packs.module3 import b  # встроенная/системная переменная для функций square3 и event
d = 7  # глобальная переменная для функций square3 и event
def square3(x):
    d = x ** 2  # локальная переменная функции square3 и объемлющая для функции event
    def event(x):
        # nonlocal d  # nonlocal - определяет переменные как не локальные, тем самым заставляя интерпретатор искать значения в объемлющем пространстве имён
        # d = d / 2
        d = x * 2  # локальная переменная функции event
        if d % 2 == 0:
            print('Чётное')
        else:
            print('Нечётное')
    event(x)
    print(b)
    return d

print(square3(5))

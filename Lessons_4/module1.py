# Подключение стороннего модуля
from Lessons_4.mod_packs import module3 as m3
from mod_packs.modules import some_func as sf

print('Ответ модуля 1')


# print(dir(m3))
print(m3.a)
print(m3.b)
m3.say_hi()


# Глобальное импортирование элементов стороннего модуля
from Lessons_4.mod_packs.module3 import *  # можно импортировать как отдельные элементы, так и все с помощью *


print('Ответ модуля 2')


# При глобальном импортировании мы можем обращаться к элементам модуля без указания названия модуля
print(a)
print(b)
say_hi()
print()

print(sf())
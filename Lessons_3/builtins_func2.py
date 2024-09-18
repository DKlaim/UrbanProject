# Функция any - если хотя бы один объект True, то результат True

a = [1, 0, 0]
print(any(a))
a = [0, 1, 0]
print(any(a))
a = [0, 0, 0]
print(any(a))
print()
b = ''
print(any(b))
b = 'a'
print(any(b))
b = '0'
print(any(b))
print()

# Функция all - если все объекты True, то результат True
a = [1, 0, 0]
print(all(a))
a = [0, 1, 0]
print(all(a))
a = [0, 0, 0]
print(all(a))
print()
b = ''
print(all(b))
b = 'a'
print(all(b))
b = '0'
print(all(b))
print()

# Функции интраспекции - получение информации об атрибутах и методах объектов в процессе выполнения программы
a = [1, 1, 1]
b = ''
print(dir(a))  # dir - атрибуты объекта
print(dir(b))
print()
print(type(a))  # type - тип объекта
print(type(b))
print()
print(isinstance(b, str))  # isinstance - проверяем соответствует ли тип объекта указанному типу
print(type(b) == str)  # аналог строки выше
print()
c = [1, 1, 1]
print(a == c)  # проверяем соответствует ли содержимое одного объекта, содержимому другого
print(a is c)  # при этом "a" не является "c", т.к. ведут к разным объектам
print(id(a))
print(id(c))
d = c  # в таком случае "d" является "c"
print(id(d))
print(d == c)
print()
d[0] = 2  # изменив значение переменной "d", изменится значение в переменной "c"
print(d)
print(c)
print()

print(id(a))
print(id(c))
print(id(d))
print(c is d)
print()

# Числа и символы имеют одинаковые id
print(id(1))
a = 1
b = 1
print(id(a))
print(id(b))
print()

print(id('a'))
c = 'a'
d = 'a'
print(id(c))
print(id(d))
print()

# Функция help - Мануал в самом коде
print(help(print))
print('--------------------')


# Документирование собственных функций
def helper():
    """
    Эта функция-помощник
    """
    pass


print(help(helper))  # функция help выводит строку документирования функции helper()
print(helper.__doc__)  # метод .__doc__ также выводит строку документирования функции helper()

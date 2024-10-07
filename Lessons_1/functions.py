# Обычная функция. Названия функций начинаются с глагола
def say_hello():
    print('Hello!')

say_hello()

print('---------------------')

# Принимающая функция
def say_hello_name(name):
    print(f'Hello, {name}!')

say_hello_name('Денис')
say_hello_name('Макс')
say_hello_name('Антон')

print('---------------------')

# Возвращающая функция
import random
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets)
    return win

win = lottery()
print(win)

print('---------------------')

# Принимающевозвращающая функция
def lottery2(mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2

win1, win2 = lottery2('mon', 'thue')
print(win1, win2)

print('---------------------')

# Если не знаем сколько параметров будет принимать функция, то можем применить *args или **kwargs
def lottery3(*args, **kwargs):  # *args для обычных параметров; **kwargs для именованных
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2

win1, win2 = lottery3(1,2,3,4,5,6,7,8,9,10)
print(win1, win2)

print('---------------------')

# Значения по умолчанию в принимающих функциях
def test(a=5, b=True):
    print(a, b)

test()
test(1, 2)
test(10)
test(' ', 3)
test(8, '')

print('---------------------')

test([1, 2])  # можно передать список

test(*[1, 2])  # распаковка списка

print('---------------------')

# Также можно передавать и распаковывать словари
dict_ = {
    'a': 123,
    'b': 234
}

test(dict_)  # передаём словарь

test(**dict_)  # распаковка словаря

print('---------------------')

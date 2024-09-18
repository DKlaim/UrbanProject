# int()     - целые числа
# float()   - числа с плавающей точкой
# bool()    - логические значения True/False
print(bool(1))
print(bool(0))
print(bool('a'))
print(bool(''))
print(bool(None))

type = None
if type:
    print('on')
else:
    print('off')

type = 'None'
if type:
    print('on')
else:
    print('off')

# str()     - строки
# list()    - списки
print(list('abcdef'))

# tuple()   - кортежи
print(tuple('abcdef'))

# set()     - множества
print(set('abcdef'))

# dict()    - словари

salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary) / len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = zip(names, salary)
print(zipped)
print(list(zipped))

zipped = zip(names, salary)
print(dict(zipped))

zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')

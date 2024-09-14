for _ in 1, 2, 3, 4:
    print('Hi!')

print('---------------------')

for i in 1, 2, 3, 4:
    print(i)

print('---------------------')

for i in 'hello':
    print(i)

print('---------------------')

list_ = ['один', 'два', 'три', 'четыре']
for i in list_:
    print(i)

print('---------------------')

list_ = ['один', 'два', 'три', 'четыре']
for i in list_:
    if i == 'четыре':
        list_.remove(i)
print(list_)

print('---------------------')

for i in range(5):
    print(i)

print('---------------------')

print(list_)
for i in range(len(list_)):
    print(list_[i],'- индекс', i)

print('---------------------')

for i in range(1, 11):  # range(start, stop, step) - функция range принимает три параметра: начало последовательности, конец последовательности и шаг
    print(i, 'X', 1, '=', i * 1)
    print(i, 'X', 2, '=', i * 2)
    print(i, 'X', 3, '=', i * 3)
    print(i, 'X', 4, '=', i * 4)
    print(i, 'X', 5, '=', i * 5)
    print(i, 'X', 6, '=', i * 6)
    print(i, 'X', 7, '=', i * 7)
    print(i, 'X', 8, '=', i * 8)
    print(i, 'X', 9, '=', i * 9)
    print(i, 'X', 10, '=', i * 10)
    print('=============')

print('---------------------')

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} X {j} = {i * j}')
    print('=============')

print('---------------------')

dict_ = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

for i in dict_:
    print(f'Ключ: {i} - значение: {dict_[i]}')

print('=============')

for i, j in dict_.items():
    print(f'Ключ: {i} - значение: {j}')

print('---------------------')


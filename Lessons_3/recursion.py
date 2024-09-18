# Пример рекурсивной функции
def summa(n):
    if n == 0:
        return 0 # - точка выхода из рекурсии (ОБЯЗАТЕЛЬНА!)
    else:  # далее идёт пример рекурсии - вызов функцией саму себя (любую рекурсию можно заменить циклом и наоборот)
        return n + summa(n - 1)  # При каждом вызове функции мы забиваем стек вызовов (область памяти, где хранятся точки перехода - место, где компьютер "отвлекается" на выполнение какой-то функции в процессе выполнения основной программы)
                                 # в стеке хранятся основные данные (переменные, аргументы функции, а также адрес возврата - то место куда компьютер должен перейти после выполнения подпрограммы)
print(summa(5))
print(5 + 4 + 3 + 2 + 1)
print()

# # Пример без выхода из рекурсии (так делать не надо!)
# def recursion():
#     recursion()
#
# recursion()


print('Наглядный пример стека')
stack = []

print(f'Собираем пирамидку: {stack}')
stack.append(1)
print(f'Добавили элемент  - {stack}')
stack.append(2)
print(f'Добавили элемент  - {stack}')
stack.append(3)
print(f'Добавили элемент  - {stack}')
print()
print(f'{stack} - Разбираем пирамидку')
stack.pop()
print(f'{stack} - Убрали элемент')
stack.pop()
print(f'{stack} - Убрали элемент')
stack.pop()
print(f'{stack} - Убрали элемент')
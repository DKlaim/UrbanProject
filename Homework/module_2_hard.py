import random

# Дано
random_number = random.randint(3, 20)


# Делаем выборку всех возможных пар чисел для любого числа больше 2
def couples(value):
    couples_list = ''
    for i in range(1, value):
        for j in range(1, value):
            if value % (i + j) == 0 and (i + j) > 2:
                couples_list += f'{i}{j}'
    return couples_list


# Вывод результата
print(f'Число в первой ячейке: {random_number}')
print(f'Пароль: {couples(random_number)}')

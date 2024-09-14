import random


# Создаём список чисел от 1 до 21
def numeric_list():
    num_list = []
    for i in range(1, 21):
        num_list.append(i)
    return num_list


# Получаем случайное число в первой ячейке из диапазона от 3 до 20
first_window = random.choice(numeric_list()[2:])


# Получаем пароль да случайного числа, состоящий из уникальных пар чисел
def password(num_set, first_win):
    passwd = ''
    n = 0
    k = 1
    # Делаем выборку всех возможных пар чисел для удовлетворения условия задачи
    while n < first_win:
        for j in range(k, first_win):
            if first_win % (num_set[n] + num_set[j]) == 0:
                passwd += str(num_set[n]) + '/' + str(num_set[j]) + ' '  # Добавлены разделители для наглядной демонстрации
        n += 1
        k = 0
    return passwd


print(f'Число в первой ячейке: {first_window}')
print(f'Пароль: {password(numeric_list(), first_window)}')

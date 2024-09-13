import random


# Создаём список чисел от 1 до 21
def numeric_list():
    num_list = []
    for i in range(1, 21):
        num_list.append(i)
    return num_list


# Получаем случайное число в первой ячейке из диапазона от 3 до 20
first_window = random.choice(numeric_list()[2:])


# Получаем пары да случайного числа
def couples(first_win, num_set):
    couples_ = ''
    n = 0
    k = 1
    # Делаем выборку всех возможных пар чисел для удовлетворения условия задачи
    while n < first_win:
        for j in range(k, first_win):
            if first_win % (num_set[n] + num_set[j]) == 0:
                couples_ += str(num_set[n]) + '/' + str(
                    num_set[j]) + ' '  # Разделители для более наглядной демонстрации
        n += 1
        k = 0
    return couples_


couples = (couples(first_window, numeric_list()))
print(f'Число в первой ячейке: {first_window}')
print(f'Пары: {couples}')
print('Пароль:', couples.replace('/', '').replace(' ', ''))

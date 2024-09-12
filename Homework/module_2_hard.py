import random

numeric_set = []

# Создаём список чисел от 1 до 20
for i in range(1, 21):
    numeric_set.append(i)

# Получаем случайное число в первой ячейке из диапазона от 3 до 20
first_window = random.choice(numeric_set[2:])

print(f'Число в первой ячейке: {first_window}')


# Делаем выборку всех возможных комбинаций цифр для удовлетворения условия задачи
def password(num_set, first_win):
    passwd = ''
    n = 0
    k = 1
    while n < first_win:
        for j in range(k, first_win):
            if first_win % (num_set[n] + num_set[j]) == 0:
                passwd += str(num_set[n]) + str(num_set[j])
        n += 1
        k = 0
    return passwd


print(f'Пароль: {password(numeric_set, first_window)}')
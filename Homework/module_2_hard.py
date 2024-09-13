import random

# Дано
number_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_number = random.choice(number_list)


# Делаем выборку всех возможных пар чисел для любого числа больше 3
def couples(value):
    couples_list = ''
    for i in range(1, value):
        for j in range(1, value):
            if value % (i + j) == 0 and (i + j) > 2:
                couples_list += str(i) + '/' + str(j) + ' '  # Разделители для более наглядной демонстрации
    return couples_list


# Вывод результата
def result(number):
    print(f'Число в первой ячейке: {number}')
    print(f'Пары: {couples(number)}')
    print('Пароль:', couples(number).replace('/', '').replace(' ', ''))


# Вывод решения задачи
result(random_number)

# Проверяем вывод пар для любого числа больше 3
n = 3
while n >= 3:
    print('-------------------- ПРОВЕРКА --------------------')
    n = int(input('Введите любое число от 3 до 20 или 0 для выхода: '))
    if n >= 3:
        result(n)
    else:
        break

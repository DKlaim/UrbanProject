my_list = [11, 2, 3, 6, 9, 8, 7, 10, 4, 5, 5, 4, 3, 1]
print(my_list)

def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

# Функция find_max сравнивает все элементы списка друг с другом и выдаёт значение максимального элемента
print(f'Максимальное число из списка: {find_max(my_list)}')

def count_event(list_):
    counter = 0
    for i in list_:
        if i % 2 == 0:
            counter += 1
    return counter

# Функция count_event сравнивает все элементы списка друг с другом и выдаёт количество чётных чисел в списке
print(f'Количество чётных чисел в списке: {count_event(my_list)}')

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(f'Список уникальных элементов: {unique(my_list)}')  # Функция unique выбирает из имеющегося списка неповторяющиеся элементы и создаёт список уникальных элементов

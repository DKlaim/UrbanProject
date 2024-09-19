def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

my_list = [11, 2, 3, 6, 9, 8, 7, 10, 4, 5]
print(find_max(my_list))  # Функция find_max сравнивает все элементы списка друг с другом и выдаёт значение максимального элемента


def count_event(list_):
    counter = 0
    for i in list_:
        if i % 2 == 0:
            counter += 1
    return counter

print(count_event(my_list))  # Функция count_event сравнивает все элементы списка друг с другом и выдаёт значение максимального элемента
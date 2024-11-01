from SortFunc.sort_func import insertion_sort, bubble_sort, selection_sort

# Создадим список из одной строки ввода
data_1 = list(map(int, input('Введите числа через пробел: ').split()))  # метод inpun создаёт строку, метод split создаёт из этой строки список по разделителю,
data_2 = list(map(int, input('Введите числа через пробел: ').split()))  # метод map конвертирует каждый элемент списка из строчного типа (str) в целочисленный (int),
data_3 = list(map(int, input('Введите числа через пробел: ').split()))  # а метод list переводит map-объект в читаемый список


bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print('Пример пузырьковой сортировки:', data_1)
print('Пример сортировки выборкой:', data_2)
print('Пример сортировки вставкой:', data_3)

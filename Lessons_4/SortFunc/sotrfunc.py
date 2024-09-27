# # Сортировка списка
# nums = [5, 6, 2, 1, 3, 4]

# Пример пузырьковой сортировки
def bubble_sort(ls):
    swapper = True
    while swapper:
        swapper = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]  # приём смены значений в переменных: a,b = b,a
                swapper = True
    return ls


# bubble_sort(nums)
# print(nums)


# nums = [5, 6, 2, 1, 3, 4]

# Пример сортировки выборкой
def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    return ls

# selection_sort(nums)
# print(nums)


# nums = [5, 6, 2, 1, 3, 4]

# Пример сортировки вставкой
def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


# insertion_sort(nums)
# print(nums)
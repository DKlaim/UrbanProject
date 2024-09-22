data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summa = 0


def calculate_structure_sum(datas):
    global summa  # глобальная переменная бля подсчёта общей суммы
    # Разделяем элементы на числа и строки для дальнейшего суммирования
    if isinstance(datas, int):
        summa += datas
    elif isinstance(datas, str):
        summa += len(datas)
    # Вычисляем списки/кортежи/множества для дальнейшего рекурсивного прогона
    elif isinstance(datas, list) or isinstance(datas, tuple) or isinstance(datas, set):
        for data in datas:
            calculate_structure_sum(data)
    # Вычисляем словари для дальнейшего рекурсивного прогона ключей и их значений
    elif isinstance(datas, dict):
        for key in datas:
            calculate_structure_sum(key)
            calculate_structure_sum(datas[key])

    return summa


result = calculate_structure_sum(data_structure)
print(result)

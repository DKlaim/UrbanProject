# Пример 1: как выглядит объединение функций map и filter

def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))
print()

collection = my_numbers
# Словарные и списковые сборки
# Пример 2: Генерация списка с помощью новой операции
list_comp_1 = [x * 2 for x in collection]  # только for - аналог map
print(list_comp_1)
print()

# Пример 3: Генерация списка с фильтрацией (только один if, без elif/else)
list_comp_2 = [x * 3 for x in collection if x % 2]  # комбинация функций map и filter
print(list_comp_2)
print()

# Пример 4: Генерация списка с изменением операции над элементом (условия перед циклом, для того чтобы не отфильтровать данные, а поменять операцию над ними)
list_comp_3 = [x * 2 if x > 2 else x * 10 for x in collection]
print(list_comp_3)
print()

my_numbers_2 = ['A', 1, 4, 'B', 5, 'C', 2, 6]
list_comp_4 = [x if type(x) == str else x * 5 for x in my_numbers_2]
print(list_comp_4)
print()

# Пример 5: Вложенные списки. Генерация для двух элементов
collection_1 = my_numbers
collection_2 = [1, 2, 3, 4, 5, 6, 7, 8]
list_comp_5 = [x * y for x in collection_1 for y in collection_2]
print(list_comp_5)
print()

list_comp_5 = [x * y for x in collection_1 for y in collection_2 if x % 2]
print(list_comp_5)
print()

list_comp_5 = [x * y for x in collection_1 for y in collection_2 if x % 2 and y // 2]
print(list_comp_5)
print()

# Пример 6: Можно создавать множества и словари на лету
set_1 = {x for x in collection_1}  # набор
print(set_1)
print()

dict_1 = {x: x ** 2 for x in collection_1}  # словарь
print(dict_1)
print()

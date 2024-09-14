tuple_1 = 1, 2, 3, 4
print(tuple_1, type(tuple_1))   # в результате получим кортеж (неизменяемый список/коллекцию)
                                # коллекции/кортежи - неизменяемые, упорядоченные, принимают разные типы элементов
tuple_2 = (4, 3, 2, 1)
print(tuple_2, type(tuple_2))

tuple_3 = tuple([1, 2, 3, 4])
print(tuple_3, type(tuple_3))


# кортежи занимают меньше памяти чем списки
list_1 = [1, 2, 3, 4]

print('Занято памяти в кортеже: ', tuple_1.__sizeof__())
print('Занято памяти в списке: ',list_1.__sizeof__())

tuple_4 = ([1, 2], 3)
print(tuple_4)

# сами элементы кортежа изменяемые
tuple_4[0][0] = 2
print(tuple_4)

# кортежи поддерживают конкатенацию
tuple_5 = tuple_1 + tuple_2
print(tuple_5)

# кортежи поддерживают умножение
tuple_6 = tuple_1 * 3
print(tuple_6)


######################
tuple_7 = ([0], [1], [2], [3], [4])
print(tuple_7)
print(tuple_7[0])
print(tuple_7[0][0])
tuple_7[0][0] = 10
print(tuple_7)

list_7 = list(tuple_7)
print(list_7)

print()
print('Занято памяти в кортеже: ', tuple_7.__sizeof__())
print('Занято памяти в списке: ',list_7.__sizeof__())
phone_book = {
    'Denis': 88001234556,
    'MaX': 88001236554
}
print(phone_book)
print(phone_book['MaX'])
print()

phone_book_1 = phone_book

phone_book['MaX'] = 6554
print(phone_book)
print()

phone_book['Anton'] = 88001237889
print(phone_book)
print()

del phone_book['Denis']
print(phone_book)
print()

phone_book.update({
    'Denis': 88001234556,
    'Sasha': 88001239887,
    'AleX': 88001234152
})
print(phone_book)
print()

print(phone_book.get('MaX')) # метод вывода значения по ключу
print()

print(phone_book.get('Neo')) # если ключа нет, то выведет None
print(phone_book.get('Neo', 'Такого ключа нет.')) # вместо None выводит указанную строку
print()

print(phone_book.setdefault('Neo', 'Такого ключа нет.')) # если ключа нет в словаре, то метод .setdefault добавит искомый ключ к паре со значением, указанным как альтернативный вывод при методе .get
print()

print('Словарь до применения метода .pop:\n', phone_book)
a = phone_book.pop('Anton') # метод .pop удаляет ключ и возвращает его значение
print('Словарь после применения метода .pop() с аргументом "Anton":\n', phone_book)
print('Значение ключа "Anton":', a)
print()

print('Список ключей словаря: ', phone_book.keys())
print('Список значений словаря: ', phone_book.values())
print('Список пар словаря: ', phone_book.items())
print()

phone_book['Denis'] = [88001234556, 4556]
print(phone_book)
print()

print('Словарь №1:', phone_book)
print('Словарь №2:', phone_book_1)
print('Проверка на равенство словарей №1 и №2:', phone_book == phone_book_1)
print()

print("Проверяем содержится ли ключ Мах в словаре:", 'MaX' in phone_book)
print("Проверка содержится ли значение 6554 ключа Мах в словаре не сработает:", 6554 in phone_book)
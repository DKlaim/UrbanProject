# Функция input #
string = input('Введите текст: ')
print(string, type(string))

string = input('Введите число: ')  # функция input всегда! создаёт строковый тип данных, для получения другого типа потребуется преобразование
print(string, type(string))
string = int(string)
print(string, type(string))
print()
print()

# Пример #
current_year = 2024

name = input('Введите Ваше имя: ')
data_of_birth = (int(input('Ваш год рождения: ')))

print()
print('Здравствуйте,', name + '!')


# Методы со строками #
print('СТРОКА В ВЕРХНЕМ РЕГИСТРЕ'.upper()) # перевод строки в верхний регистр

print('строка в нижнем регистре'.lower()) # перевод строки в нижний регистр

print('строка в нижнем регистре'.upper().lower()) # методы выполняются последовательно, соответственно итогом будет перевод строки в нижний регистр

print('В этом году Вам'.replace('Вам', 'тебе'),current_year - data_of_birth, 'лет.') # метод для замены символов


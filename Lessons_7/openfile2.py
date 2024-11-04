import io
from pprint import pprint

file_name = 'package2.txt'
file = open(file_name, 'r', encoding='utf-8')  # если возникают ошибки с кодировкой, то нужно указать encoding
print(file.tell())  # tell показывает положение курсора (но курсор работает со значениями в байтах)
pprint(file.read())
print(file.seek(10))  # seek смещает положение курсора
pprint(file.read())  # читаем файл с нового положения курсора
print(file.tell())

# Узнать в какой режиме открыт файл
print('Режим чтения:', file.readable())
print('Режим записи:', file.writable())
print('Возможность перемещать курсор:', file.seekable())
print('Файл закрыт:', file.closed)
file.close()

file = open(file_name, 'r+', encoding='utf-8')  # попробуем что-нибудь добавить в наш файл
print(file.seek(100))  # в область за пределами содержимого файла
file.write('\nnew text')  # новый текст добавился в конце файла
pprint(file.read())
print(file.tell())
file.close()
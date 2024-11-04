from pprint import pprint

file_name = 'package.txt'

# Режимы работы с файлами: r - чтение, w - запись, a - добавление
# Открытие файла для чтения
file = open(file_name, 'r')  # или file = open(file_name).read()

print(file)
# Для вывода содержимого файла на экран необходимо использовать конструкцию чтения:
pprint(file.read())

# Каждое открытие файла должно завершаться его закрытием
file.close()

# Открытие файла для записи
''' При открытии файла в режиме записи перезаписывает всё содержимое файла! '''
file_name = 'package2.txt'  # если открываемый файл не будет найден, то интерпретатор создаст новый файл
file = open(file_name, 'w')
file.write('new file')
file.close()

# Открытие файла для добавления информации
file_name = 'package2.txt'
file = open(file_name, 'a')
file.write('\nnew file2')  # метод write в режиме "a" (добавления) не перезаписывает содержимое файла, а добавляет новые данные
file.close()

# Также можно открывать бинарные файлы добавляя приставку "b"
file_name = 'package3'  # если открываемый файл не будет найден, то интерпретатор создаст новый файл
file = open(file_name, 'ab')
file.write(b'\x68')
file.close()

# Управление курсором
file_name = 'package2.txt'
file = open(file_name, 'r')
print(file.tell())  # tell показывает положение курсора
pprint(file.read())
print(file.seek(9))  # seek смещает положение курсора
pprint(file.read())
file.close()
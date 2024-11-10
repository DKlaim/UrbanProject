import os
from base64 import decode
from quopri import decodestring

print('Текущая директория:', os.getcwd())

os.mkdir('second')  # создаём новую папку - second
print(os.path.exists('second'))  # возвращает True, если папка second существует в нашем текущем окружении
print('Текущая директория:', os.getcwd())

os.chdir('second')  # изменяем текущее окружение на папку second (зашли в созданную ранее папку second)
print(os.path.exists('second'))
print('Текущая директория:', os.getcwd())

os.makedirs(r'third\fourth')  # создаём ветку вложенных папок - строка r'' позволяет использовать разделитель \ в WinOS
print(os.listdir())  # показывает содержимое нашего текущего окружения

# конструкция для просмотра вложенности содержимого относительно '.' - текущего окружения/папки/пространства
for i in os.walk('.'):
    print(i)

os.chdir(r'D:\UrbanProject\Lessons_7')  # переходим/меняем текущее окружение/пространство на Lessons_7
print(os.listdir())  # смотрим содержимое папки Lessons_7 (вывод не отсортирован)

# конструкция генератора списков для сортировки содержимого папки Lessons_7 на папки и файлы
dirs = [d for d in os.listdir() if os.path.isdir(d)]
files = [f for f in os.listdir() if os.path.isfile(f)]
print('Папки:', dirs)
print('Файлы:', files)

# запуск файла из программы
os.startfile('package.txt')  # по названию файла
os.startfile(files[5])  # по индексу файла

print(os.stat('package.txt'))  # общая информация о файле
print(os.stat('package.txt').st_size)  # конкретная информация о файле

os.system('pip list')  # запуск команды как в терминале OS
# os.system('python.exe -m pip install --upgrade pip')

"""
math - математические функции
random - генерация случайных чисел
datetime - работа с датой и временем
os - взаимодействие с ОС (например работа с файлами и директориями)
sys - взаимодействие с интерпретатором Python и системными настройками
json - работа с форматом данных JSON
urllib - работа с URL-адресами и выполнение HTTP-запросов
re - регулярные выражения
collections - дополнительные структуры данных (например OrderedDict, Counter)
itertools - инструменты для создания итераторов и операций с ними
sqlite3 - взаимодействие с базой данных SQLite
pickle - сериализация и десериализация объектов Python
csv - работа с файлами формата CSV
email - работа с электронной почтой
socket - низкоуровневая работа с сетевыми сокетами
argparse - обработка аргументов командной строки
logging - система логирования
subprocess - запуск и управление внешними процессами
"""

# Работа с датой (в date не включена работа со временем)
# from datetime import date
#
# my_date = date(1900, 1, 1)
# print(my_date)
# print(my_date.isoweekday())
# print(type(my_date))
# print(my_date.day)  # вывод числа дня
# print(my_date.month)  # вывод числа месяца
# print(my_date.year)  # вывод числа года
# print(date.min)  # вывод минимально допустимой даты
# print(date.max)  # вывод максимально допустимой даты
# print(my_date.toordinal())  # вывод номера дня
# print(my_date.fromordinal(724575))  # вывод даты по номеру дня

# today_date = date.today()  # сегодняшняя дата
# print(today_date)
# # print(today_date.weekday())  # день недели: 0 - понедельник, 1 - вторник и т.д
# print(today_date.isoweekday())  # день недели: 1 - понедельник, 2 - вторник и т.д
# print(today_date - my_date)
# print('-----------------------')
# my_dates = [my_date, date(2010,1,2), date(2020,1,10), date(2000,1,5)]
# print(my_dates)  # вывод списка дат
# print(*my_dates, sep='\n')  # распаковка списка дат в читаемом формате
# my_dict = {date(204, 12, 31): 'Новый год', date(1996, 7, 5): 'День рождения'}
# print(my_dict)
# print(min(my_dates))
# print(max(my_dates))
# print(sorted(my_dates))
# print('Сортировка по ключу day', *sorted(my_dates, key=lambda d: d.day), sep=', ')
# print('Сортировка по ключу month', *sorted(my_dates, key=lambda m: m.month), sep=', ')
# print('Сортировка по ключу year', *sorted(my_dates), sep=', ')
# print('-----------------------')
# my_date1 = my_date.replace(year=1999)  # замена значения года
# my_date2 = my_date.replace(month=1, day=2)  # замена значений месяца и дня
# print(my_date)
# print(my_date1)
# print(my_date2)
# print('-----------------------')

# Работа со временем (в time не включена работа с датой)
# from datetime import time
#
# my_time = time(10, 20, 30, 12345)
# print(my_time)
# print(type(my_time))
# my_time1 = time(10, 20, 30, 12345)
# my_time2 = time(10, 20, 30)
# my_time3 = time(10, 20)
# my_time4 = time(10)
# my_time5 = time()
# my_time6 = time(second=30)
# print(my_time1, my_time2, my_time3, my_time4, my_time5, my_time6, sep='\n')
# print(my_time1.hour)
# print(my_time1.minute)
# print(my_time1.second)
# print(time.min)
# print(time.max)
# print('-----------------------')
# print(my_time) # вывод в читаемом формате
# print(repr(my_time)) # вывод в компьютерном формате
# print(str(my_time)) # принудительный вывод в читаемом формате
# print('-----------------------')
# my_times = [my_time, time(1,2,3), time(10,20,30)]
# print(my_times) # вывод списка времени
# print(*my_times, sep='\n') # распаковка списка времени в читаемом формате
# print('-----------------------')
# my_set = {my_time, time(1,2,3), time(10,20,30)}
# print(my_set)

# Работа с библиотекой os
import os

print(os.name)  # имя системы
print(os.getcwd())  # директория в которой находимся
# os.chdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\')  # изменение текущей директории
# print(os.getcwd())
print(os.path.abspath('Мод_11_Лекция_1.py'))  # вывод абсолютного пути до файла/директории
print(os.path.exists('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Мод_11_Лекция_1.py'))  # проверка существования пути до файла/директории
print(os.path.isfile('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Мод_11_Лекция_1.py'))  # проверка существования файла
print(os.path.isdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Webinar\\NewDir'))  # проверка существования директории
os.mkdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Webinar\\NewDir')  # создание директории
print(os.path.isdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Webinar\\NewDir'))  # проверка существования директории
# os.remove('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Мод_11_Лекция_123.py')  # удаление файла
os.rmdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Webinar\\NewDir')  # удаление директории
print(os.path.basename('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Мод_11_Лекция_1.py'))  # получение имени файла из полного пути
# os.path.dirname()  # получение пути к файлу без названия
# os.path.split()  # разделить имя файла и путь
# os.path.join()  # объединить директорию и имя файла
print(os.path.getsize('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11\\Мод_11_Лекция_1.py'))  # получение размера файла в байтах
# os.rename()  # переименовать файл
print(os.listdir('C:\\Users\\klimchuk\\YandexDisk\\UrbanProject\\Lessons_11'))  # вывод содержания директории

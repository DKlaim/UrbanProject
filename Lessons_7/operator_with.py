import io
from pprint import pprint

file_name = 'text.txt'
file = open(file_name, 'w', encoding='utf-8')
file.write('new text\n')
file.write('новый текст 2\n')
file.close()

''' Формула оператора with:
with <выражение> as <объект куда сохраняется>:
    <действия которые выполняются>

После выполнения всех действий с файлом в теле оператора with - файл закрывается автоматически! 
'''
with open(file_name, encoding='utf-8') as file:
    # # Перебор файла построчно
    # for line in file:
    #     # print(line)
    #     print(line, end='')  # end='' - заменяет \n на пустое значение, в результате исключаются пустые строки при выводе

    # Перебор файла посимвольно (результат тот же)
    for line in file:
        for char in line:
            # print(char)
            print(char, end='')

file_name = 'text.txt'
string = 'мама мыла раму'

with open(file_name, mode='x', encoding='utf-8') as file:
    file.write(string)

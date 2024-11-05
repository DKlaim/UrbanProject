def custom_write(file_name, strings):
    file = file_name
    strings_positions = {}
    line_number = 0

    file = open(file, 'w', encoding='utf-8')
    for string in strings:
        line_number += 1
        strings_positions[(line_number, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

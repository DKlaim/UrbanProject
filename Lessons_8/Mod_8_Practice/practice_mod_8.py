def calc(line):
    value_1, action, value_2 = line.split()
    # print(value_1, action, value_2)
    value_1 = int(value_1)
    value_2 = int(value_2)
    # if action == '+':
    #     result = value_1 + value_2
    #     print(f'{value_1} {action} {value_2} = {result}')
    # elif action == '-':
    #     result = value_1 - value_2
    #     print(f'{value_1} {action} {value_2} = {result}')
    # elif action == '*':
    #     result = value_1 * value_2
    #     print(f'{value_1} {action} {value_2} = {result}')
    # elif action == '/':
    #     result = value_1 / value_2
    #     print(f'{value_1} {action} {value_2} = {result}')
    # elif action == '//':
    #     result = value_1 // value_2
    #     print(f'{value_1} {action} {value_2} = {result}')
    # elif action == '%':
    #     result = value_1 % value_2
    #     print(f'{value_1} {action} {value_2} = {result}')


cnt = 0
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в строке {cnt}: "Недостаточно значений для решения"')
            elif 'invalid' in exc.args[0]:
                print(f'Ошибка в строке {cnt}: "Невозможно перевести аргумент в десятичное число"')

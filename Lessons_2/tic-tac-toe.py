area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

def draw_area():
    for i in area:
        print(*i)


print('-------------------------')
print('XoX КРЕСТИКИ / НОЛИКИ oXo')
print('-------------------------')
draw_area()
print('-------------------------')


def check_winner():
    if ((area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X') or
       (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X') or
       (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X') or
       (area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X') or
       (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X') or
       (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X') or
       (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X') or
       (area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X')):
        return 'X'
    elif ((area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O' ) or
       (area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O' ) or
       (area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O' ) or
       (area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O' ) or
       (area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O' ) or
       (area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O' ) or
       (area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O' ) or
       (area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O' )):
        return 'O'
    else:
        return '*'


for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
    else:
        turn_char = 'X'

    print(f'Ходят "{turn_char}"')
    row = int(input('Введите номер строк (1, 2 или 3): ')) - 1
    column = int(input('Введите номер столбца (1, 2 или 3): ')) - 1

    while area[row][column] != '*':
        print('-------------------------')
        print('Эта клетка уже занята. Попробуйте ещё раз.')
        print('-------------------------')
        draw_area()
        print('-------------------------')
        print(f'Ходят "{turn_char}"')
        row = int(input('Введите номер строк (1, 2 или 3): ')) - 1
        column = int(input('Введите номер столбца (1, 2 или 3): ')) - 1
        if area[row][column] != '*':
            continue
        else:
            area[row][column] = turn_char
        break

    area[row][column] = turn_char

    if check_winner() == 'X':
        print('Победили крестики!')
        print('-------------------------')
        draw_area()
        print('-------------------------')
        break
    if check_winner() == 'O' :
        print('Победили нолики!')
        print('-------------------------')
        draw_area()
        print('-------------------------')
        break
    if check_winner() == '*' and turn == 9:
        print('Победила дружба!')
        print('-------------------------')
        draw_area()
        print('-------------------------')
        break

    print('-------------------------')
    draw_area()
    print('-------------------------')

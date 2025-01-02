import calc


def test_add():
    if calc.add(2, 2) == 4:
        print('Test add(a,b) is OK')
    else:
        print('Test add(a,b) is Fail')


def test_sub():
    if calc.sub(2, 2) == 0:
        print('Test sub(a,b) is OK')
    else:
        print('Test sub(a,b) is Fail')


def test_mul():
    if calc.mul(2, 2) == 4:
        print('Test mul(a,b) is OK')
    else:
        print('Test mul(a,b) is Fail')


def test_div():
    if calc.div(2, 2) == 1:
        print('Test div(a,b) is OK')
    else:
        print('Test div(a,b) is Fail')


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()

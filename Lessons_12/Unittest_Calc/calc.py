def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# def add(a, b):
#     return a ** 2 + b ** 2  # изменили функцию сложения на сумму квадратов


# Добавили новые функции и сделали новый тест - test_new_calc
def sqrt(a):
    return a ** 0.5


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    print(mul(123, 321))

# При вызове данной функции ввод параметров обязателен
def print_params_1(a, b, c):
    print(a, b, c)

print_params_1(1, 2, 3)
print()

# При вызове данной функции ввод параметров не обязателен (будут использованы значения по умолчанию)
def print_params_2(a=1, b=2, c=3):
    print(a, b, c)

print_params_2()
print_params_2(10, 20, 30)  # позиционное переопределение параметров функции
print_params_2(c='string')  # именованное переопределение параметра функции
print_params_2(c='string', a=True, b=(1, 2))  # именованное переопределение параметра функции
print_params_2(10, 20, c='string')  # позиционное и именованное переопределение параметров функции
print()


# Строгое определение именованных параметров (всё что после звёздочки необходимо указывать явно при вызове функции)
# Если * стоит вначале (*, a, b, c), то при вызове функции все параметры необходимо указывать явно
def print_params_2(a,*, b, c):
    print(a, b, c)

print_params_2(10, b=20, c=30)
print()


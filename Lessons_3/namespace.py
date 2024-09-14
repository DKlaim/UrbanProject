# Переменные находятся в глобальном пространстве имён
a = 5
b = 10

print(a, b)


# Переменные находятся в локальном пространстве имён функции printer()
def printer_1():
    с = 15
    d = 20
    print(с, d)


printer_1()


# Внутри функций мы можем обращаться к глобальным переменным
def printer_2():
    с = 15
    d = 20
    print(с, d, '- local')
    print(a, b, '- global')


printer_2()


# Внутри функций мы можем менять значения глобальных переменных (но только эти изменения будут действовать только локально - внутри функции)
def printer_3():
    a = 'string 1'
    b = 'string 2'
    с = 15
    d = 20
    print(с, d, '- local')
    print(a, b, '- global change to local')


printer_3()
print(a, b, '- global')

# Но если мы хотим взаимодействовать с глобальными переменными локально, но как с глобальными, то
# мы можем обозначить их с помощью функции global
def printer_3():
    global a, b
    a = 'string 1'
    b = 'string 2'
    с = 15
    d = 20
    print(с, d, '- local')
    print(a, b, '- global')


printer_3()
print(a, b, '- global')
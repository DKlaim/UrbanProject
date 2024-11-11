# # Пример 1 - Ошибка (исключение) летит по стеку вызовов функций
# def f1(namber):
#     return 10 / namber
#
#
# def f2():
#     print('Какой хороший день!')
#     result_f1 = f1(0)
#     return result_f1
#
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'Обнаружена ошибка - {exc}, но мы устояли')


# # Пример 2 - Ошибка (исключение) перехватывается на одном из уровней стека вызовов функций
# def f1(namber):
#     return 10 / namber
#
#
# def f2():
#     print('Какой хороший день!')
#     summ = 0
#     for i in range(-2, 2):
#         summ += f1(i)  # ошибка возникает на данном уровне, соответственно print и return не выполняются
#         print(summ)
#     return summ
#
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'Обнаружена ошибка - {exc}, но мы устояли')


# # Пример 3 - Перехват ошибки (исключения) на уровне её появления
# def f1(namber):
#     return 10 / namber
#
#
# def f2():
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'Внутри f1() обнаружена ошибка - {exc}, но мы устояли')
#     return summ
#
#
# try:
#     total = f2()
#     print(f'Результат функции f2: {total}')
# except ZeroDivisionError as exc:
#     print(f'Внутри f2() обнаружена ошибка - {exc}, но мы устояли')


# Пример 4 - Неперехваченная ошибка NameError (переменная total не определена) приводит к вылету программы
def f1(namber):
    return total / namber


def f2():
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'Внутри f1() обнаружена ошибка - {exc}, но мы устояли')
    return summ


try:
    total = f2()
    print(f'Результат функции f2: {total}')
except ZeroDivisionError as exc:
    print(f'Внутри f2() обнаружена ошибка - {exc}, но мы устояли')

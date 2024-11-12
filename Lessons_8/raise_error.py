# # Пример 1 - raise ошибка
# def greet_person(person_name):
#     if person_name == 'Энакин Скайуокер':
#         raise Exception(f'Тёмную сторону силы в тебе ощущаю, {person_name}')
#     print(f'Да прибудет с тобой сила, {person_name}')
#
# greet_person('Люк Скайуокер')
# greet_person('Энакин Скайуокер')


# # Пример 2 - raise ошибка с предварительной обработкой
# try:
#     raise NameError('Привет Там')  # генерируем ошибку
# except NameError as exc:  # сразу же её перехватываем, сохраняем в переменной exc
#     print(f'Исключение типа {type(exc)} пролетело мимо! Его параметры: {exc.args}')  # и выводим данные о ней
#     raise  # на данном этапе мы "перебрасываем" ошибку дальше (raise без параметров)


# # Пример 3 - создание собственного класса ошибки/исключения
# class ProZero(Exception):
#     pass
#
#
# def f(a, b):
#     if b == 0:
#         raise ProZero('Деление на ноль невозможно!')
#     return a / b
#
#
# print(f(2, 0))


# Пример 4 - создание собственного продвинутого класса ошибки/исключения
class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero('Деление на ноль невозможно!', {'a': a, 'b': b})
    return a / b


try:
    result = f(10, 0)
    print(result)
except ProZero as exc:
    print('Не очень хорошо получилось - мы словили ошибку.')
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация: {exc.extra_info}')

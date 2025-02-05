""" Логирование """

import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b  # записываем выражение для проверки возможности выполнения данной операции (без сохранения/вывода результата)
        logging.info(f'Успешное деление {a} / {b}')
        return a / b
    except:
        logging.error(f'На ноль делить нельзя!', exc_info=True)  # exc_info=True - для передачи в логи информации об ошибке
        return 0  # вывод какого-то значения при возникновении ошибки


def add(a, b):
    return a ** 2 + b ** 2  # изменили функцию сложения на сумму квадратов


if __name__ == '__main__':
    # logging.debug('debug-текст')  # текущие сообщения о работе
    # logging.info('info-текст')  # важная информация о работе
    # logging.warning('warning-текст')  # предупреждения о потенциальных ошибках
    # logging.error('error-текст')  # сообщения уровня ошибок
    # logging.critical('critical-текст')  # сообщения уровня критических ошибок (из-за чего "легла" программа)
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py_info.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')  # запись логов в файл: level - что, filemode - запись, filename - куда, format - оформление вывода сообщений из логов
    print(div(3, 5))
    print(div(3, 0))
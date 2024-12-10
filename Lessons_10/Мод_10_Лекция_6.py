# Пример поточной и процессорной обработки
import threading
import multiprocessing
from time import sleep

counter = 0


def first_worker(n):
    global counter
    for i in range(n):
        counter += 1
        sleep(1)
    print(f'Первый рабочий изменил значение счетчика {counter}')


def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        sleep(1)
    print(f'Второй рабочий изменил значение счетчика {counter}')


# Пример поточной обработки (потоки выполняются параллельно используя общую область памяти)
thread_1 = threading.Thread(target=first_worker, args=(10,))
thread_2 = threading.Thread(target=second_worker, args=(5,))
thread_1.start()
thread_2.start()


# Пример процессорной обработки (процессы выполняются параллельно используя разные области памяти)
# if __name__ == '__main__':
#     process_1 = multiprocessing.Process(target=first_worker, args=(10,))
#     process_2 = multiprocessing.Process(target=second_worker, args=(15,))
#     process_1.start()
#     process_2.start()

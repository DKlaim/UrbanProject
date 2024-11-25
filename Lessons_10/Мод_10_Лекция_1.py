''' Поток - минимальная единица работы, которую необходимо выполнить ОС.
Потоки существуют внутри процессов, а также в одном процессе может существовать несколько потоков.
Потоки, которые работают внутри одного процесса, работают с общим состоянием и памятью родительского процесса. '''
import threading
import time


# # 1. Главный поток
# def func():  # функция печатает от 1 до 10 (поток № 1)
#     for i in range(10):
#         time.sleep(1)  # пауза в 1 сек, для замедления процесса выполнения функции
#         print(i, threading.current_thread())  # Функция current_thread() показывает какой сейчас поток выполняет код...
#         # ...в данном случае главный поток - MainThread (он создаёт все остальные)
#
#
# func()
# print(threading.enumerate())  # Функция enumerate() показывает список потоков


# # 2. Пример создания второго потока
# def func_1():  # функция печатает от 1 до 10 (поток № 1)
#     for i in range(10):
#         time.sleep(1)  # пауза в 1 сек, для замедления процесса выполнения функции
#         print(i, threading.current_thread())
#
#
# def func_2():  # функция печатает от 1 до 10 (поток № 1)
#     for i in range(10):
#         time.sleep(1)  # пауза в 1 сек, для замедления процесса выполнения функции
#         print(i, threading.current_thread())
#
#
# thread = threading.Thread(target=func_2)  # создаём поток для второй функции с помощью класса Thread
# thread.start()  # запускаем второй поток
#
# func_1()
#
# print(threading.enumerate())


# # 3. Пример потоковой функции с параметрами
# def func_1():
#     for i in range(10):
#         time.sleep(0.5)
#         print(i, threading.current_thread())
#
#
# def func_2(x):
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
#
# thread = threading.Thread(target=func_2, args=(1,))  # параметр передаётся как кортеж параметров
# thread.start()
# func_1()
#
# print(threading.enumerate())


# # 4. Работа программы и потоков
# def func_1():
#     for i in range(10):
#         time.sleep(0.5)
#         print(i, threading.current_thread())
#
#
# def func_2():
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
#
# thread = threading.Thread(target=func_2)
# thread.start()
# thread.join()  # приостановка главного потока
# print(thread.is_alive())  # Функция is_alive() показывает "жив" поток или нет (True/False)
# func_1()  # Главный поток начнёт выполняться после завершения дочернего (в данном случае)
#
# print(threading.enumerate())
# # Программа работает до тех пор, пока не завершиться последний поток.
# # Поток существует до тех пор, пока не завершит свою работу.


# 5. Пример потока-демона
def func_1():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())


def func_2():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())


thread = threading.Thread(target=func_2, daemon=True)  # у потоков по умолчанию параметр daemon равен False
thread.start()

func_1()

print(threading.enumerate())
# При наличии потока-демона, программа завершается не дожидаясь его полной отработки.

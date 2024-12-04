from threading import Thread, Lock, Event
from time import sleep


# # Пример 1
# def func_1():
#     for letter in 'Hello World':
#         print(letter)
#
#
# def func_2():
#     for letter in 'Привет Мир':
#         print(letter)
#
#
# thread_1 = Thread(target=func_2, daemon=True)
# # thread_2 = Thread(target=func_2)
# thread_1.start()
# thread_1.join()
# # thread_2.start()
# func_1()

# # Пример 2
# class MyThread(Thread):
#     def __init__(self, name, delay):
#         super().__init__(target=func, args=(name, delay))  # или Thread.__init__(self)
#         self.delay = delay
#
# def func(name, delay):
#     print(f'Поток {name} начался')
#     sleep(delay)
#     print(f'Поток {name} завершён')
#
# thread = Thread(target=func, daemon=True)
#
# thread_1 = MyThread('first', 5)
# thread_2 = MyThread('second', 5)
#
# thread_1.start()
# thread_2.start()


# # Пример 3
# class MyThread(Thread):
#     def __init__(self, name, delay):
#         super().__init__()  # или Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print(f'Поток {self.name} начался')
#         sleep(self.delay)
#         print(f'Поток {self.name} завершён')
#
#
# thread_1 = MyThread('first', 5)
# thread_2 = MyThread('second', 5)
#
# thread_1.start()
# thread_2.start()


# # Пример 4
# counter = 0
# lock = Lock()
#
# def increment():
#     lock.acquire()
#     for _ in range(100):
#         global counter
#         counter += 1
#         print(counter)
#     lock.release()
#
#
# def decrement():
#     lock.acquire()
#     for _ in range(100):
#         global counter
#         counter -= 1
#         print(counter)
#     lock.release()
#
#
# thread1 = Thread(target=increment)
# thread2 = Thread(target=decrement)
# thread3 = Thread(target=increment)
# thread4 = Thread(target=decrement)
#
# thread1.start()  # проблема решается замком Lock
# thread2.start()  # но есть проблема dead lock (решается закрытием/открытием замка: lock.acquire() / lock.release() в функции)
# thread3.start()
# thread4.start()


# # Пример 5
# from queue import Queue
#
#
# def func(queue: Queue):
#     sleep(2)
#     queue.put(1)
#
#
# q = Queue()
# thread = Thread(target=func, args=(q,))
#
# thread.start()
# result = q.get(timeout=5)
# print(result)
# print('end')


# Пример 6 - Выполнение потока по команде
def sniper():
    global open_fire_command
    print('Снайпер: Вижу цель, жду приказ')
    open_fire_command.wait() # 2 остановка потока до изменения флага
    sleep(1)
    print('Снайпер: выстрел')
    sleep(2)
    print('Снайпер: Цель поражена')


def commandor():
    global open_fire_command
    sleep(5)
    print('Командир: Открыть огонь')
    open_fire_command.set()  # 3 изменение флага для команды на исполнение


open_fire_command = Event()  # 1 Event создаёт объект-флаг

sniper_thread = Thread(target=sniper)
commandor_thread = Thread(target=commandor)

sniper_thread.start()
commandor_thread.start()

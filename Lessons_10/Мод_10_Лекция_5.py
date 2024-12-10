# Пример класса Event
from threading import Thread, Event
from time import sleep


def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять свою задачу')
    sleep(5)
    print('Первый рабочий закончил выполнять свою задачу')


def second_worker():
    print('Второй рабочий приступил к своей задаче')
    sleep(10)
    print('Второй рабочий закончил выполнять свою задачу')
    event.set()


event = Event()  # флаг
# print(event.is_set())  # is_set возвращает значение флага
#
# event.wait(timeout=3)  # wait ожидает пока не произойдёт какое-то событие (можно установить timeout - время ожидания)
# print(event.is_set())
#
# event.set()  # set сознаёт событие - меняет значение флага
# print(event.is_set())
#
# event.wait(timeout=5)  # wait ожидает событие - смену флага на True
# print(event.is_set())
#
# event.clear()  # clear сбрасывает состояние события - меняет значение флага на False
# print(event.is_set())

thread_1 = Thread(target=first_worker)
thread_2 = Thread(target=second_worker)
thread_1.start()
thread_2.start()

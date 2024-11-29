''' Очереди - конструкция, позволяющая синхронизировать потоки между собой.
Существует три вида: FIFO - первый пришёл - первый ушёл, LIFO, Priority '''

# Пример конструкции очереди вида FIFO
from queue import Queue
import threading
from time import sleep


def getter(queue):
    while True:
        sleep(5)
        item = queue.get()  # метод get получает элемент из очереди, параметром timeout можно указать время сколько ждать
        print(f'{threading.current_thread()} взял элемент {item}')


q = Queue(maxsize=10)  # пустая очередь (объект класса Queue), maxsize ограничивает количество элементов в очереди

thread_1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread_1.start()

for i in range(10):
    sleep(2)
    q.put(i)  # метод put кладёт элемент в очередь
    print(f'{threading.current_thread()} положил в очередь элемент {i}')

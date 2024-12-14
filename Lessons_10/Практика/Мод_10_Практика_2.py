import random
from queue import Queue
from threading import Thread
from time import sleep


class Bulka(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            sleep(random.randint(1, 2))
            if random.random() > 0.9:
                self.queue.put('подгорелая булка')
            else:
                self.queue.put('нормальная булка')


class Kotleta(Thread):

    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        print(f'Необходимо приготовить {self.count} бургеров')
        while self.count:
            print(f'Булок в очереди: {self.queue.qsize()}')  # метод qsize показывает длину/размер очереди (аналог строкового метода len)
            bulka = self.queue.get(timeout=3)
            if bulka == 'нормальная булка':
                sleep(random.randint(2, 3))
                self.count -= 1
            print(f'Осталось приготовить: {self.count}')
        else:
            print('Все бургеры готовы!')


queue = Queue(maxsize=5)

thread_1 = Bulka(queue)
thread_2 = Kotleta(queue, 20)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

''' Существует 2 способа работы с потоками:
1. Создавать объекты готового (встроенного) класса Thread
2. Создать свой класс, наследуемый от класса Thread с переопределением необходимого нам функционала '''
import threading
import time


# 1. Пример потокового класса
class MyThread(threading.Thread):
    def __init__(self, name):  # конструктора init в потоковом классе недостаточно
        threading.Thread.__init__(self)  # необходимо добавить конструктор потока
        self.name = name

    # Для работы потокового класса необходимо переопределить метод run (вызывается при команде start)
    def run(self):  # в данном методе прописывается вся логика работы потока
        print(f'Поток {self.name} запущен')
        print(f'Поток {self.name} завершён')


thread_1 = MyThread('thread_1')
thread_2 = MyThread('thread_2')

thread_1.start()
thread_2.start()


# 2. Пример потокового класса с расширенным функционалом
class MyThread2(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершён')


thread_1 = MyThread2('thread_1', 5, 1)
thread_2 = MyThread2('thread_2', 3, 0.5)  # завершиться быстрее

thread_1.start()
thread_2.start()

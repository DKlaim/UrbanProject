import threading
from random import randint
from time import sleep, process_time_ns
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        n = 0
        for guest in guests:
            if n == len(self.tables) or self.tables[n].guest:
                self.queue.put(guest.name)
                print(f'{guest.name} в очереди')
            else:
                self.tables[n].guest = guest.name
                thread = Guest(guest.name)
                thread.start()
                thread.join()
                print(f'Поток {thread.is_alive()}')
                print(f'{guest.name} сел(-а) за стол номер {self.tables[n].number} - {threading.current_thread()}')
                n += 1

    def discuss_guests(self):
        if self.queue.empty() or None in [table.guest for table in self.tables]:
            print(self.queue.empty(), 'None')
        else:
            for table in self.tables:
                print(table.number, table.guest)


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # # Обслуживание гостей
    cafe.discuss_guests()

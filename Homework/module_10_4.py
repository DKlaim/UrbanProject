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
        for guest in guests:
            # while None in [table.guest for table in self.tables]:
            for n in range(len(self.tables)):
                if self.tables[n].guest is None or guest.name != self.tables[n].guest:
                    self.tables[n].guest = guest.name
                    thread = Guest(guest.name)
                    print(f'{guest.name} сел(-а) за стол номер {self.tables[n].guest} - {threading.current_thread()}')
                    thread.start()
                    # thread.join()
                    break
                elif guest.name == self.tables[n].guest:
                    continue
                else:
                    self.queue.put(guest.name)
                    print(f'{guest.name} в очереди')

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

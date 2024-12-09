import threading
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


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
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    guest.start()
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    break

            if guest.name not in [table.guest for table in self.tables]:
                self.queue.put(guest.name)
                print(f'{guest.name} в очереди')

        print(threading.enumerate())  # проверка потоков

    def discuss_guests(self):
        while not self.queue.empty() or None not in [table.guest for table in self.tables]:
            for table in self.tables:
                # if Guest(table.guest).is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

            if not self.queue.empty() and None in [table.guest for table in self.tables]:
                for table in self.tables:
                    if table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{self.queue.get()} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        Guest(table.guest).start()



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

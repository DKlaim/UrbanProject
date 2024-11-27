import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self, name, power):
        days = 1
        enemies = 100
        while enemies:
            time.sleep(1)
            enemies -= power
            print(f'{name} сражается {days}..., осталось {enemies} воинов.')
            days += 1
        print(f'{name} одержал победу спустя {days - 1} дней(дня)!')

    def run(self):  # в данном методе прописывается вся логика работы потока
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

if not first_knight.is_alive() and not second_knight.is_alive():
    print('Все битвы закончились!')


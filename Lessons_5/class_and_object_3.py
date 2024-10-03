'''
Методы с нижним подчёркиванием являются специальными методами (или магические, или dunder - double underline)
'''

class Human:
    def __init__(self, name, age):  # __init__ - специальный метод-конструктор
        self.name = name
        self.age = age
        self.sey_info()

    def sey_info(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age}.')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения! Мне теперь {self.age}.')

    def __len__(self):  # Пример как вывести возраст по функции len для экземпляра нашего класса
        return self.age  # по сути мы переопределяем поведение функции len для вычисления размера экземпляра (объекта) нашего класса (для строк len определяет размер строки)

    def __del__(self):  # __del__ - специальный метод-деструктор, описывает логику того, что будет происходить, если экземпляр класса перестанет существовать
        print(f'{self.name} ушёл')


Den = Human('Денис', 22)
print(Den.name, Den.age)

Den.age = 23
print(Den.name, Den.age)
print(f'Возраст: {len(Den)}')
print('----------------------')

Max = Human('Макс', 22)
print(Max.name, Max.age)

Max.age = 32
print(Max.name, Max.age)
print('----------------------')

Den.sey_info()
Max.sey_info()
del Den
Max.birthday()
print('----------------------')
input('Для выхода нажмите любую кнопку.')

'''
Объекты существуют до тех пор, пока на них ссылается хоть одна ссылка!
'''
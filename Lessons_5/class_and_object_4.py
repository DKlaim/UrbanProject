class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sey_info()

    def sey_info(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age}.')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения! Теперь мне {self.age}.')

    def __len__(self):
        return self.age

    def __lt__(self,
               other):  # переопределение поведения оператора (в данном случае оператор МЕНЬШЕ "<") называется ПЕРЕГРУЗКОЙ оператора
        return self.age < other.age  # возвращаем True, если возраст первого участника меньше чем у второго участника данной операции

    def __gt__(self, other):  # ПЕРЕГРУЗКА оператора БОЛЬШЕ ">"
        return self.age > other.age  # возвращаем True, если возраст первого участника больше чем у второго

    def __eq__(self, other):  # перегрузка оператора РАВЕНСТВА "=="
        return self.name == other.name and self.age == other.age  # возвращаем True, если имена и возраст первого второго участника равны

    def __bool__(self):  # магический метод определения ЛОГИЧЕСКОГО оператора "True/False"
        return bool(self.age)  # возвращаем True, если значение возраста не равно нулю

    def __str__(self):
        return f'{self.name}'

    def __del__(self):
        print(f'{self.name} ушёл')


Den = Human('Денис', 22)
Max = Human('Макс', 22)
Denis = Human('Денис', 22)
print(Den < Max)
print(Den == Denis)

Max.birthday()
print(Den < Max)
print(Den > Max)
print(Max > Den)

if Den:
    Den.sey_info()

print('----------------------')
'''
При попытке вывести значение объекта Den, получим строку вида __main__.Human object at 0x0000027755462D80
Для преобразования строки в читаемый вид, воспользуемся магическим методом __str__
'''
print(Den)
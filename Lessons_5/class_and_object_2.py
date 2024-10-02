class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sey_info()  # Методы могут вызывать внутри себя другие методы

    def sey_info(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age}.')

    def birthday(self):
        self.age += 1  # Методы могут изменять атрибуты/характеристики из других методов внутри себя
        print(f'У меня день рождения! Мне теперь {self.age}.')


Den = Human('Денис', 22)  # При создании объекта и присвоении ему класса, происходит инициализация объекта в классе и он становится экземпляром данного класса
print(Den.name, Den.age)

Den.age = 23
print(Den.name, Den.age)
print('----------------------')

Max = Human('Макс', 22)
print(Max.name, Max.age)

Max.age = 32
print(Max.name, Max.age)
print('----------------------')

Den.sey_info()
Max.sey_info()
Max.birthday()
print('----------------------')
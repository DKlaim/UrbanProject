# print(int.__mro__)  # __mro__ показывает цепочку наследования
# print(object.__mro__)  # Класс object - базовый класс в иерархии классов


class User:
    # def __new__(cls, *args, **kwargs):  # cls является указателем на класс
    #     print('Я в __new__')  # таким образом мы переопределили метод __new__

    # __instance = None
    # def __new__(cls, *args, **kwargs):
    #     print('Я в __new__')
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __init__(self, *args, **kwargs):  # self является указателем на объект класса
        print('Я в __init__')
        self.args = args
        self.kwargs = kwargs
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, values in kwargs.items():
            setattr(self, key, values)


# user1 = User()
# print(User.__mro__)
# print(user1)  # Выведет None потому, что объект не создался из-за того, что мы переопределили метод __new__

'''
Метод __new__ должен возвращать ссылку на класс, но т.к. мы его переопределили, он ничего не возвращает, поэтому объект не может создаться
Если добавить в метод добавить строку "return super().__new__(cls)", то таким образом мы сможем передать ссылку на класс
Переопределение метода __new__ может быть применено при реализации паттерна синглтон, когда необходимо создать уникальный/единственный объект класса,
чтобы избежать повторной его инициализации.

Пример реализации:
    __instance = None  # создаём классовую переменную со значением None
    def __new__(cls, *args, **kwargs):
        print('Я в __new__')
        if cls.__instance is None:  # создаём условие при котором будет передаваться ссылка на класс, только в случае несуществующего объекта данного класса
            cls.__instance = super().__new__(cls)
        return cls.__instance

При такой реализации, все создаваемые объекты данного класса будут вести к одному адресу в памяти!
'''

other = [1, 2, 3]
user = {
    'name': 'Den',
    'age': 23
}

user1 = User(other, user)
print(user1.args)
print(user1.kwargs)
print()

print('---- Передаём именованный параметр ----')
user1 = User(other, user, name='Den')
print(user1.args)
print(user1.kwargs)
print()

print('---- Распаковка ----')
user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print()

print('---- Получаем отдельные характеристики ----')
user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print(user1.name)
print(user1.age)
print()

print('---- Передаём дополнительный параметр ----')
user = {
    'name': 'Den',
    'age': 23,
    'gender': 'male'
}

user1 = User(*other, **user)
print(user1.args)
print(user1.kwargs)
print(user1.name)
print(user1.age)
print()

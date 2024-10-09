class Human:

    head = True  # Переменная head (классовый объект) - атрибут, который является общим для всех экземпляров данного класса (будет принадлежать всем создаваемым объектам)

    def __init__(self, name, age):
        self.name = name  # Переменная name (экземплярный объект) - атрибут, который принадлежит создаваемым (инициируемым) экземплярам данного класса (внутри самого класса его не существует)
        self.age = age


Den = Human('Денис', 22)
Max = Human('Макс', 23)

print(Human.__dict__)
print(Den.__dict__)
print(Max.__dict__)
print('----------------------')
Human.head = False  # Если изменить значение классового атрибута, то оно изменится для всех экземпляров класса
print(Human.__dict__)
print(Den.head)
print(Max.head)
print('----------------------')
Den.head = True  # Но мы также можем менять значения атрибутов для отдельных экземпляров. При этом значение атрибута поменяется только у данного экземпляра.
print(Den.__dict__)
print(Max.__dict__)
print(Max.head)
print('----------------------')
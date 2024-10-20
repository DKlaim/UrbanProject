class Human:
    head = True


class Student:

    def about(self):
        print('Я студент 1')


class Human2:
    head = True


# Механизм наследования (получаем доступ к атрибутам класса Human2)
class Student2(Human2):  # При этом класс Student2 будет дочерним по отношению к классу Human2 (Human2 базовый/родительский класс)
    # head = False  # Если атрибут не будет найден, то тогда будет искаться в родительском классе

    def about(self):
        print('Я студент 2')


class Human3:
    head = True

    def __init__(self):  # Конструкция, которая позволяет обратиться к атрибутам/методам дочернего класса
        self.about()  # self это ссылка на объект student3 - экземпляр класса Student3


class Student3(Human3):

    def about(self):
        print('Я студент 3')


if __name__ == '__main__':
    human = Human()
    student = Student()

    print(human.head)
    student.about()

    print('-------------------')
    human2 = Human2()
    student2 = Student2()

    print(student2.head)
    student2.about()

    print('-------------------')
    student3 = Student3()
    print(student3.head)

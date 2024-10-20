# Пример использования наследования

class Human:
    head = True

    def say_hello(self):
        print('Здравствуйте!')


class Student(Human):

    def about(self):
        print('Я студент')

    # def say_hello(self):
    #     print('Здравствуйте!')


class Teacher(Human):

    def about(self):
        print('Я учитель')

    # def say_hello(self):
    #     print('Здравствуйте!')

# Классы Student и Teacher имеют дублирование кода, который можно вынести в родительский класс Human

if __name__ == '__main__':
    human = Human()
    student = Student()
    teacher = Teacher()

    student.about()
    student.say_hello()

    teacher.about()
    teacher.say_hello()
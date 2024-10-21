class _Human:  # Нижнее подчёркивание "_" перед названием класса определяет его локальным (блокировка от импортирования)
    head = True
    _legs = True
    __arms = True  # Двойное подчёркивание "__" создаёт уникальную переменную, защищая её от переопределения в дочерних классах

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)  # дочерний класс не сможет сослаться на данную переменную, но будет иметь её в качестве атрибута


class Student(_Human):
    arms = False


class Teacher(_Human):
    pass


if __name__ == '__main__':
    human = _Human()
    student = Student()
    teacher = Teacher()
    print('---------------------')
    student.about()
    print('---------------------')
    teacher.about()
    print('---------------------')
    human.about()
    print('---------------------')
    print(dir(human))
    print(dir(student))
    # print(student._legs)  # работает
    # print(student.__arms)  # не работает
    # print(human.__arms)  # также работать не будет
    print(student._Human__arms)  # работает
    print(human._Human__arms)  # работает
    print(student.arms)  # работает

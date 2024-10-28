class Human:
    def __init__(self, name, group):  # Создание цепочки наследования: 3. добавили group для привязки дочернего класса Student (принимаем от Student (name и group))
        self.name = name
        super().__init__(group)  # Создание цепочки наследования: 4. через метод super создаём привязку к атрибуту self.group класса, следующему далее по цепочке наследования после Human (передаём group в StudentGroup)
        super().about()  # 5. ИТОГО через метод super получаем метод about из StudentGroup в который передаём значения (self.name и self.group)
        # Метод super выступает своего рода мостом для перехода по цепочке наследования, если программа не нашла в текущем классе необходимый атрибут/метод
    def info(self):
        print(f'Привет! Меня зовут {self.name}.')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, StudentGroup):  # Наследование возможно от скольких угодно классов, НО! *** Важно! Чтобы цепочка работала, необходимо её создать/прописать во всех необходимых init-ах ***
    def __init__(self, name, place, group):  # Создание цепочки наследования: 1. добавили group для привязки к родительскому классу Human
        # self.name = name  # Чтобы не дублировать атрибут, можно обратиться к родительскому классу и вызвать напрямую его init
        # Human.__init__(self, name)  # но вместо данной записи следует записать метод super
        super().__init__(name, group)  # Создание цепочки наследования: 2. добавили group для привязки к родительскому классу Human (передаём (name и group) в Human)
        self.place = place
        super().info()  # также с помощью метода super можно обращаться к методам родительского класса



# human = Human('Денис')
# print(human.name)
#
# student = Student('Макс', 'Урбан')  # При инициализации экземпляра сначала выводятся обращения к методам внутри класса (в данном случае родительского info)
# print(student.name, student.place)

print(Student.mro())  # метод mro выводит цепочку наследования *** Важно следить за параметрами, которые создаются в init-ах наследственных классов, которые будут присоединены к нашему классу ***
student = Student('Макс', 'Урбан', '"Python Developers"')
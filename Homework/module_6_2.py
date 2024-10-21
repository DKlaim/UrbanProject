class Vehicl:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, __engine_power):
        self.owner = owner
        self.model = model
        self.color = color
        self.__engine_power = __engine_power

    def get_model(self):
        return f'Модель: {self.model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        color_variants = [color.lower() for color in self.__COLOR_VARIANTS]
        if new_color.lower() in color_variants:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicl):
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

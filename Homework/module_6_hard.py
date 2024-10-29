class Figure:
    sides_count = 0

    def __init__(self, sides: list, color: list, filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *colors):
        return all(0 <= color <= 255 for color in colors)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(side > 0 and isinstance(side, int) for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        from math import pi
        self.__radius = sides / (2 * pi)
        super().__init__(sides, color, filled=True)

    def get_square(self):
        return __import__('math').pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(sides, color, filled=True)

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        # Полупериметр
        pp = (a + b + c) / 2
        # Формула Герона для площади треугольника
        return __import__('math').sqrt(pp * (pp - a) * (pp - b) * (pp - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        self.sides = sides
        super().__init__(sides, color, filled=True)

    def get_volume(self):
        return self.sides ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((10, 20, 30), [3,5,7])  # (Цвет, стороны)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())


    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())


    print(triangle1.get_color())
    triangle1.set_sides(15, 20)  # Изменится
    print(triangle1.get_sides())
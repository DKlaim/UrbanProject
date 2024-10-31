class Figure:
    sides_count = 0

    def __init__(self, sides: list, color: list, filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, *colors):
        return all(0 <= color <= 255 for color in colors)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(side > 0 and isinstance(side, int) for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if isinstance(self.get_sides(), list):
            return sum(self.get_sides())
        if isinstance(self.get_sides(), tuple):
            return sum(list(self.get_sides()))
        return self.get_sides()

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

    def valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        return sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        from math import pi
        if len(side) > 1:
            side = [1]
            self.__radius = side[0] / (2 * pi)
            super().__init__(side, color, filled=True)
        else:
            self.__radius = list(side)[0] / (2 * pi)
            super().__init__(list(side), color, filled=True)

    def get_square(self):
        return __import__('math').pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
            super().__init__(sides, color, filled=True)
        super().__init__(list(sides), color, filled=True)

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

    def __init__(self, color, *side):
        if len(side) > 1:
            self.side = 1
            sides = [1] * self.sides_count
            super().__init__(sides, color, filled=True)
        else:
            self.side = list(side)[0]
            sides = side * self.sides_count
            super().__init__(list(sides), color, filled=True)

    def get_volume(self):
        return self.side ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

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

    triangle1 = Triangle((200, 200, 100), 2, 3, 5)
    print('Исходный цвет треугольника:', triangle1.get_color())
    print('Исходные стороны треугольника:', triangle1.get_sides())
    print('Периметр треугольника:', len(triangle1))

    triangle1.set_color(55, 66, 77)
    print('Изменённый цвет треугольника:', triangle1.get_color())

    triangle1.set_sides(5, 3, 12, 4, 5)
    print('Некорректное изменение сторон треугольника:', triangle1.get_sides())

    triangle1.set_sides(12, 13, 14)
    print('Изменённые стороны треугольника:', triangle1.get_sides())
    print('Периметр треугольника:', len(triangle1))

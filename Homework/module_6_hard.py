class Figure:
    sides_count = 0

    def __init__(self, sides: int, color: list, filled: bool):
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
        return all(side > 0 and isinstance(side, int) and side ==  for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        pass

    def set_sides(self, *new_sides):








class Circle:
    pass


class Triangle:
    pass


class Cube:
    pass



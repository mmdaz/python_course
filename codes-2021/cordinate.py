import math


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        if not isinstance(other, Coordinate):
            raise Exception("Other must be Coordinate not {}".format(type(other)))
        x_distance = (self.x - other.x) ** 2
        y_distance = (self.y - other.y) ** 2

        return math.sqrt(x_distance + y_distance)

    def __str__(self):
        return "x: {}, y: {}".format(self.x, self.y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


c = Coordinate(4, 3)
a = Coordinate(5, 6)


print(a + c)

origin = Coordinate(0, 0)

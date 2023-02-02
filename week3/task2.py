import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        dx = abs(other.x - self.x)
        dy = abs(other.y - self.y)

        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f'Point (x = {self.x}, y = {self.y})'

point1 = Point(10,4)
# print(point1)
# print(point1.get_x())
# print(point1.get_y())
# point1.shift(10,1)
# print(point1)
point2 = Point(6,7)
print(point1.distance(point2))


# point2 = Point(5,12)
#
# print(point1.distance(point2))
# print(point1.distance(point2))
# print(point2.__str__())
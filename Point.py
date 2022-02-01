import math


class Point:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    @staticmethod
    def distance(a, b):
        v = Point(b.x-a.x, b.y-a.y)
        return Point.norm(v)

    @staticmethod
    def norm(v):
        return math.sqrt((v.x*v.x+v.y*v.y))

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def copy(self):
        return Point(self.x, self.y)

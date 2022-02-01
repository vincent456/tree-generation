import Point


class Branch:
    def __init__(self, parent, position: Point.Point, direction: Point.Point):
        self.position: Point.Point = position
        self.parent = parent
        self.direction: Point.Point = direction

    def next(self):
        next_position: Point.Point = self.position + self.direction
        next_branch = Branch(self, next_position, self.direction.copy())
        return next_branch

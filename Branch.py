import numpy
import cv2

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

    def show(self, im: numpy.ndarray):
        if self.parent is not None:
            im = cv2.line(im, (int(self.position.x),
                               int(self.position.y)),
                          (int(self.parent.position.x),
                           int(self.parent.position.y)),
                          (0, 0, 255), 5)

    def __str__(self):
        return "parent:"+str(self.parent.position)+", position:"+str(self.position)


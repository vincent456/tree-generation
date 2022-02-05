import numpy
import cv2

import Point


class Branch:
    def __init__(self, parent, position: Point.Point, direction: Point.Point):
        self.position: Point.Point = position
        self.parent = parent
        self.direction: Point.Point = direction
        self.origDir: Point.Point = self.direction.copy()
        self.count: int = 0
        self.len: int = 5

    def reset(self):
        self.direction = self.origDir.copy()
        self.count = 0

    def next(self):
        #next_position: Point.Point = self.position + self.direction
        next_dir = self.len*self.direction
        next_pos = self.position + next_dir
        next_branch = Branch(self, next_pos, self.direction.copy())
        return next_branch

    def show(self, im: numpy.ndarray):
        if self.parent is not None:
            im = cv2.line(im, (int(self.position.x),
                               int(self.position.y)),
                          (int(self.parent.position.x),
                           int(self.parent.position.y)),
                          (0, 0, 255), 2)

    def __str__(self):
        return "parent:"+str(self.parent.position)+", position:"+str(self.position)


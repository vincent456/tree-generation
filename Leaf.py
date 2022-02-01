import numpy
import cv2

import Point


class Leaf:
    def __init__(self, pos: "Point.Point"):
        self.pos = pos

    def show(self, im: numpy.ndarray):
        im = cv2.circle(im, (self.pos.x, self.pos.y), 4, (0, 255, 0), -1)

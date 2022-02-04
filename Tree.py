import numpy

import Leaf
from typing import List
from Branch import Branch

from Point import Point


class Tree:
    def __init__(self):
        self.leaves: List["Leaf.Leaf"] = leaves
        self.direction = Point(0, 1)
        self.root = Branch(None, rootpos, self.direction)
        self.branches: List[Branch] = []
        self.branches.append(self.root)
        self.max_dist = max_dist

        #self.after_init()

    def after_init(self):
        found = False
        current: Branch = self.root
        while not found:
            for leaf in self.leaves:
                d = Point.distance(current.position, leaf.pos)
                if d < self.max_dist:
                    found = True
        if not found:
            branch = current.next()
            current = branch
            self.branches.append(current)
            print("branche crée",current)

    def show(self, im: numpy.ndarray):
        for leaf in self.leaves:
            leaf.show(im)
        for branch in self.branches:
            branch.show(im)

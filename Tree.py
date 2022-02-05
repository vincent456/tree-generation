import numpy

from Leaf import Leaf
from typing import List
from Branch import Branch

from Point import Point


class Tree:
    def __init__(self, glob):
        self.leaves: List[Leaf] = []
        self.branches: List[Branch] = []

        #global leaves
        for leaf in glob["leaves"]:
            self.leaves.append(leaf)
        #global width
        #global height
        pos = Point(glob["width"]/2, glob["height"])
        dir = Point(0, -1)
        root = Branch(None, pos, dir)
        self.branches.append(root)
        current = root
        found = False
        #global max_dist
        while not found:
            for leaf in self.leaves:
                d = Point.distance(current.position , leaf.pos)
                if d < glob["max_dist"]:
                    found = True

            if not found:
                branch = current.next()
                current = branch
                self.branches.append(current)

    def grow(self, glob):
        #global max_distance

        for leaf in self.leaves:
            closest_branch = None
            record = glob["max_dist"]
            #global min_distance
            for branch in self.branches:
                d = Point.distance(leaf.pos, branch.position)
                if d < glob["min_dist"]:
                    leaf.reached = True
                    closest_branch = None
                    break
                elif d < record:
                    closest_branch = branch
                    record = d

            if closest_branch is not None:
                new_dir = leaf.pos - closest_branch.position
                new_dir = new_dir.normalize()
                closest_branch.direction = closest_branch.direction + new_dir
                closest_branch.count = closest_branch.count + 1


        #remove reached leaves
        arr = []
        for i in range(len(self.leaves)):
            if not self.leaves[i].reached:
                arr.append(self.leaves[i])

        self.leaves = arr

        arr = self.branches
        for i in range(len(self.branches)):
            branch = self.branches[i]
            if branch.count > 0:
                branch.direction = branch.direction / (branch.count + 1)
                arr.append(branch.next())
                branch.reset()

        self.branches = arr

    def show(self, im):
        #for leaf in self.leaves:
         #   leaf.show(im)

        for branch in self.branches:
            branch.show(im)

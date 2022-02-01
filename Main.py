import cv2
from numpy import ndarray
import random

from Tree import Tree
from Point import Point
from Leaf import Leaf


min_dist = 10
max_dist = 10
tree = None


def main():
    im = cv2.imread("Bored-Ape-NFT-Bored-Ape-Yacht-Club-NFT-Culture.jpg")
    cv2.imshow("window", im)
    cv2.waitKey(0)

    global tree
    w, h, d = get_dimensions(im)
    tree = Tree([], Point(w/2, h), max_dist)
    # tree.root.position = Point(w / 2, h)
    print("traitement")
    scatter(im, 0.001)
    cv2.imshow("window", im)
    print("prêt")
    cv2.waitKey(0)

    print("traitement")
    tree.after_init()
    tree.show(im)

    print("prêt")
    cv2.waitKey(0)

    while True:
        cv2.imshow("window", im)
        o = cv2.waitKey(0)
        print(o)
        if o == 27: #escape
            break
    print("finished")


def scatter(im: ndarray, am):
    w, h, d = get_dimensions(im)
    for y in range(h):
        for x in range(w):
            if is_color(im, y, x, 255, 255, 255) and random.random() < am:
                tree.leaves.append(Leaf(Point(x, y-50)))
                set_color(im, y, x, 255, 0, 0)


def get_dimensions(im: ndarray):
    return \
        (
            im.shape[1],
            im.shape[0],
            im.shape[2]
        )


def is_color(im: ndarray, y, x, b, g, r):
    return im[y, x, 0] == b and im[y, x, 1] == g and im[y, x, 2] == r


def set_color(im: ndarray, y, x, b, g, r):
    im[y, x, 0] = b
    im[y, x, 1] = g
    im[y, x, 2] = r


if __name__ == '__main__':
    main()

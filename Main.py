import cv2
from numpy import ndarray
import random

from Tree import Tree
from Point import Point
from Leaf import Leaf


glob = {
    "min_dist": 10,
    "max_dist": 50,
    "tree": None,
    "leaves": [],
    "width": None,
    "height": None
}

def main():
    im = cv2.imread("Bored-Ape-NFT-Bored-Ape-Yacht-Club-NFT-Culture.jpg")
    cv2.imshow("window", im)
    cv2.waitKey(0)

    w, h, d = get_dimensions(im)
    glob["width"] = w
    glob["height"] = h
    glob["height"] = h
    # tree.root.position = Point(w / 2, h)
    print("traitement")
    scatter(im, 0.005)
    glob["tree"] = Tree(glob)
    glob["tree"].show(im)
    cv2.imshow("window", im)
    print("prêt")
    cv2.waitKey(0)

    while True:

        glob["tree"].grow(glob)
        glob["tree"].show(im)
        cv2.imshow("window", im)
        o = cv2.waitKey(0)
        print(o)
        if o == 27: #escape
            break
        if o == 115: #s
            cv2.imwrite("render.jpg", im)
            print("saved")
    print("finished")


def scatter(im: ndarray, am):
    w, h, d = get_dimensions(im)
    for y in range(h):
        for x in range(w):
            if is_color(im, y, x, 255, 255, 255) and random.random() < am:
                glob["leaves"].append(Leaf(Point(x, y)))
                #set_color(im, y, x, 255, 0, 0)


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

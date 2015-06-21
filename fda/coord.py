__author__ = 'saintdragon2'

import math

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2))

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
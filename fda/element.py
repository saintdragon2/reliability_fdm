__author__ = 'saintdragon2'

from fda.coord import Coord

class Element:
    def __init__(self, id, type, dx, x, y, diffusion_coeff, init_val=0):
        self._id = id
        self._type = type
        self._dx = dx

        self.coord = Coord(x, y)

        self.diffusion_coeff = diffusion_coeff

        self.dt = self.dt()
        self.fo = self.fo()

        self.values = [init_val]

        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def set_neighbors(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def dt(self):
        return self._dx * self._dx / self.diffusion_coeff / 4

    def fo(self):
        return self.diffusion_coeff * self.dt / ( self._dx * self._dx )

    def get_x(self):
        return self.coord.x

    def get_y(self):
        return self.coord.y

    def last_value(self, t):
        if self.is_domain():
            return self.values[t]
        else:
            return self.values[0]

    def is_domain(self):
        return self._type == 'D' or self._type == 'd'


    def calculate(self):
        if self.is_domain():
            last_time = len(self.values) - 1
            self.values.append(
                (
                    self.north.fo * self.north.last_value(last_time)
                    + self.east.fo * self.east.last_value(last_time)
                    + self.south.fo * self.south.last_value(last_time)
                    + self.west.fo * self.west.last_value(last_time)
                ) + (1-4*self.fo)*self.last_value(last_time)
            )




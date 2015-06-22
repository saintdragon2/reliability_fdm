__author__ = 'SungYong'
from fda.element import Element
from fda.coord import Coord
from statistics.normpdf import NormPdf

class ConvElement(Element):
    def __init__(self, id, type, dx, x, y, diffusion_coeff, init_mean=0, init_std=1):
        self._id = id
        self._type = type
        self._dx = dx

        self.coord = Coord(x, y)

        self.diffusion_coeff = diffusion_coeff

        self.values = []

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        init_value = NormPdf(mean=init_mean, std=init_std, delta=0.01)
        # init_value.pack()
        self.values.append( init_value )

    def calculate(self):
        if self.is_domain():
            last_time = len(self.values) - 1

            self.values.append(
                (
                    self.north.last_value(last_time)
                    + self.east.last_value(last_time)
                    + self.south.last_value(last_time)
                    + self.west.last_value(last_time)
                ).scale( self.fo )
                + (self.last_value(last_time).scale(1-4*self.fo))
            )
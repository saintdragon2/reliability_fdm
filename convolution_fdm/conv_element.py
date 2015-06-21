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
        init_value = NormPdf(init_mean, init_std)
        init_value.pack()
        self.values.append( init_value )

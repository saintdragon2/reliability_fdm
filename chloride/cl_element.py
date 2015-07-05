__author__ = 'SungYong'

from fda.element import Element
from chloride.coeffs import DiffCoeff, SurfaceChloride

class ClElement(Element):
    def __init__(self, id, e_type, dx, x, y, d_ref, init_val=0):
        Element.__init__(self, id, e_type, dx, x, y, d_ref, init_val)

        self.diffusion_coeff = DiffCoeff(d_ref, 1)

    def get_fo(self, year):
        return self.diffusion_coeff.t(year) * self.dt / (self._dx * self._dx)

    def last_value(self, t):
        return self.values[t]

    def calculate(self):
        year = len(self.values) * self.dt
        if self.is_domain():
            last_time = len(self.values) - 1

            if self.get_fo(year) >= 0.25:
                raise OutOfConversionRadiusException(str(self.get_fo(year)) + ' is not smaller than 0.25')

            self.values.append(
                (
                    self.north.last_value(last_time)
                    + self.east.last_value(last_time)
                    + self.south.last_value(last_time)
                    + self.west.last_value(last_time)
                ) * self.get_fo(year)
                + (1-4*self.get_fo(year))*self.last_value(last_time)
            )
        elif self.get_type() == 'B':
            cs = SurfaceChloride(1.52, 3.77)
            self.values.append(cs.t(year))

    def get_type(self):
        return self._type


# class ClBoundaryElement(ClElement):
#     def __init__(self, id, e_type, dx, x, y, d_ref, init_val=0):
#         ClElement.__init__(id, e_type, dx, x, y, d_ref, init_val)
#         # self.cs = SurfaceChloride(1.52, 3.77)
#
#     def calculate(self):
#         year = self.dt * len(self.values)
#         print('id')
#         self.values.append(self.cs.t(year))


class MirrorElement(ClElement):
    def __init__(self, id, e_type, dx, x, y, d_ref, init_val=0):
        ClElement.__init__(self, id, e_type, dx, x, y, d_ref, init_val)
        self.original = None

    def set_original(self, original_element):
        self.original = original_element

    def calculate(self):
        self.values = self.original.values


class OutOfConversionRadiusException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

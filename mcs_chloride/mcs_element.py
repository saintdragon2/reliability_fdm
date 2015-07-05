__author__ = 'SungYong'

import numpy
from chloride.cl_element import ClElement
from chloride.coeffs import SurfaceChloride

class ReliabilityElement(ClElement):
    def __init__(self, id, e_type, dx, x, y, d_ref, init_val=0, bc_std=0.001):
        ClElement.__init__(self, id, e_type, dx, x, y, d_ref, init_val)
        self._no = id
        self._type = e_type
        self.bc_std_dev = bc_std

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
            v = numpy.random.normal(cs.t(year), self.bc_std_dev)
            self.values.append(v)

class OutOfConversionRadiusException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


__author__ = 'saintdragon2'

import math

class DiffCoeff:
    def __init__(self, d_ref, t_ref): # d_ref: 10e-12; t_ref: year
        self.d_ref = d_ref
        self.t_ref = t_ref

    def t(self, year):
        if year <= 30:
            return self.d_ref * math.pow(self.t_ref / year, 0.2)
        else:
            return self.d_ref * math.pow(self.t_ref/30, 0.2)


class SurfaceChloride:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def t(self, year):
        return self.alpha * math.log(self.beta * year + 1)
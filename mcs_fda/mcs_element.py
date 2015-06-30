__author__ = 'SungYong'

import numpy

class McsElement:
    def __init__(self):
        self.elements = []

    def is_boundary(self):
        return not self.elements[0].is_domain()

    def is_domain(self):
        return self.elements[0].is_domain()

    def get_id(self):
        return self.elements[0].get_id()

    def mean(self, step):
        sum = 0
        for element in self.elements:
            sum += element.values[step]

        return sum / len(self.elements)

    def std(self, step):
        values = []
        for element in self.elements:
            values.append(element.values[step])

        return numpy.std(values)



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

    def all_values(self, step):
        result = []
        for element in self.elements:
            result.append(element.values[step])
        return result

    def get_pdf(self, step, no_bins = 100):
        values = self.all_values(step)

        return numpy.histogram(values, bins=no_bins, density=True)



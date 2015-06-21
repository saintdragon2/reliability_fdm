__author__ = 'SungYong'

import csv
import numpy
import math

from fda.fdm import Fdm
from fda.coord import Coord
from fda.element import Element
from mcs_fda.mcs_element import McsElement

class McsFdm():
    def __init__(self):
        self.runs = None
        self.fdms = []
        self.mcs_elements = []
        # self.bcs = []

    def read_file(self, file_name):
        dx = None

        element_types = []
        element_init_values = []
        element_coords = []
        element_diffusion_coeffs = []

        initial_conditions = []

        ys = 0

        with open(file_name) as fdm_file:
            read_fdm = csv.reader(fdm_file, delimiter=',')

            for row in read_fdm:
                if row[0] == 'dx':
                    dx = float(row[1])

                elif row[0].startswith('init condition'):
                    initial_conditions.append({'id': row[1], 'mean': float(row[2]), 'std': float(row[3])})

                elif row[0].startswith('runs'):
                    self.runs = int(row[1])

                elif row[0].startswith('Element Type'):
                    for i in range(1, len(row)):

                        if row[i]:
                            element_types.append(row[i].strip())

                    ys += 1

                elif row[0].startswith('Initial Values'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_init_values.append(int(row[i].strip()))

                elif row[0].startswith('Diffusion Coeff'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_diffusion_coeffs.append(float(row[i].strip()))

        self.xs = int(len(element_types) / ys )

        for xx in range(0, self.xs):
            for yy in range(0, ys):
                x = xx * dx
                y = yy * dx
                element_coords.append(Coord(x, y))

        for p in range(0, self.runs):
            fdm = Fdm()
            fdm.dx = dx
            fdm.xs = self.xs

            for i in range(0, len(element_types)):
                id = i + 1
                type = element_types[i]
                diffusion_coeff = element_diffusion_coeffs[i] #numpy.random.normal( self.bcs[0]['mean'], self.bcs[0]['std'])

                init_mean = initial_conditions[element_init_values[i]]['mean']
                init_std = initial_conditions[element_init_values[i]]['std']
                init_value = numpy.random.normal(init_mean, init_std)
                x = element_coords[i].x
                y = element_coords[i].y

                fdm.elements.append( Element(id, type, dx, x, y, diffusion_coeff, init_value))

            for element in fdm.elements:
                if element._type == 'D':
                    fdm.find_neighbors(element, self.xs)

            self.fdms.append(fdm)

        self.set_dt_fo()


        for i in range(0, len(self.fdms[0].elements)):
            mcs_element = McsElement()
            for fdm in self.fdms:
                mcs_element.elements.append(fdm.elements[i])
            self.mcs_elements.append(mcs_element)


    def set_dt_fo(self):
        max_d = 0
        for fdm in self.fdms:
            for element in fdm.elements:
                if element.diffusion_coeff > max_d:
                    max_d = element.diffusion_coeff

        dt = 0.25/max_d * math.pow((self.fdms[0].dx), 2)

        for fdm in self.fdms:
            fdm.set_dt_fo(dt)

    def calculate(self, iteration=1):
        for fdm in self.fdms:
            fdm.calculate(iteration)

    def print_snapshots(self, steps):
        for s in steps:
            if s > len(self.fdms[0].get_domains()[0].values):
                print('Wrong Step No.')
                return None

        for s in steps:
            print('-----------' + str(s) + '--------------')
            c = 1
            result = ''
            for mcs_element in self.mcs_elements:
                if not mcs_element.is_domain():
                    result += str(mcs_element.mean(0))
                else:
                    result += str(mcs_element.mean(s))
                if c % self.xs == 0:
                    print(result)
                    result = ''
                else:
                    result += '\t'
                c += 1


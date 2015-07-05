__author__ = 'saintdragon2'

import csv
from fda.coord import Coord
from fda.element import Element

class Fdm:
    def __init__(self):
        self.elements = []
        self.dx = None
        self.dt = None
        self.xs = None

    def read_file(self, file_name):

        element_types = []
        element_init_values = []
        element_diffusion_coeffs = []
        element_coords = []

        ys = 0

        with open(file_name) as fdm_file:
            read_fdm = csv.reader(fdm_file, delimiter=',')

            for row in read_fdm:
                if row[0] == 'dx':
                    self.dx = float(row[1])
                elif row[0].startswith('Element Type'):
                    for i in range(1, len(row)):

                        if row[i]:
                            element_types.append(row[i].strip())

                    ys += 1

                elif row[0].startswith('Initial Values'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_init_values.append(float(row[i].strip()))

                elif row[0].startswith('Diffusion Coeff'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_diffusion_coeffs.append(float(row[i].strip()))

        self.xs = int(len(element_types) / ys )

        for xx in range(0, self.xs):
            for yy in range(0, ys):
                x = xx * self.dx
                y = yy * self.dx
                element_coords.append(Coord(x, y))

        for i in range(0, len(element_types)):
            id = i + 1
            type = element_types[i]
            dx = self.dx
            diffusion_coeff = element_diffusion_coeffs[i]
            if i >= len(element_init_values):
                print(i)

            init_value = element_init_values[i]
            x = element_coords[i].x
            y = element_coords[i].y

            self.elements.append( Element(id, type, dx, x, y, diffusion_coeff, init_value))

        self.set_dt_fo(0.5)

        for element in self.elements:
            if element._type == 'D':
                self.find_neighbors(element, self.xs)

    def set_dt_fo(self, max_dt = None):

        if max_dt is None:
            max_dt = 0
            for element in self.elements:
                if max_dt < element.possible_dt():
                    max_dt = element.possible_dt()

        self.dt = max_dt

        for element in self.elements:
            element.set_fo(self.dt)

    def find_neighbors(self, element, xs):
        element.north = self.elements[element.get_id() - 1 - xs]
        element.south = self.elements[ element.get_id() - 1 + xs]
        element.west = self.elements[ element.get_id() - 2]
        element.east = self.elements[ element.get_id() ]

    def get_boundaries(self):
        boundaries = []

        for element in self.elements:
            if not element.is_domain():
                boundaries.append(element)

        return boundaries

    def get_domains(self):
        domains = []
        for element in self.elements:
            if element.is_domain():
                domains.append(element)
        return domains

    def calculate(self, iteration=1):
        for i in range(0, iteration):
            print('try iteration : ' + str(i))
            for element in self.elements:
                if element.is_domain():
                    element.calculate()

    def print_snapshots(self, steps):
        # print( self.get_domains())
        for s in steps:
            if s > len(self.get_domains()[0].values):
                print('Wrong Step No.')
                return None

        for s in steps:
            print('-----------' + str(s) + '--------------')
            c = 1
            result = ''
            for element in self.elements:

                if not element.is_domain():
                    result += str(element.values[0])
                else:
                    result += str(element.values[s])
                if c % self.xs == 0:
                    print(result)
                    result = ''
                else:
                    result += '\t'
                c += 1

    def write_file_snapshots(self, file):
        tt = len(self.get_domains()[0].values)
        for step in range(0, tt):

            file.write('-mean----' + str(step) + '-----\n')
            c = 1
            result = ''
            for element in self.elements:
                if not element.is_domain():
                    result += str(element.values[0])
                else:
                    result += str(element.values[step])

                if c % self.xs == 0:
                    file.write(result+'\n')
                    result = ''
                else:
                    result += '\t'
                c += 1

    def write_traking_elements(self, file, elements_idx):
        for i in elements_idx:
            file.write(str(self.elements[i].get_id()) + '\n')
            file.write(str(self.elements[i].values) + '\n')





    # print(element_types)
    # print(element_init_values)
    # print(element_diffusion_coeffs)
    # print(ys)
    # print(xs)
    #
    # for coord in element_coords:
    #     print(coord)






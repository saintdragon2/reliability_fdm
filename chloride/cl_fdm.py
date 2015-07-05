__author__ = 'SungYong'

import csv
from chloride.cl_element import ClElement, MirrorElement#, ClBoundaryElement
from fda.coord import Coord
from fda.fdm import Fdm
class ClFdm(Fdm):
    def __init__(self):
        self.elements = []
        self.dx = None
        self.dt = None
        self.xs = None

        self.d_ref = None
        self.init_value = None

    def read_file(self, file_name):

        element_types = []
        element_init_values = []
        element_diffusion_coeffs = []
        element_coords = []

        ys = 0

        with open(file_name) as file:
            read_cl_fdm = csv.reader(file, delimiter=',')

            for row in read_cl_fdm:
                if row[0].startswith('dx'):
                    self.dx = float(row[1])
                elif row[0].startswith('dt'):
                    self.dt = float(row[1])
                elif row[0].startswith('d_ref'):
                    self.d_ref = float(row[1])
                elif row[0].startswith('init value'):
                    self.init_value = float(row[1])
                elif row[0].startswith('Element Type'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_types.append(row[i].strip())

                    ys += 1

                # elif row[0].startswith('Initial Values'):
                #     for i in range(1, len(row)):
                #         if row[i]:
                #             element_init_values.append(float(row[i].strip()))
                #
                # elif row[0].startswith('Diffusion Coeff'):
                #     for i in range(1, len(row)):
                #         if row[i]:
                #             element_diffusion_coeffs.append(float(row[i].strip()))

        self.xs = int(len(element_types) / ys)

        for xx in range(0, self.xs):
            for yy in range(0, ys):
                x = xx * self.dx
                y = yy * self.dx
                element_coords.append(Coord(x, y))

        for i in range(0, len(element_types)):
            id = i + 1
            type = element_types[i]
            dx = self.dx

            # if i >= len(element_init_values):
            #     print(i)

            # init_value = element_init_values[i]
            x = element_coords[i].x
            y = element_coords[i].y

            self.elements.append( ClElement(id, type, dx, x, y, self.d_ref, self.init_value))

        for element in self.elements:
            element.dt = self.dt
            element.dx = self.dx

            if element.get_type() == 'D':
                self.find_neighbors(element, self.xs)
            elif element.get_type() == 'B':
                id = element.get_id()
                # element = ClBoundaryElement(id, 'B', self.dx, element.get_x(), element.get_y(), element.diffusion_coeff, element.values[0])
            elif element.get_type() == 'M_W':
                id = element.get_id()
                element = MirrorElement(id, 'M_W', self.dx, element.get_x(), element.get_y(), element.diffusion_coeff, element.values[0])
                element.set_original(self.elements[id - 2])

    def calculate(self, iteration=1):
            for i in range(0, iteration):
                print('try iteration : ' + str(i))
                for element in self.elements:
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
                    result += str(element.values[s])
                else:
                    result += str(element.values[s])
                if c % self.xs == 0:
                    print(result)
                    result = ''
                else:
                    result += '\t'
                c += 1
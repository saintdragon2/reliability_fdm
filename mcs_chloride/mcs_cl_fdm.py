__author__ = 'SungYong'

import csv
from chloride.cl_fdm import ClFdm
from mcs_chloride.mcs_element import ReliabilityElement
from fda.coord import Coord

class ReliabilityClFdm(ClFdm):
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

            self.elements.append(ReliabilityElement(id, type, dx, x, y, self.d_ref, self.init_value))

        for element in self.elements:
            element.dt = self.dt
            element.dx = self.dx

            if element.get_type() == 'D':
                self.find_neighbors(element, self.xs)
            # elif element.get_type() == 'B':
            #     id = element.get_id()
                # element = ClBoundaryElement(id, 'B', self.dx, element.get_x(), element.get_y(), element.diffusion_coeff, element.values[0])
            # elif element.get_type() == 'M_W':
            #     id = element.get_id()
            #     element = MirrorElement(id, 'M_W', self.dx, element.get_x(), element.get_y(), element.diffusion_coeff, element.values[0])
            #     element.set_original(self.elements[id - 2])





    # def __init__(self):
    #     self.runs = None
    #     self.fdms = []
    #     self.mcs_elements = []
    #
    #     self.dx = None
    #     self.dt = None
    #
    #     self.init_value = None
    #     self.d_ref = None
    #
    #     self.xs = None
    #
    #     self.elements = []
    #
    # def read_file(self, file_name):
    #     ys = 0
    #
    #     element_types = []
    #
    #     with open(file_name) as fdm_file:
    #         read_fdm = csv.reader(fdm_file, delimiter=',')
    #
    #         for row in read_fdm:
    #             if row[0] == 'runs':
    #                 self.runs = int(row[1])
    #             elif row[0].startswith('dx'):
    #                 self.dx = float(row[1])
    #             elif row[0].startswith('dt'):
    #                 self.dt = float(row[1])
    #             elif row[0].startswith('d_ref'):
    #                 self.d_ref = float(row[1])
    #             elif row[0].startswith('init value'):
    #                 self.init_value = float(row[1])
    #             elif row[0].startswith('Element Type'):
    #                 for i in range(1, len(row)):
    #                     if row[i]:
    #                         element_types.append(row[i].strip())
    #
    #                 ys += 1
    #
    #     self.xs = int(len(element_types) / ys)
    #
    #     for f in range(0, self.runs):
    #         cl_fdm = ClFdm()
    #         cl_fdm.dx = self.dx
    #         cl_fdm.dt = self.dt
    #         cl_fdm.xs = self.xs
    #         cl_fdm.d_ref = self.d_ref
    #         cl_fdm.init_value = self.init_value
    #

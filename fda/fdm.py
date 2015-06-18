__author__ = 'saintdragon2'

import csv
import string

class Fdm:
    def __init__(self):
        self.elements = []
        self.dx = None

    def read_file(self, file_name):

        element_types = []
        element_init_values = []
        element_diffusion_coeffs = []

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

        print(element_types)
        print(element_init_values)
        print(element_diffusion_coeffs)
        print(ys)






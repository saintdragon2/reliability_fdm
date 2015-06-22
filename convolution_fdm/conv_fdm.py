__author__ = 'saintdragon2'

import csv
from fda.coord import Coord
from convolution_fdm.conv_element import ConvElement
from fda.fdm import Fdm

class ConvFdm(Fdm):
    def __init__(self):
        self.elements = []
        self.dx = None
        self.dt = None
        self.xs = None

    def read_file(self, file_name):

        initial_conditions = []

        element_types = []
        element_init_values = []
        element_diffusion_coeffs = []
        element_coords = []

        ys = 0

        with open(file_name) as fdm_file:
            read_fdm = csv.reader(fdm_file, delimiter=',')

            for row in read_fdm:
                if row[0] == 'dx':
                    self.dx = float( row[1])
                elif row[0] == 'dt':
                    self.dt = float(row[1])
                elif row[0].startswith('init condition'):
                    initial_conditions.append({'id': row[1], 'mean': float(row[2]), 'std': float(row[3])})
                elif row[0].startswith('Element Type'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_types.append( row[i].strip() )
                    ys += 1
                elif row[0].startswith('Initial Values'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_init_values.append(int(row[i].strip()))
                elif row[0].startswith('Diffusion Coeff'):
                    for i in range(1, len(row)):
                        if row[i]:
                            element_diffusion_coeffs.append(float(row[i].strip()))

        self.xs = int(len(element_types) / ys)

        for xx in range(0, self.xs):
            for yy in range(0, ys):
                x = xx * self.dx
                y = yy * self.dx
                element_coords.append(Coord(x, y))

        for i in range(0, len(element_types)):
            id = i + 1
            type = element_types[i]
            diffusion_coeff = element_diffusion_coeffs[i]
            init_mean = initial_conditions[element_init_values[i]]['mean']
            init_std = initial_conditions[element_init_values[i]]['std']

            x = element_coords[i].x
            y = element_coords[i].y

            self.elements.append( ConvElement(id, type, self.dx, x, y, diffusion_coeff, init_mean, init_std))

        for element in self.elements:
            element.set_fo(self.dt)
            if element.is_domain():
                self.find_neighbors(element, self.xs)

        print('reading completed')


    def print_snapshots(self, steps):
        for step in steps:
            print('-mean----' + str(step) +  '-----')
            c = 1
            result = ''
            for element in self.elements:
                if not element.is_domain():
                    result += str(element.values[0].mean)
                else:
                    result += str(element.values[step].mean)

                if c % self.xs == 0:
                    print(result)
                    result = ''
                else:
                    result += '\t'
                c += 1

        print('---------std------')
        for step in steps:
            print('-std----' + str(step) +  '-----' + str(step*self.dt))
            c = 1
            result = ''
            for element in self.elements:
                if not element.is_domain():
                    result += str(element.values[0].std)
                else:
                    result += str(element.values[step].std)

                if c % self.xs == 0:
                    print(result)
                    result = ''
                else:
                    result += '\t'
                c += 1




    def write_file_snapshots(self, file):
        tt = len(self.get_domains()[0].values)
        for step in range(0, tt):

            file.write('-mean----' + str(step) +  '-----\n')
            c = 1
            result = ''
            for element in self.elements:
                if not element.is_domain():
                    result += str(element.values[0].mean)
                else:
                    result += str(element.values[step].mean)

                if c % self.xs == 0:
                    file.write(result+'\n')
                    result = ''
                else:
                    result += '\t'
                c += 1

        print('---------std------\n')
        for step in range(0, tt):
            file.write('-std----' + str(step) +  '-----' + str(step*self.dt) + '\n')
            c = 1
            result = ''
            for element in self.elements:
                if not element.is_domain():
                    result += str(element.values[0].std)
                else:
                    result += str(element.values[step].std)

                if c % self.xs == 0:
                    file.write(result+'\n')
                    result = ''
                else:
                    result += '\t'
                c += 1




        # for s in steps:
        #     print('-----------' + str(s) + '--------------')
        #     c = 1
        #     result = ''
        #     for element in self.elements:
        #
        #         if not element.is_domain():
        #             result += str(element.values[0])
        #         else:
        #             result += str(element.values[s])
        #         if c % self.xs == 0:
        #             print(result)
        #             result = ''
        #         else:
        #             result += '\t'
        #         c += 1
        #





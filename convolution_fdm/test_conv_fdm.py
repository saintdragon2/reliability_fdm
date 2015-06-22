__author__ = 'SungYong'

import unittest

from convolution_fdm.conv_element import ConvElement
from convolution_fdm.conv_fdm import ConvFdm

class TestConvElement(unittest.TestCase):
    def setUp(self):
        dx = 1e-3
        self.conv_element = ConvElement(1, 'D', dx=dx, x=10, y=10, diffusion_coeff=1.43e-7, init_mean=5.0, init_std=1.5)

        self.e_west = ConvElement(2, 'B', dx=dx, x=9, y=10, diffusion_coeff=1.43e-7, init_mean=100, init_std=4)
        self.e_east = ConvElement(3, 'D', dx=dx, x=11, y=10, diffusion_coeff=1.43e-7, init_mean=15, init_std=5)
        self.e_north = ConvElement(4, 'B', dx=dx, x=10, y=9, diffusion_coeff=1.43e-7, init_mean=100, init_std=4)
        self.e_south = ConvElement(5, 'D', dx=dx, x=10, y=11, diffusion_coeff=1.43e-7, init_mean=15, init_std=5)

        self.conv_element.set_neighbors(self.e_north, self.e_east, self.e_south, self.e_west)
        self.conv_element.set_fo(1)
        self.e_west.set_fo(1)
        self.e_east.set_fo(1)
        self.e_south.set_fo(1)
        self.e_north.set_fo(1)

    def test_create_conv_element(self):

        self.assertEqual(self.conv_element._id, 1)
        self.assertEqual(self.conv_element._type, 'D')
        self.assertEqual(self.conv_element._dx, 1e-3)
        self.assertEqual(self.conv_element.get_x(), 10)
        self.assertEqual(self.conv_element.get_y(), 10)

        self.assertEqual(self.conv_element.values[0].mean, 5.0)
        self.assertEqual(self.conv_element.values[0].std, 1.5)
        # print(self.conv_element.values[0].xs)
        self.assertEqual(len(self.conv_element.values[0].xs), 3049)
        self.assertAlmostEqual(sum(self.conv_element.values[0].pds), 1)

        self.assertEqual(str(self.conv_element), '1\t: 10, 10')

        self.assertEqual(self.conv_element.north, self.e_north)
        self.assertEqual(self.conv_element.south, self.e_south)
        self.assertEqual(self.conv_element.east, self.e_east)
        self.assertEqual(self.conv_element.west, self.e_west)

        self.assertTrue(self.conv_element.fo < 0.25)
        self.assertAlmostEqual(self.conv_element.fo, 0.143)

        self.assertTrue(self.conv_element.values[0].is_valid_pdf())
        self.assertEqual(self.conv_element.values[0].delta, 1e-2)
#
    def test_element_calculate(self):

        self.conv_element.calculate()
        self.assertEqual(len(self.conv_element.values), 2)
        print(self.conv_element.values[0].mean)
        print(self.conv_element.values[0].std)
        self.assertTrue(self.conv_element.values[0].is_valid_pdf())
        self.assertEqual(self.conv_element.values[1].delta, 1e-2)
        # self.assertTrue(self.conv_element.values[1].is_valid_pdf())

        print(self.conv_element.values[1].mean)
        print(self.conv_element.values[1].std)
        print(self.conv_element.values[1].xs)
        print(self.conv_element.values[1].pds)
        print(sum(self.conv_element.values[1].pds))


class TestConvFdm(unittest.TestCase):
    def setUp(self):
        self.cov_fdm = ConvFdm()
        self.cov_fdm.read_file('conv_fdm.csv')

    def test_create_fdm(self):
        self.assertEqual(self.cov_fdm.dx, 1e-3)
        self.assertEqual(len(self.cov_fdm.elements), 182)
        self.assertEqual(len(self.cov_fdm.get_domains()), 132)
        self.assertEqual(len(self.cov_fdm.get_boundaries()), 50)
        self.assertEqual(self.cov_fdm.elements[14]._id, 15)
        self.assertEqual(self.cov_fdm.elements[14].north._id, 2)
        self.assertEqual(self.cov_fdm.elements[14].south._id, 28)
        self.assertEqual(self.cov_fdm.elements[14].west._id, 14)
        self.assertEqual(self.cov_fdm.elements[14].east._id, 16)

    def test_calculate(self):
        self.assertEqual(len(self.cov_fdm.elements[14].values), 1)
        self.cov_fdm.calculate()
        self.assertEqual(len(self.cov_fdm.elements[14].values), 2)
        self.cov_fdm.calculate()
        self.assertEqual(len(self.cov_fdm.elements[14].values), 3)
        self.cov_fdm.calculate(3)
        self.assertEqual(len(self.cov_fdm.elements[14].values), 6)

        self.cov_fdm.calculate(30)





if __name__ == '__main__':
    unittest.main()
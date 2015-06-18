import unittest

__author__ = 'saintdragon2'

from fda.element import Element
from fda.fdm import Fdm
from fda.coord import Coord

class TestCoord(unittest.TestCase):
    def test_create_coord(self):
        p01 = Coord(1, 1)
        p02 = Coord(2, 1)

        self.assertEqual( p01.distance(p02), 1)



class TestElement(unittest.TestCase):
    def setUp(self):
        dx = 1e-3
        self.d11 = Element(1, 'D', dx, 10, 10, 1.43e-7, 5)

        self.e_west = Element(2, 'B', dx, 9, 10, 1.43e-7, 100)
        self.e_east = Element(3, 'D', dx, 11, 10, 1.43e-7, 5)
        self.e_north = Element(4, 'B', dx, 10, 9, 1.43e-7, 100)
        self.e_south = Element(5, 'D', dx, 10, 11, 1.43e-7, 5)

        self.d11.set_neighbors(self.e_north, self.e_east, self.e_south, self.e_west)


    def test_create_element(self):
        self.assertEqual(self.d11._id, 1)
        self.assertEqual(self.d11._type, 'D')
        self.assertEqual(self.d11._dx, 0.001)
        self.assertEqual(self.d11.get_x(), 10)
        self.assertEqual(self.d11.get_y(), 10)

        self.assertEqual(len(self.d11.values), 1)

        self.assertEqual(self.d11.north, self.e_north)
        self.assertEqual(self.d11.east, self.e_east)
        self.assertEqual(self.d11.south, self.e_south)
        self.assertEqual(self.d11.west, self.e_west)

        self.assertEqual(self.d11.diffusion_coeff, 1.43e-7)
        self.assertAlmostEqual(self.d11.dt, 1.7482517)
        self.assertEqual(self.d11.fo, 0.25)

        self.assertEqual(self.d11.diffusion_coeff, 1.43e-7)
        self.assertAlmostEqual(self.d11.dt, 1.7482517)
        self.assertEqual(self.d11.fo, 0.25)

    def test_element_calculate(self):
        self.d11.calculate()
        self.assertEqual(len(self.d11.values), 2)
        self.assertEqual(self.d11.values[1], 52.5)

        self.e_north.calculate()
        self.assertEqual(len(self.e_north.values), 1)


class TestFdm(unittest.TestCase):
    def test_read_fdm(self):
        fdm = Fdm()
        fdm.read_file('fdm00.csv')

        self.assertEqual(fdm.dx, 1e-3)


    # def setUp(self):
    #
    #     dx = 1e-3
    #     d11 = Element(1, 'D', dx, 10, 10, 1.43e-7, 5)
    #
    #     e_west = Element(2, 'B', dx, 9, 10, 1.43e-7, 100)
    #     e_east = Element(3, 'D', dx, 11, 10, 1.43e-7, 5)
    #     e_north = Element(4, 'B', dx, 10, 9, 1.43e-7, 100)
    #     e_south = Element(5, 'D', dx, 10, 11, 1.43e-7, 5)
    #
    #     d11.set_neighbors(e_north, e_east, e_south, e_west)
    #
    #     self.fdm  = Fdm([d11, e_north, e_east, e_south, e_west])
    #
    # def test_create_fdm(self):
    #     self.assertEqual( len(self.fdm.elements), 5)

    # def test_calculate(self):
    #     self.assertEqual(len(self.fdm.elements[0].values), 1)
    #     self.fdm.calculate()
    #     self.assertEqual(len(self.fdm.elements[0].values), 2)



if __name__ == '__main__':
    unittest.main()
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
        self.assertEqual( str(p01), '1, 1')



class TestElement(unittest.TestCase):
    def setUp(self):
        dx = 1e-3
        self.d11 = Element(1, 'D', dx, 10, 10, 1.43e-7, 5)

        self.e_west = Element(2, 'B', dx, 9, 10, 1.43e-7, 100)
        self.e_east = Element(3, 'D', dx, 11, 10, 1.43e-7, 5)
        self.e_north = Element(4, 'B', dx, 10, 9, 1.43e-7, 100)
        self.e_south = Element(5, 'D', dx, 10, 11, 1.43e-7, 5)

        self.d11.set_neighbors(self.e_north, self.e_east, self.e_south, self.e_west)
        self.d11.set_fo(0.5) #1.7482517482517481
        self.e_west.set_fo(0.5)
        self.e_east.set_fo(0.5)
        self.e_south.set_fo(0.5)
        self.e_north.set_fo(0.5)


    def test_create_element(self):
        self.assertEqual(self.d11._no, 1)
        self.assertEqual(self.d11._type, 'D')
        self.assertEqual(self.d11._dx, 0.001)
        self.assertEqual(self.d11.get_x(), 10)
        self.assertEqual(self.d11.get_y(), 10)

        self.assertEqual(str(self.d11), '1\t: 10, 10')

        self.assertEqual(len(self.d11.values), 1)

        self.assertEqual(self.d11.north, self.e_north)
        self.assertEqual(self.d11.east, self.e_east)
        self.assertEqual(self.d11.south, self.e_south)
        self.assertEqual(self.d11.west, self.e_west)

        self.assertEqual(self.d11.diffusion_coeff, 1.43e-7)
        self.assertEqual(self.d11.dt, 0.5)
        self.assertAlmostEqual(self.d11.fo,  0.0715)

        self.assertEqual(self.d11.diffusion_coeff, 1.43e-7)
        self.assertEqual(self.d11.dt, 0.5)
        self.assertAlmostEqual(self.d11.fo, 0.0715)

    def test_element_calculate(self):
        self.d11.calculate()
        self.assertEqual(len(self.d11.values), 2)
        self.assertEqual(self.d11.values[1], 18.585)

        self.e_north.calculate()
        self.assertEqual(len(self.e_north.values), 1)


class TestFdm(unittest.TestCase):
    def setUp(self):
        self.fdm = Fdm()
        self.fdm.read_file('fdm00.csv')

    def test_read_fdm(self):

        self.assertEqual(self.fdm.dx, 1e-3)
        self.assertEqual(len(self.fdm.elements), 182)
        self.assertEqual(len(self.fdm.get_boundaries()), 50)
        self.assertEqual(self.fdm.elements[14]._id, 15)
        self.assertEqual(self.fdm.elements[14].north._id, 2)
        self.assertEqual(self.fdm.elements[14].south._id, 28)
        self.assertEqual(self.fdm.elements[14].west._id, 14)
        self.assertEqual(self.fdm.elements[14].east._id, 16)

    def test_calculate_fdm(self):
        self.assertEqual(len(self.fdm.elements[14].values), 1)
        self.fdm.calculate()
        self.assertEqual(len(self.fdm.elements[14].values), 2)
        self.fdm.calculate()
        self.assertEqual(len(self.fdm.elements[14].values), 3)
        self.fdm.calculate(3)
        self.assertEqual(len(self.fdm.elements[14].values), 6)

        self.fdm.calculate(30)

class TestMirrorFdm(unittest.TestCase):
    def setUp(self):
        self.fdm = Fdm()
        self.fdm.read_file('fdm00_mirror.csv')

    def test_read_fdm(self):
        self.assertEqual(self.fdm.dx, 1e-3)

if __name__ == '__main__':
    unittest.main()
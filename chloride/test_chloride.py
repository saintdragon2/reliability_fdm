__author__ = 'SungYong'

import unittest

from chloride.coeffs import DiffCoeff, SurfaceChloride
from chloride.cl_element import ClElement, MirrorElement
from chloride.cl_fdm import ClFdm


class TestDiffCoeff(unittest.TestCase):
    def test_create_diff_coeff(self):
        diff_coeff = DiffCoeff(5.78e-12, 1)

        self.assertEqual(diff_coeff.d_ref, 5.78e-12)
        self.assertEqual(diff_coeff.t_ref, 1)

        self.assertEqual(diff_coeff.t(1), 5.78e-12)
        self.assertEqual(diff_coeff.t(35), 2.927545054168043e-12)

        self.assertEqual(diff_coeff.t(10), 3.646933451095517e-12)


class TestSurfaceChloride(unittest.TestCase):
    def test_surface_chloride(self):
        surface_cl = SurfaceChloride(1.52, 3.77)

        self.assertEqual(surface_cl.alpha, 1.52)
        self.assertEqual(surface_cl.beta, 3.77)

        self.assertEqual(surface_cl.t(0), 0)
        self.assertEqual(surface_cl.t(1), 2.3747663834483794)


class TestChlorideElement(unittest.TestCase):
    def test_create_cl_element(self):
        cl_element = ClElement(1, 'D', 1, 10, 10, 1.43e-7)

        self.assertEqual(len(cl_element.values), 1)

    def test_mirror_element(self):
        d_element = ClElement(14, 'D', 1, 6, 1, 1.43e-7)
        mw_element = MirrorElement(16, 'M_W', 1, 8, 1, 1.43e-7)
        mw_element.set_original(d_element)

        self.assertEqual(mw_element.get_id(), 16)
        self.assertEqual(mw_element.original, d_element)




class TestChlorideFdm(unittest.TestCase):
    def setUp(self):
        self.cl_fdm = ClFdm()
        self.cl_fdm.read_file('500.csv')

    def test_read_file(self):
        self.assertEqual(self.cl_fdm.dt, 1)
        self.assertEqual(self.cl_fdm.dx, 1e-2)

        self.assertEqual(len(self.cl_fdm.elements), 251502)
        self.assertEqual(len(self.cl_fdm.get_boundaries()), 2002)

        self.assertEqual(self.cl_fdm.elements[502].get_id(), 503)
        self.assertEqual(self.cl_fdm.elements[502].north.get_id(), 2)
        self.assertEqual(self.cl_fdm.elements[502].south.get_id(), 1004)
        self.assertEqual(self.cl_fdm.elements[502].west.get_id(), 502)
        self.assertEqual(self.cl_fdm.elements[502].east.get_id(), 504)

        self.assertEqual(self.cl_fdm.elements[14].dt, 1)

    def test_calculate_fdm(self):
        self.assertEqual(len(self.cl_fdm.elements[502].values), 1)
        self.cl_fdm.calculate()
        self.assertEqual(len(self.cl_fdm.elements[502].values), 2)
        self.cl_fdm.calculate()
        self.assertEqual(len(self.cl_fdm.elements[502].values), 3)
        self.cl_fdm.calculate(3)
        self.assertEqual(len(self.cl_fdm.elements[502].values), 6)

        self.cl_fdm.calculate(30)

    # def test_mirror(self):
    #     mirror_fdm = ClFdm()
    #     mirror_fdm.read_file('src294_mirror.csv')
    #
    #     mirror_fdm.calculate(100)
    #
    #     self.assertAlmostEqual(mirror_fdm.elements[21].values[99], 15.222799073414075)

if __name__ == '__main__':
    unittest.main()

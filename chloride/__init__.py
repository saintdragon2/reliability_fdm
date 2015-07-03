__author__ = 'saintdragon2'


import unittest

from chloride.coeffs import DiffCoeff, SurfaceChloride


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
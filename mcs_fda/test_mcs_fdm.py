__author__ = 'SungYong'

import unittest
import numpy
from mcs_fda.mcs_fdm import McsFdm

class TestMcsFdm(unittest.TestCase):
    def setUp(self):
        self.mcs_fdm = McsFdm()
        self.mcs_fdm.read_file('mcs_fdm.csv')

    def test_read_mcs_fdm(self):
        self.assertEqual(self.mcs_fdm.fdms[0].dx, 1e-3)
        self.assertEqual(self.mcs_fdm.runs, 1000)
        self.assertEqual(len(self.mcs_fdm.fdms), 1000)
        self.assertEqual(self.mcs_fdm.fdms[0].xs, 13)
        # self.assertEqual(len(self.mcs_fdm.initial_condition), 4)

        self.assertEqual(len(self.mcs_fdm.fdms[0].elements), 182)
        self.assertEqual(len(self.mcs_fdm.fdms[0].get_boundaries()), 50)
        self.assertEqual(self.mcs_fdm.fdms[0].elements[20].diffusion_coeff, 1.43e-7)

    def test_calculate(self):
        self.mcs_fdm.calculate()

        self.assertEqual(len(self.mcs_fdm.fdms[0].get_domains()[0].values), 2)

        self.mcs_fdm.calculate(10)
        self.assertEqual(len(self.mcs_fdm.fdms[0].get_domains()[0].values), 12)

        self.assertEqual(len(self.mcs_fdm.mcs_elements), 182)
        self.assertEqual(len(self.mcs_fdm.mcs_elements[0].elements), 1000)

        self.assertTrue(self.mcs_fdm.mcs_elements[0].is_boundary())
        self.assertTrue(self.mcs_fdm.mcs_elements[15].is_domain())

        self.assertAlmostEqual(self.mcs_fdm.mcs_elements[0].mean(0), 100, delta=1 )
        self.assertAlmostEqual(self.mcs_fdm.mcs_elements[0].std(0), 4, delta=0.3)








if __name__ == '__main__':
    unittest.main()

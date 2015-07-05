__author__ = 'SungYong'

import unittest

from mcs_chloride.mcs_cl_fdm import ReliabilityClFdm

class TestMcsFdm(unittest.TestCase):
    def setUp(self):
        self.reliability_fdm = ReliabilityClFdm()
        self.reliability_fdm.read_file('src294.csv')

    def test_read_mcs_fdm(self):
        self.assertEqual(self.reliability_fdm.runs, 5)
        self.assertEqual(self.reliability_fdm.dx, 1e-2)
        self.assertEqual(self.reliability_fdm.dt, 0.05)

        self.assertEqual(len(self.reliability_fdm.fdms), 5)

        # self.assertEqual(self.mcs_cl_fdm.fdms[0].dx, 1e-3)
        # self.assertEqual(self.mcs_cl_fdm.runs, 1000)
        # self.assertEqual(len(self.mcs_cl_fdm.fdms), 1000)
        # self.assertEqual(self.mcs_cl_fdm.fdms[0].xs, 13)
        # # self.assertEqual(len(self.mcs_fdm.initial_condition), 4)
        #
        # self.assertEqual(len(self.mcs_cl_fdm.fdms[0].elements), 182)
        # self.assertEqual(len(self.mcs_cl_fdm.fdms[0].get_boundaries()), 50)
        # self.assertEqual(self.mcs_cl_fdm.fdms[0].elements[20].diffusion_coeff, 1.43e-7)
        #

if __name__ == '__main__':
    unittest.main()

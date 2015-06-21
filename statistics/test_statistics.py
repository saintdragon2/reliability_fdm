__author__ = 'SungYong'
import unittest
import numpy
import scipy.stats
import math
from statistics.normpdf import NormPdf


class TestMcsFdm(unittest.TestCase):
    # def setUp(self):
    #     self.pdf = Pdf()

    def test_create_pdf(self):

        pdf_x = NormPdf(40, 2)

        self.assertEqual(pdf_x.mean, 40)
        self.assertEqual(pdf_x.std, 2)
        self.assertEqual(len(pdf_x.xs), 201)
        self.assertEqual(pdf_x.xs[0], -60)
        self.assertEqual(pdf_x.xs[200], 140)

        xs_x = []
        pds_x = []

        for i in range(0, 120):
            xs_x.append(i)
            pds_x.append(scipy.stats.norm(40, 2).pdf(i))

        pdf_with_list = NormPdf(xs=xs_x, pds=pds_x)

        self.assertEqual(pdf_with_list.mean, 40)
        self.assertAlmostEqual(pdf_with_list.std, 2)

    def test_multiplication_pdf(self):
        xs_x = []
        pds_x = []

        for i in range(0, 120):
            xs_x.append(i)
            pds_x.append(scipy.stats.norm(40, 2).pdf(i))

        pdf_x = NormPdf(xs=xs_x, pds=pds_x)

        xs_y  = []
        pds_y = []

        for i in range(0, 200):
            xs_y.append(i)
            pds_y.append(scipy.stats.norm(50, 3).pdf(i))

        pdf_y = NormPdf(xs=xs_y, pds=pds_y)

        pdf_z = pdf_x.mult(pdf_y)

        print(pdf_z.mean)
        print(pdf_z.std)

        print(pdf_z.xs[0])
        print(pdf_z.pds[0])

        pdf_zx = pdf_z.mult(pdf_x)
        print(pdf_zx.mean)
        print(pdf_zx.std)
        print(len(pdf_zx.xs))
        print(pdf_zx.pds[1])



if __name__ == '__main__':
    unittest.main()

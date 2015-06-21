__author__ = 'SungYong'

import unittest

from convolution_fdm.conv_element import ConvElement

class TestConvElement(unittest.TestCase):
    def test_create_conv_element(self):
        conv_element = ConvElement(1, 'D', 1, 10, 10, 1.43e-7, 5.0, 1.5)
        self.assertEqual(conv_element._id, 1)
        self.assertEqual(conv_element._type, 'D')
        self.assertEqual(conv_element._dx, 1)
        self.assertEqual(conv_element.get_x(), 10)
        self.assertEqual(conv_element.get_y(), 10)

        self.assertEqual(conv_element.values[0].mean, 5.0)
        self.assertEqual(conv_element.values[0].std, 1.5)

        print(conv_element.values[0].xs[0])
        print(conv_element.values[0].pds[0])
        print(len(conv_element.values[0].xs))

        self.assertEqual(str(conv_element), '1\t: 10, 10')
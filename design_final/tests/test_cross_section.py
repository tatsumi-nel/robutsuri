import unittest

import sys
sys.path.append('../lib')

from node import Node
from cross_section import CrossSection

class NodeTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()
        xs.set_d(1.0)
        xs.set_siga(2.0)
        xs.set_nusigf(3.0)
        self.assertEqual(xs.dif(), 1.0)
        self.assertEqual(xs.siga(), 2.0)
        self.assertEqual(xs.nusigf(), 3.0)
 
    def test_sets3(self):
        xs1 = CrossSection()
        xs1.set([1.0, 2.0, 3.0])
        xs1_ref = CrossSection()
        xs1_ref.set(xs1)
        self.assertEqual(xs1, xs1_ref)
    
    def test_operation_add(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = CrossSection([2.0, 3.0, 4.0])
        xs3 = xs1 + xs2
        xs3_ref = CrossSection([3.0, 5.0, 7.0])
        self.assertEqual(xs3, xs3_ref)

    def test_operation_sub(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = CrossSection([2.0, 3.0, 4.0])
        xs3 = xs2 - xs1
        xs3_ref = CrossSection([1.0, 1.0, 1.0])
        self.assertEqual(xs3, xs3_ref)

    def test_operation_mul(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = xs1 * 2.0
        xs2_ref = CrossSection([2.0, 4.0, 6.0])
        self.assertEqual(xs2, xs2_ref)

        xs3 = 2.0 * xs1
        xs3_ref = CrossSection([2.0, 4.0, 6.0])
        self.assertEqual(xs3, xs3_ref)

        xs4 = 2.0 * xs1 * 3.0
        xs4_ref = CrossSection([6.0, 12.0, 18.0])
        self.assertEqual(xs4, xs4_ref)

if( __name__ == '__main__'):
    unittest.main()

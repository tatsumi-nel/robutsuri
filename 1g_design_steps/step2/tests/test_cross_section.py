import unittest

import sys
sys.path.append('../lib')

from node import Node
from cross_section import CrossSection

class CrossSectionTest(unittest.TestCase):

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
    

if __name__ == '__main__':
    unittest.main()

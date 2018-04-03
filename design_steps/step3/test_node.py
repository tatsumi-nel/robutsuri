import unittest

from lib.node import Node
from lib.cross_section import CrossSection

class NodeTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()

        xs.set_d(1.0)
        xs.set_sigr(2.0)
        xs.set_nusigf(3.0)
        xs.set_sigf(4.0)
        
        self.assertEqual(xs.get_d(), 1.0)
        self.assertEqual(xs.get_sigr(), 2.0)
        self.assertEqual(xs.get_nusigf(), 3.0)
        self.assertEqual(xs.get_sigf(), 4.0)

    def test_sets2(self):
        xs = CrossSection()

        xs.set([1.0, 2.0, 3.0, 4.0])
                
        self.assertEqual(xs.get_d(), 1.0)
        self.assertEqual(xs.get_sigr(), 2.0)
        self.assertEqual(xs.get_nusigf(), 3.0)
        self.assertEqual(xs.get_sigf(), 4.0)

    def test_sets3(self):
        xs = CrossSection()
        xs.set([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(xs.get(), [1.0, 2.0, 3.0, 4.0])
    
    def test_operation_add(self):
        xs1 = CrossSection()
        xs1.set([1.0, 2.0, 3.0, 4.0])
        xs2 = CrossSection()
        xs2.set([2.0, 3.0, 4.0, 5.0])
        xs3 = xs1 + xs2
        self.assertEqual(xs3.get(), [3.0, 5.0, 7.0, 9.0])

    def test_operation_sub(self):
        xs1 = CrossSection()
        xs1.set([1.0, 2.0, 3.0, 4.0])
        xs2 = CrossSection()
        xs2.set([2.0, 3.0, 4.0, 5.0])
        xs3 = xs2 - xs1
        self.assertEqual(xs3.get(), [1.0, 1.0, 1.0, 1.0])

    def test_operation_mul(self):
        xs1 = CrossSection()
        xs1.set([1.0, 2.0, 3.0, 4.0])
        xs2 = xs1 * 2.0
        self.assertEqual(xs2.get(), [2.0, 4.0, 6.0, 8.0])
        xs3 = 2.0 * xs1
        self.assertEqual(xs3.get(), [2.0, 4.0, 6.0, 8.0])

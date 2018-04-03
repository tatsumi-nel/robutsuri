import unittest

from lib.node import Node
from lib.cross_section import CrossSection

class NodeTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()

        xs.set_d(1.0)
        xs.set_sigtr(2.0)
        xs.set_nusigf(3.0)
        xs.set_sigf(4.0)
        
        self.assertEqual(xs.get_d(), 1.0)
        self.assertEqual(xs.get_sigtr(), 2.0)
        self.assertEqual(xs.get_nusigf(), 3.0)
        self.assertEqual(xs.get_sigf(), 4.0)

    def test_sets2(self):
        xs = CrossSection()

        xs.set([1.0, 2.0, 3.0, 4.0])
                
        self.assertEqual(xs.get_d(), 1.0)
        self.assertEqual(xs.get_sigtr(), 2.0)
        self.assertEqual(xs.get_nusigf(), 3.0)
        self.assertEqual(xs.get_sigf(), 4.0)

    
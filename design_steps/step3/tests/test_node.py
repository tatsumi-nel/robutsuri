import unittest

import sys
sys.path.append('../')

from lib.node import Node
from lib.cross_section import CrossSection

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.xs = CrossSection()
        self.xs.set_d(0, 1.58)
        self.xs.set_d(1, 0.271)
        self.xs.set_siga(0, 0.0200)
        self.xs.set_siga(1, 0.0930)
        self.xs.set_sigs(0, 0.0178)  # down scatter only
        self.xs.set_sigs(1, 0.0000)  # dummy
        self.xs.set_nusigf(0, 0.0)
        self.xs.set_nusigf(1, 0.168)
        self.xs.set_xi(0, 1.0)
        self.xs.set_xi(1, 0.0)

    def test_set1(self):
        self.assertEqual(self.xs.get_d(0), 1.58)
        self.assertEqual(self.xs.get_d(1), 0.271)
        self.assertEqual(self.xs.get_siga(0), 0.0200)
        self.assertEqual(self.xs.get_siga(1), 0.0930)
        self.assertEqual(self.xs.get_sigs(0), 0.0178)
        self.assertEqual(self.xs.get_sigs(1), 0.0)
        self.assertEqual(self.xs.get_nusigf(0), 0.0)
        self.assertEqual(self.xs.get_nusigf(1), 0.168)
        self.assertEqual(self.xs.get_xi(0), 1.0)
        self.assertEqual(self.xs.get_xi(1), 0.0)

    def test_set2(self):
        xs2 = CrossSection()
        xs2.set_d(0, 1.58)
        xs2.set_d(1, 0.271)
        xs2.set_siga(0, 0.0200)
        xs2.set_siga(1, 0.0930)
        xs2.set_sigs(0, 0.0178)  # down scatter only
        xs2.set_sigs(1, 0.0000)  # dummy
        xs2.set_nusigf(0, 0.0)
        xs2.set_nusigf(1, 0.168)
        xs2.set_xi(0, 1.0)
        xs2.set_xi(1, 0.0)
        
        self.assertEqual(self.xs,  xs2)

        xs3 = xs2 * 2.0
        self.assertNotEqual(self.xs, xs3)
        
        xs4 = xs2 + xs2
        self.assertEqual(xs4, xs3)

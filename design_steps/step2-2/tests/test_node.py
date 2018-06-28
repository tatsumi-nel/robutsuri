import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_onenode(self):
        node = Node()
        xs = CrossSection([1.36, 0.0181, 0.0279])
        #xs.debug()
        node.set_xs(xs)
        node.set_keff( xs.nusigf() / xs.siga() )    
        node.calc()

        for k in range(100):
            jout_xm = node.get_jout(XM)
            jout_xp = node.get_jout(XP)
            node.set_jin(XM, jout_xm)
            node.set_jin(XP, jout_xp)
            node.calc()

        node.debug()

        self.assertEqual(node.get_jout(XM), node.get_jout(XP))
        self.assertEqual(node.get_jin(XM), node.get_jout(XM))
        self.assertEqual(node.get_jin(XP), node.get_jout(XP))
        self.assertEqual(node.get_jout(XM)+node.get_jin(XM), node.get_flux() / 2.0)


if __name__ == '__main__':
    unittest.main()
    
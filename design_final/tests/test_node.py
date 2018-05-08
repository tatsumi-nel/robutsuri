import unittest

import sys
sys.path.append('../lib')

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_uniform(self):
        node = Node()
        xs = CrossSection([1.36, 0.0181, 0.0279])
        xs.debug()
        node.set_xs(xs)
        node.set_keff( xs.nusigf() / xs.siga() )    
        node.calc()

        for k in range(100):
            node.calc()

        self.assertEqual(node.get_jout(XM), node.get_jout(XP))
        self.assertEqual(node.get_jin(XM), node.get_jout(XM))
        self.assertEqual(node.get_jin(XP), node.get_jout(XP))
        self.assertEqual(node.get_jout(XM)+node.get_jin(XM), node.get_flux() / 2.0)



    def test_twonodes(self):
        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        xs_ref  = CrossSection([0.55, 0.0127, 0.0])
        delta = 1.0
        geom = [{'xs':xs_ref, 'width':30}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':30} ]

        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)
        
        keff_old = 1.0
        conv = 1.0e-5
        for ik in range(2000):  # outer iteration

            for istart in range(2):  # start color (0: red, 1:black)
                for ix in range(istart, len(nodes), 2):
                    if(ix==0):
                        jin_xm = -nodes[ix].get_jout(XM)
                    else:
                        jin_xm = nodes[ix-1].get_jout(XP)
                    
                    if(ix==len(nodes)-1):
                        jin_xp = -nodes[ix].get_jout(XP)
                    else:
                        jin_xp = nodes[ix+1].get_jout(XM)

                    nodes[ix].set_jin(XM, jin_xm)
                    nodes[ix].set_jin(XP, jin_xp)
                    nodes[ix].calc()

            # red/black done
            rr = CrossSection()
            for ix in range(len(nodes)):
                the_node = nodes[ix]
                rr = rr + the_node.get_xs() * the_node.get_flux() * the_node.get_width()
            
            keff = rr.nusigf() / rr.siga()
            diff = abs((keff - keff_old)/keff)
            print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff            

            for ix in range(len(nodes)):
                nodes[ix].set_keff(keff)
            
        # debug
        print("flux")
        for ix in range(len(nodes)):
            print(ix, nodes[ix].get_flux())


if __name__ == '__main__':
    unittest.main()
    
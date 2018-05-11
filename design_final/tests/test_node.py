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
            node.calc()

        self.assertEqual(node.get_jout(XM), node.get_jout(XP))
        self.assertEqual(node.get_jin(XM), node.get_jout(XM))
        self.assertEqual(node.get_jin(XP), node.get_jout(XP))
        self.assertEqual(node.get_jout(XM)+node.get_jin(XM), node.get_flux() / 2.0)


    def test_uniform_zeroflux_bc(self):
        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)
        
        keff_old = 1.0
        pro_old = 1.0
        conv = 1.0e-7
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
            for the_node in nodes:
                rr = rr + the_node.get_xs() * the_node.get_flux() * the_node.get_width()
            
            #keff = rr.nusigf() / rr.siga()
            keff = rr.nusigf() / (pro_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            #print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff
            pro_old = rr.nusigf()

            for the_node in nodes:
                the_node.set_keff(keff)
            
        # debug
        #print("flux")
        #for ix in range(len(nodes)):
        #    print(ix, nodes[ix].get_flux())
    
        
        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=5)


    def test_two_regions_zeroflux_bc(self):
        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        xs_ref  = CrossSection([0.55, 0.0127, 0.0])
        delta = 1.0
        geom = [{'xs':xs_ref, 'width':60}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':60} ]

        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)
        
        keff_old = 1.0
        pro_old = 1.0
        conv = 1.0e-7
        for ik in range(3000):  # outer iteration

            for color in range(2):  # color (0: red, 1:black)
                for ix in range(color, len(nodes), 2):
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
            for the_node in nodes:
                rr = rr + the_node.get_xs() * the_node.get_flux() * the_node.get_width()
            
            #keff = rr.nusigf() / rr.siga()
            keff = rr.nusigf() / (pro_old/keff_old)
            diff = abs((keff - keff_old)/keff)

            #if( ik % 100 == 0):
                #print( ik, keff, diff)

            if(diff < conv):
                break
            keff_old = keff
            pro_old = rr.nusigf()

            for the_node in nodes:
                the_node.set_keff(keff)
            
        # debug
        #print("flux")
        #for ix in range(len(nodes)):
        #    print(ix, nodes[ix].get_flux())

        #print("keff=",keff)
        # self.assertAlmostEqual(keff, 1.41102, places=5)  # keff with strict condition
        self.assertAlmostEqual(keff, 1.41124, places=5)  # keff with strict condition

if __name__ == '__main__':
    unittest.main()
    
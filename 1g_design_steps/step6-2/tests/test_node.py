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

        for k in range(1000):
            jout_xm = node.get_jout(XM)
            jout_xp = node.get_jout(XP)
            node.set_jin(XM, jout_xm)
            node.set_jin(XP, jout_xp)
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
        
        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7

        for idx_outer in range(2000):  # outer iteration

            # calculation of total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                total_fis_src += the_node.get_fis_src()
            
            # normalize fis src to make total fis src unity
            norm_factor = 1.0 / (total_fis_src/keff)
            for the_node in nodes:
                the_node.normalize_fis_src(norm_factor)

            # inner iteration with fixed fis src
            for istart in range(2):  # start color (0: red, 1:black)
                for ix in range(istart, len(nodes), 2):
                    if(ix==0):  # left boundary
                        jin_xm = -nodes[ix].get_jout(XM)
                    else:
                        jin_xm = nodes[ix-1].get_jout(XP)
                    
                    if(ix==len(nodes)-1):  # right boundary
                        jin_xp = -nodes[ix].get_jout(XP)
                    else:
                        jin_xp = nodes[ix+1].get_jout(XM)

                    nodes[ix].set_jin(XM, jin_xm)
                    nodes[ix].set_jin(XP, jin_xp)
                    nodes[ix].calc()
            
            # calculation of new fission source
            for the_node in nodes:
                the_node.calc_fis_src()
            
            # calculation of total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                total_fis_src += the_node.get_fis_src()
            
            # estimation of eigen value as a ratio of generations
            keff = total_fis_src / (total_fis_src_old/keff_old)
                                  
            diff = abs((keff - keff_old)/keff)
            #print(idx_outer, keff, diff)

            if(diff < conv):  
                break

            keff_old = keff
            total_fis_src_old = total_fis_src

            # set new eigen value to all the nodes
            for the_node in nodes:
                the_node.set_keff(keff)
            

        # reference as analytical solution
        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=5)


if __name__ == '__main__':
    unittest.main()
    
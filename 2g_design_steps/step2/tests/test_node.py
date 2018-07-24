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
        xs = CrossSection()
        
        # two-group problem
        xs.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()
        
        #xs.debug()
        node.set_xs(xs)

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-10

        # outer iteration        
        for ik in range(1000):

            # normalize total fission source
            total_fis_src = 0.0
            for kg in range(2):
                total_fis_src += node.get_fis_src(kg) * node.get_width()
            factor = 1.0 / (total_fis_src/keff)

            for kg in range(2):
                node.normalize_fis_src(kg, factor)                

            # energy loop
            for kg in range(2):
                # update sources
                node.calc_scat_src(kg)

                # inner loop
                for i in range(4):
                    for dir in range(2):
                        node.set_jin(kg, dir, node.get_jout(kg, dir))
                    
                    # calculate jout, flux with response matrix
                    node.calc(kg)
            
                node.calc_fis_src(kg)

            # calc total fission source and k_eff
            total_fis_src = 0.0
            for kg in range(2):
                total_fis_src += node.get_fis_src(kg) * node.get_width()
                
            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            
            # convergence check
            if(diff < conv):
                break
            
            # update parameters
            total_fis_src_old = total_fis_src
            keff_old = keff
            node.set_keff(keff)
        
        # --- end of loop for outer iteration

        print("keff=", keff)

        # analytic solution by Eq.(67) on the page 114 where the buckling is zero.
        kana_nume = xs.sigr(1)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = xs.sigr(0) * xs.sigr(1)
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=5)

        for kg in range(2):
            self.assertAlmostEqual(node.get_jout(kg, XM), node.get_jout(kg, XP), places=5)
            self.assertAlmostEqual(node.get_jin(kg, XM), node.get_jout(kg, XM), places=5)
            self.assertAlmostEqual(node.get_jin(kg, XP), node.get_jout(kg, XP), places=5)
            self.assertAlmostEqual(node.get_jout(kg, XM)+node.get_jin(kg, XM), node.get_flux(kg) / 2.0, places=5)
    

if __name__ == '__main__':
    unittest.main()
    
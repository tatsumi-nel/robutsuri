import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_two_regions_zeroflux_bc(self):

        xs_fuel = CrossSection()
        xs_fuel.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs_fuel.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs_fuel.calc_sigr()
        
        xs_ref = CrossSection()
        xs_ref.set([[1.41, 0.0, 0.0, 1.0],[0.117, 0.0191, 0.0, 0.0]])
        xs_ref.set_smat( [[0.0, 0.0476], [0.0, 0.0]])
        xs_ref.calc_sigr()
    
        delta = 1.0
        geom = [{'xs':xs_ref, 'width':30}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':30} ]
        
        # geometry setting
        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)
        
        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-8
        
        # outer iteration
        for ik in range(100):

            # normalize total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()
            factor = 1.0 / (total_fis_src/keff)

            for the_node in nodes:
                for kg in range(2):
                    the_node.normalize_fis_src(kg, factor)       

            # energy loop
            for kg in range(2):

                # update scattering source
                for the_node in nodes:
                    the_node.calc_scat_src(kg)

                # inner loop
                for i in range(4):
                    for istart in range(2):  # start color (0: red, 1:black)
                        for ix in range(istart, len(nodes), 2):
                        
                            # pass partial currents to adjacent nodes
                            if(ix==0):
                                jin_xm = -nodes[ix].get_jout(kg, XM)
                            else:
                                jin_xm = nodes[ix-1].get_jout(kg, XP)
                            
                            if(ix==len(nodes)-1):
                                jin_xp = -nodes[ix].get_jout(kg, XP)
                            else:
                                jin_xp = nodes[ix+1].get_jout(kg, XM)

                            nodes[ix].set_jin(kg, XM, jin_xm)
                            nodes[ix].set_jin(kg, XP, jin_xp)
                            
                            # calculate jout, flux with response matrix
                            nodes[ix].calc(kg)
                
                # update fission source
                for the_node in nodes:
                    the_node.calc_fis_src(kg)

            # calc total fission source and keff
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()  
                
            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            
            # print( keff, diff)
            # convergence check
            if(diff < conv):
                break

            # update parameters
            total_fis_src_old = total_fis_src
            keff_old = keff
            for the_node in nodes:
                the_node.set_keff(keff)

        # --- end of loop for outer iterations

        # converged
        print("keff=", keff)
  
        #print("flux")
        #for ix in range(len(nodes)):
        #   print(ix, nodes[ix].get_flux())

        self.assertAlmostEqual(keff, 1.35826, places=5)  # keff with strict condition

if __name__ == '__main__':
    unittest.main()
    
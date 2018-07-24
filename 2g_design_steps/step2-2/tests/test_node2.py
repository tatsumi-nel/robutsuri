import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_uniform_zeroflux_bc(self):
        
        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        geom = [{'xs':xs, 'width':100}]

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

        # debug
        #print("fast flux")
        #for ix in range(len(nodes)):
        #    print(ix, nodes[ix].get_flux(0))

        b2 = (math.pi / geom[0]['width'])**2

        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)



if __name__ == '__main__':
    unittest.main()
    
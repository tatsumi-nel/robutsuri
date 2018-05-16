import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container

class ContainerTest(unittest.TestCase):

    def test_container(self):

        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        cont = Container(geom, delta, albedo)
        #cont.debug()
        
        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7
        
        for ik in range(100):

            total_fis_src = cont.get_total_fis_src()
            norm_factor = 1.0 / (total_fis_src/keff)
            cont.normalize_fis_src(norm_factor)

            for kg in range(2):
                for i in range(4):
                    for color in range(2):
                        cont.calc(kg, color)
            
                cont.calc_fis_src(kg)

            total_fis_src = cont.get_total_fis_src()
            
            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            #print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff
            total_fis_src_old = total_fis_src

            cont.set_keff(keff)

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_domi = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_domi
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)


        flux = cont.get_flux_dist(0)  # first energy
        self.assertEqual(len(flux), 2)  # x, y
        self.assertEqual(len(flux[0]), int(geom[0]['width']/delta))
        self.assertEqual(flux[0][0], delta/2.0)
        self.assertEqual(flux[0][-1], geom[0]['width']-delta/2.0)
        self.assertEqual(len(flux[1]), int(geom[0]['width']/delta))


if __name__ == '__main__':
    unittest.main()

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

        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        cont = Container(geom, delta, albedo)
        #cont.debug()

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7
        
        for idx_outer in range(100):

            total_fis_src = cont.get_total_fis_src()
            norm_factor = 1.0 / (total_fis_src/keff)
            cont.normalize_fis_src(norm_factor)

            for idx_inner in range(4):
                for color in range(2):
                    cont.calc(color)
        
            cont.calc_fis_src()

            total_fis_src = cont.get_total_fis_src()
            
            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            #print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff
            total_fis_src_old = total_fis_src

            cont.set_keff(keff)

        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=4)


        flux = cont.get_flux_dist()
        self.assertEqual(len(flux), 2)  # x, y
        self.assertEqual(len(flux[0]), int(geom[0]['width']/delta))
        self.assertEqual(flux[0][0], delta/2.0)
        self.assertEqual(flux[0][-1], geom[0]['width']-delta/2.0)
        self.assertEqual(len(flux[1]), int(geom[0]['width']/delta))


if __name__ == '__main__':
    unittest.main()

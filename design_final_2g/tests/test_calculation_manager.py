import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController
from calculation_manager import CalculationManager

class CalculationManagerTest(unittest.TestCase):

    def test_calculation_manager(self):

        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        config = { 'geometry':geom, 'mesh_width':delta, "albedo": albedo}
                
        calc_man = CalculationManager(config)
        calc_man.run()

        keff = calc_man.get_keff()

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_domi = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_domi
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)



if __name__ == '__main__':
    unittest.main()

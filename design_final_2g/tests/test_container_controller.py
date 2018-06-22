import unittest

import sys
sys.path.append('../lib')
import math


from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController


class ContainerContainerTest(unittest.TestCase):

    def test_container_controller(self):
        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        container = Container(geom, delta, albedo)
        #cont.debug()
        
        controller = ContainerController(container)
        
        controller.calc()

        keff = controller.get_keff()

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)


if __name__ == '__main__':
    unittest.main()

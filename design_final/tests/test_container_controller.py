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

        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        container = Container(geom, delta, albedo)
        #cont.debug()
        
        controller = ContainerController(container)
        
        controller.calc()

        keff = controller.get_keff()

        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=5)


if(__name__ == '__main__'):
    unittest.main()

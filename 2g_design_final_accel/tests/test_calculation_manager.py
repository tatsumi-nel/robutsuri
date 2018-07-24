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

        xs_fuel = CrossSection()
        xs_fuel.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs_fuel.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs_fuel.calc_sigr()
        
        xs_ref = CrossSection()
        xs_ref.set([[1.41, 0.0, 0.0, 1.0],[0.117, 0.0191, 0.0, 0.0]])
        xs_ref.set_smat( [[0.0, 0.0476], [0.0, 0.0]])
        xs_ref.calc_sigr()
    
        geom = [{'xs':xs_ref, 'width':30}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':30} ]
        
        delta = 1.0
        albedo = -1.0

        config = { 'geometry':geom, 'mesh_width':delta, 'albedo': albedo, 'max_iteration': 1000, \
                    'omega': 0.5, 'asymptotic_criteria': 0.05}
                
        calc_man = CalculationManager(config)
        count, flag = calc_man.run()
        print( "outer iterations:", count)

        keff = calc_man.get_keff()


        self.assertAlmostEqual(keff, 1.35826, places=5)  # keff with strict condition



if __name__ == '__main__':
    unittest.main()

import sys

sys.path.append('lib')
from calculation_manager import CalculationManager
from cross_section import CrossSection

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

print ("keff = ", keff)
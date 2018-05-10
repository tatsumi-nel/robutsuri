import sys

sys.path.append('lib')
from calculation_manager import CalculationManager
from cross_section import CrossSection

xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
delta = 1.0
albedo = -1.0
geom = [{'xs':xs_fuel, 'width':100}]

config = { 'geometry':geom, 'mesh_width':delta, "albedo": albedo}
        
calc_man = CalculationManager(config)
calc_man.run()

keff = calc_man.get_keff()

print ("keff = ", keff)
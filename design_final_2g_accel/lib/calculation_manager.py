from container import Container
from container_controller import ContainerController


class CalculationManager:

    def __init__(self, param):
        geom = param['geometry']
        delta = param['mesh_width']
        albedo = param['albedo']
        omega = param['omega']
        asym_cri = param['asymptotic_criteria']

        container = Container(geom, delta, albedo)
        container.set_omega(omega, asym_cri)
        
        self.controller = ContainerController(container)

    def run(self):
        return self.controller.calc()

    def get_keff(self):
        return self.controller.get_keff()



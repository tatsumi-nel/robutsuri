from cross_section import CrossSection

class Node:
    def __init__(self):
        self.j = [0.0, 0.0]
        self.flux = 0.0
        self.xs = CrossSection()
        
    def set_flux(self, f):
        self.flux = f

    def set_xs(self, xs):
        self.xs = xs

    def calc(self):
        pass

    def debug(self):
        print("--- Node ---------")
        print("flux = ", self.flux)
        print("j_x- = ", self.j[0])
        print("j_x+ = ", self.j[1])
        print("------------------")
        self.xs.debug()
    

if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    node.set_xs(xs)
    node.debug()

import numpy as np

class Node:
    def __init__(self):
        self.jp = np.zeros(2)
        self.jm = np.zeros(2)
        self.flux = np.zeros(2)
        self.xs = None
        
    def set_flux(self, kg, val):
        self.flux[kg] = val

    def set_xs(self, xs):
        self.xs = xs

    def calc(self):
        pass

    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print("kg\tjp\tjm\tflux")
        for kg in range(0,2):
            print(kg, self.jp[kg], self.jm[kg], self.flux[kg], sep='\t', end='\n')
        self.xs.debug()
        print("-"*50)


if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    node.set_xs(xs)
    node.debug()

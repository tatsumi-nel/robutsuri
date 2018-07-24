import numpy as np
from cross_section import CrossSection
from config import *

class Node:
    def __init__(self, xs=None):
        self.jout = np.ones(2)    # out-going, [XM, XP]
        self.jin  = np.ones(2)    # in-coming, [XM, XP]
        self.flux  = 1.0    # average flux
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = 1.0
        if(xs):
            self.set_xs(xs)

    def set_xs(self, val):
        self.xs = val

    def set_keff(self, val):
        self.keff = val
            
    def get_flux(self):
        return self.flux

    def set_jin(self, dir, val):
        self.jin[dir] = val

    def get_jin(self, dir):
        return self.jin[dir]

    def get_jout(self, dir):
        return self.jout[dir]

    def calc(self):
        self.flux = (self.jin[XM] + self.jin[XP])*2.0

    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print("  jin_XM \t", self.jin[XM] )
        print("  jin_XP \t", self.jin[XP])
        print("  jout_XM\t", self.jout[XM])
        print("  jout_XP\t", self.jout[XP])
        print("  flux   \t", self.flux)
        print("  keff   \t", self.keff)
        self.xs.debug()
        print("-"*50)


if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    node.set_xs(xs)
    node.debug()

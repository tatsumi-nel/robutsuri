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

    def set_width(self, val):
        self.width = val
            
    def get_flux(self):
        return self.flux

    def set_jin(self, dir, val):
        self.jin[dir] = val

    def get_jin(self, dir):
        return self.jin[dir]

    def get_jout(self, dir):
        return self.jout[dir]

    def get_xs(self):
        return self.xs

    def get_width(self):
        return self.width

    def get_fis_src(self):
        return self.fis_src

    def calc_fis_src(self):
        # fission source
        self.fis_src = self.xs.nusigf() * self.flux * self.width

    def normalize_fis_src(self, factor):
        self.fis_src *= factor

    def calc(self):
        src = self.xs.nusigf() * self.flux / self.keff

        #flux by Eq(28)
        coef1 = 2.0*self.xs.dif() / self.width
        coef2 = 2.0*coef1
        coef3 = 1.0 + coef2
        f_nume = coef1 * 4.0 * (self.jin[XP] + self.jin[XM]) + \
                 coef3 * self.width * src
        f_domi = coef2 + coef3*self.xs.siga()*self.width
        self.flux = f_nume / f_domi

        #net current by Eq(29)
        jnet_XM  = -coef1 * (4.0*self.jin[XM] - self.flux) / coef3
        jnet_XP = -coef1 * (4.0*self.jin[XP] - self.flux) / coef3

        #out-goinnt by Eq(30)
        self.jout[XM]  = jnet_XM  + self.jin[XM]
        self.jout[XP] = jnet_XP + self.jin[XP]

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

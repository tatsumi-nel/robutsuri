import numpy as np

from cross_section import *
from config import *

class Node:
    def __init__(self, xs=None, kg=2):
        self.jout = np.ones((kg,2))   # kg, out-going, [XM, XP]
        self.jin  = np.ones((kg,2))   # kg, in-coming, [XM, XP]
        self.flux  = np.ones(kg)      # average flux
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = np.ones(kg)
        self.scat_src = np.zeros(kg)
        if(xs):
            self.set_xs(xs)

    def set_xs(self, val):
        self.xs = val

    def set_keff(self, val):
        self.keff = val

    def set_width(self, val):
        self.width = val

    def set_flux(self, kg, val):
        self.flux[kg] = val
    
    def get_flux(self, kg):
        return self.flux[kg]

    def set_jin(self, kg, dir, val):
        self.jin[kg, dir] = val

    def get_jin(self, kg, dir):
        return self.jin[kg, dir]
    
    def get_jout(self, kg, dir):
        return self.jout[kg, dir]

    def get_xs(self):
        return self.xs

    def get_width(self):
        return self.width

    def get_fis_src(self, kg):
        return self.fis_src[kg]

    def calc_fis_src(self, kg):
        # fission source
        self.fis_src[kg] = self.xs.nusigf(kg) * self.flux[kg] * self.width

    def normalize_fis_src(self, kg, factor):
        self.fis_src[kg] *= factor

    def calc(self, kg):
        # scattering source
        s_scat = 0.0
        for kkg in range(self.xs.ng()):
            if kg != kkg:
                s_scat += self.xs.sigs(kkg, kg) * self.flux[kkg] * self.width

        # fission source        
        s_fis = 0.0
        for kkg in range(self.xs.ng()):
            s_fis += self.xs.xi(kg) * self.fis_src[kkg] / self.keff 

        #flux by Eq(28)
        coef1 = 2.0*self.xs.dif(kg) / self.width
        coef2 = 2.0*coef1
        coef3 = 1.0 + coef2
        f_nume = coef1 * 4.0 * (self.jin[kg, XP] + self.jin[kg, XM]) + coef3 * (s_fis + s_scat)
        f_domi = coef2 + coef3*self.xs.sigr(kg)*self.width
        self.flux[kg] = f_nume / f_domi

        #net current by Eq(29)
        jnet_XM  = -coef1 * (4.0*self.jin[kg, XM] - self.flux[kg]) / coef3
        jnet_XP = -coef1 * (4.0*self.jin[kg, XP] - self.flux[kg]) / coef3

        #out-goinnt by Eq(30)
        self.jout[kg, XM] = jnet_XM + self.jin[kg, XM]
        self.jout[kg, XP] = jnet_XP + self.jin[kg, XP]


    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print( "kg\tjin_XM\tjin_XP\tjout_XM\tjout_XP")
        for kg in range(self.xs.ng()):
            print(kg, self.jin[kg, XM], self.jin[kg, XP], self.jout[kg, XM], self.jout[kg, XP], sep='\t')

        print("  flux   \t", self.flux)
        print("  fis_src\t", self.fis_src)
        print("  scat_src\t", self.scat_src)
        print("  keff   \t", self.keff)
        
        self.xs.debug()
        print("-"*50)


if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    xs.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
    xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])

    xs.debug()
    node.set_xs(xs)

    b2 = 0.0
    kana_nume = (xs.siga(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
    kana_domi = (xs.dif(0)*b2 + xs.siga(0) ) * (xs.dif(1)*b2 + xs.siga(1))
    kana = kana_nume / kana_domi
    print("kana=", kana)

    node.set_keff( kana )
    node.debug()    
    
    for kg in range(2):
        node.calc(kg)
    
    node.debug()    

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
        s_fis = 0.0
        for kkg in range(self.xs.ng()):
            s_fis += self.xs.xi(kg) * self.xs.nusigf(kkg)*self.flux[kkg]
        self.fis_src[kg] = s_fis

    def calc_scat_src(self, kg):
        # scattering source
        s_scat = 0.0
        for kkg in range(self.xs.ng()):
            if kg != kkg:
                s_scat += self.xs.sigs(kkg, kg) * self.flux[kkg]
        self.scat_src[kg] = s_scat

    def normalize_fis_src(self, kg, factor):
        self.fis_src[kg] *= factor

    def calc(self, kg):
        #flux by Eq(28)
        coef1 = 2.0*self.xs.dif(kg) / self.width
        coef2 = 2.0*coef1
        coef3 = 1.0 + coef2
        f_nume = coef1 * 4.0 * (self.jin[kg, XP] + self.jin[kg, XM]) + coef3 * \
                (self.fis_src[kg]  / self.keff + self.scat_src[kg]) * self.width
        f_deno = coef2 + coef3*self.xs.sigr(kg)*self.width
        self.flux[kg] = f_nume / f_deno

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


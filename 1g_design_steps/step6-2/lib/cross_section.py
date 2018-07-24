import numpy as np
import copy

# 定数
N_REACT = 3  # D, Siga, nuSigf
DIF    = 0
SIGA   = 1
NUSIGF = 2

class CrossSection:
    """
        断面積クラス (1群)
    """

    def __init__(self, val=None):
        self.x = np.zeros(N_REACT)
        if(not (val is None)):
            self.set(val)

    def set(self, val):
        if (type(val) == CrossSection):
            self.x = copy.copy(val.x)
        else:
            for k in range(N_REACT):
                self.x[k] = val[k]

    def set_d(self, val):
        self.x[DIF] = val

    def set_siga(self, val):
        self.x[SIGA] = val

    def set_nusigf(self, val):
        self.x[NUSIGF] = val

    def dif(self):
        return self.x[DIF]

    def siga(self):
        return self.x[SIGA]

    def nusigf(self):
        return self.x[NUSIGF]

    def __eq__(self, other):
        return np.allclose(self.x, other.x)
            
    def __mul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        return xs

    def __rmul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        return xs

    def __truediv__(self, factor):
        xs = CrossSection(self)
        xs.x *= (1.0/factor)
        return xs

    def __neg__(self):
        return self * (-1.0)

    def __add__(self, other):
        xs = CrossSection(self)
        xs.x += other.x
        return xs
    
    def __sub__(self, other):
        xs = CrossSection(self) + (-other)
        return xs
    
    def debug(self):
        print("-" * 9 + " XS " + "-" * 9)
        print("D\tSiga\tNuSigf")
        print(self.x[DIF], self.x[SIGA], self.x[NUSIGF], sep='\t', end='\n')
        print("-"*22)


if __name__ == '__main__':
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    xs.debug()
    
    xs2 = xs * 2.0
    xs2.debug()

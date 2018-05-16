import numpy as np
import copy

# 大域変数
N_REACT = 5  # D, Siga, nuSigf, Xi, sigr
DIF    = 0
SIGA   = 1
NUSIGF = 2
XI     = 3
SIGR   = 4

class CrossSection:
    """
    断面積クラス (2群)
    """

    def __init__(self, val=None, ng=2):
        """
        コンストラクタ
        """
        self.x  = np.zeros((ng, N_REACT))
        self.sm = np.zeros((ng, ng))
        if not (val is None):
            self.set(val)

    def set(self, val):
        if type(val) == CrossSection:
            self.x = copy.copy(val.x)
            self.sm = copy.copy(val.sm)
        else: # リストの場合
            for kg in range(self.ng()):
                for i in range(len(val[kg])):
                    self.x[kg, i] = val[kg][i]

    def set_d(self, kg, val):
        self.x[kg, DIF] = val

    def set_siga(self, kg, val):
        self.x[kg, SIGA] = val

    def set_nusigf(self, kg, val):
        self.x[kg, NUSIGF] = val

    def set_xi(self, kg, val):
        self.x[kg, XI] = val

    def set_smat(self, mat):
        for kg in range(self.ng()):
            for i in range(self.ng()):
                self.sm[kg, i] = mat[kg][i]

    def calc_sigr(self):
        for kg in range(self.ng()):
            self.x[kg, SIGR] = self.x[kg, SIGA]
            for kkg in range(self.ng()):
                if kg != kkg:
                    self.x[kg, SIGR] += self.sm[kg,kkg]

    def ng(self):
        return self.x.shape[0]

    def dif(self, kg):
        return self.x[kg, DIF]

    def siga(self, kg):
        return self.x[kg, SIGA]

    def sigr(self, kg):
        return self.x[kg, SIGR]    

    def nusigf(self, kg):
        return self.x[kg, NUSIGF]
    
    def xi(self, kg):
        return self.x[kg, XI]

    def sigs(self, kg, kkg):
        return self.sm[kg, kkg]

    def __eq__(self, other):
        return np.allclose(self.x, other.x) and np.allclose(self.sm, other.sm)
            
    def __mul__(self, factor):
        # ここで val は float であることを前提とする
        xs = CrossSection(self)
        xs.x *= factor
        xs.sm *= factor
        return xs

    def __rmul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        xs.sm *= factor
        return xs

    def __truediv__(self, factor):
        xs = CrossSection(self)
        xs.x *= (1.0/factor)
        xs.sm *= (1.0/factor)
        return xs

    def __neg__(self):
        return self * (-1.0)

    def __add__(self, other):
        xs = CrossSection(self)
        xs.x += other.x
        xs.sm += other.sm
        return xs
    
    def __sub__(self, other):
        xs = CrossSection(self) + (-other)
        return xs
    
    def debug(self):
        print("-" * 9 + " XS " + "-" * 29)
        print("kg\tD\tSiga\tSigr\tNuSigf\tXi")
        for kg in range(self.x.shape[0]):
            print(kg, self.x[kg, DIF], self.x[kg, SIGA], self.x[kg, SIGR], self.x[kg, NUSIGF], self.x[kg, XI], sep='\t', end='\n')
        print( "smat")
        print( self.sm )
        print("-"*42)


if __name__ == '__main__':
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    xs.debug()
    
    xs2 = xs * 2.0
    xs2.debug()

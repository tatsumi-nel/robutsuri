import numpy as np

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
        """
        コンストラクタ
        """
        self.x = np.zeros(N_REACT)

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
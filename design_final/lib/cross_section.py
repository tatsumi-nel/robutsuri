import numpy as np

class CrossSection:

    def __init__(self, val):
        self.d      = np.zeros(2)
        self.siga   = np.zeros(2)
        self.nusigf = np.zeros(2)
        self.xi     = np.zeros(2)
        self.sigs   = np.zeros((2,2))

    def set_d(self, kg, val):
        self.d[kg] = val

    def set_siga(self, kg, val):
        self.siga[kg] = val

    def set_sigs(self, kg, val):
        self.sigs[kg] = val

    def set_nusigf(self, kg, val):
        self.nusigf[kg] = val

    def set_xi(self, kg, val):
        self.xi[kg] = val

    def get_d(self, kg):
        return self.d[kg]

    def get_siga(self, kg):
        return self.siga[kg]

    def get_sigs(self, kg):
        return self.sigs[kg]

    def get_nusigf(self, kg):
        return self.nusigf[kg]

    def get_xi(self, kg):
        return self.xi[kg]

    def __eq__(self, other):
        if (self.d == other.d and self.siga == other.siga and
            self.sigs == other.sigs and self.nusigf == other.nusigf and
            self.xi == other.xi):
            return True
        else:
            return False

    def __mul__(self, val):
        # ここで val は float であることを前提とする
        xs = CrossSection()
        for kg in range(0,2):
            xs.d[kg] = self.d[kg] * val
            xs.siga[kg] = self.siga[kg] * val
            xs.sigs[kg] = self.sigs[kg] * val
            xs.nusigf[kg] = self.nusigf[kg] * val
            xs.xi[kg] = self.xi[kg] * val
        return xs

    def __add__(self, other):
        xs = CrossSection()
        for kg in range(0,2):
            xs.d[kg] = self.d[kg] + other.d[kg]
            xs.siga[kg] = self.siga[kg] + other.siga[kg]
            xs.sigs[kg] = self.sigs[kg] + other.sigs[kg]
            xs.nusigf[kg] = self.nusigf[kg] + other.nusigf[kg]
            xs.xi[kg] = self.xi[kg] + other.xi[kg]
        return xs
    
    def debug(self):
        print("-" * 10 + " XS " + "-" * 30)
        print("kg\tD\tSiga\tSigs\tnuSigf\tXi")
        for kg in range(0,2):
            print( )
            print(kg, self.d[kg], self.siga[kg], self.sigs[kg], self.nusigf[kg], self.xi[kg], sep='\t', end='\n')
        print("-"*44)


if __name__ == '__main__':
    xs = CrossSection()
    for kg in range(0,2):
        xs.set_d(kg, kg*10+1.0)
        xs.set_siga(kg, kg*10+2.0)
        xs.set_sigs(kg, kg*10+3.0)
        xs.set_nusigf(kg, kg*10+4.0)
        xs.set_xi(kg, kg*10+5.0)
    xs.debug()
    
    
    xs2 = xs * 2.0
    xs2.debug()

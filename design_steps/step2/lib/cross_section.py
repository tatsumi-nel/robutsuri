import numpy as np

class CrossSection:
    def __init__(self):
        self.d      = np.zeros(2)
        self.siga   = np.zeros(2)
        self.sigs   = np.zeros(2)
        self.nusigf = np.zeros(2)
        self.xi     = np.zeros(2)

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
    

    def debug(self):
        print("-" * 10 + " XS " + "-" * 30)
        print("kg\tD\tSiga\tSigs\tnuSigf\tXi")
        for kg in range(0,2):
            print( )
            print(kg, self.d[kg], self.siga[kg], self.sigs[kg], self.nusigf[kg], self.xi[kg], sep='\t', end='\n')
        print("-"*44)

if __name__ == '__main__':
    xs = CrossSection()
    xs.debug()

class CrossSection:
    def __init__(self):
        self.d      = [0.0, 0.0]
        self.siga   = [0.0, 0.0]
        self.nusigf = [0.0, 0.0]
        self.sigs   = [0.0, 0.0]
        self.xi     = [0.0, 0.0]

    def set_d(self, kg, val):
        self.d[kg] = val

    def set_siga(self, kg, val):
        self.siga[kg] = val

    def set_nusigf(self, kg, val):
        self.nusigf[kg] = val

    def set_xi(self, kg, val):
        self.xi[kg] = val

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

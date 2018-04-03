class CrossSection:
    def __init__(self):
        self.d = 0.0
        self.sigtr  = 0.0
        self.sigr   = 0.0
        self.nusigf = 0.0
        self.sigf   = 0.0
        # self.xi     = 1.0

    def set(self, vec):
        self.d      = vec[0]
        self.sigr   = vec[1]
        self.nusigf = vec[2]
        self.sigf   = vec[3]

    def set_d(self, val):
        self.d = val

    def set_sigr(self, val):
        self.sigr = val

    def set_nusigf(self, val):
        self.nusigf = val

    def set_sigf(self, val):
        self.sigf = val

    def get_d(self):
        return self.d
    
    def get_sigr(self):
        return self.sigr

    def get_nusigf(self):
        return self.nusigf
    
    def get_sigf(self):
        return self.sigf

    def get(self):
        dat = [self.d, self.sigr, self.nusigf, self.sigf]
        return dat

    def __add__(self, other):
        self.d = self.d + other.d
        self.sigr = self.sigr + other.sigr
        self.nusigf = self.nusigf + other.nusigf
        self.sigf = self.sigf + other.sigf
        return self

    def __sub__(self, other):
        self.d = self.d - other.d
        self.sigr = self.sigr - other.sigr
        self.nusigf = self.nusigf - other.nusigf
        self.sigf = self.sigf - other.sigf
        return self

    def __mul__(self, val):
        xs = CrossSection()
        xs.d = self.d * val
        xs.sigr = self.sigr * val
        xs.nusigf = self.nusigf * val
        xs.sigf = self.sigf * val
        return xs

    def __rmul__(self, val):
        return self.__mul__(val)

    def debug(self):
        print("--- XS ---------------")
        print("      D = ", self.d)
        print("  Sig_r = ", self.sigr)
        print("sig_pro = ", self.nusigf)
        print("  Sig_f = ", self.sigf)
        print("----------------------")

if __name__ == '__main__':
    xs = CrossSection()
    xs.debug()

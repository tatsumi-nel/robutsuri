class CrossSection:
    def __init__(self):
        self.d = 0.0
        self.sigtr  = 0.0
        self.sigr   = 0.0
        self.nusigf = 0.0
        self.sigf   = 0.0
        # self.xi     = 1.0

    def set_d(self, val):
        self.d = val

    def set_sigtr(self, val):
        self.sigtr = val

    def set_nusigf(self, val):
        self.nusigfs = val

    def set_sigf(self, val):
        self.sigf = val

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

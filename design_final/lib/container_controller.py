class ContainerController:
    """
    Container オブジェクトを操作し、外側反復計算を行う。
    """

    def __init__(self, container=None):
        self.container = container
        self.keff = 1.0
        self.keff_old = 1.0
        self.pro_old = 1.0
        self.conv_criterion = 1.0E-7
        self.max_outer_iterations = 2000
        self.inner_iterations = 1

    def calc(self):
        for idx_outer in range(self.max_outer_iterations):
            diff = self.calc_step()
            if(diff < self.conv_criterion):
                break


    def calc_step(self):
        for idx_inner in range(self.inner_iterations):
            for color in range(2): # (0:red, 1:black)
                self.container.calc(color)
            
        rr = self.container.reaction_rates()
        self.keff = rr.nusigf() / (self.pro_old/self.keff_old)
        diff = abs((self.keff - self.keff_old)/self.keff)

        self.keff_old = self.keff
        self.pro_old = rr.nusigf()

        self.container.set_keff(self.keff)

        return diff

    def get_keff(self):
        return self.keff

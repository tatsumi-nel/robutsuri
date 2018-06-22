class ContainerController:
    """
    Container オブジェクトを操作し、外側反復計算を行う。
    """

    def __init__(self, container=None):
        self.cont = container
        self.keff = 1.0
        self.keff_old = 1.0
        self.total_fis_src_old = 1.0
        self.conv_criterion = 1.0E-7
        self.max_outer_iterations = 100000
        self.inner_iterations = 4
        self.converged = False


    def calc(self):
        for idx_outer in range(self.max_outer_iterations):
            
            self.total_fis_src = self.cont.get_total_fis_src()
            norm_factor = 1.0 / (self.total_fis_src/self.keff)
            self.cont.normalize_fis_src(norm_factor)

            for idx_inner in range(self.inner_iterations):
                for color in range(2):
                    self.cont.calc(color)
                
            self.cont.calc_fis_src()
                
            self.total_fis_src = self.cont.get_total_fis_src()

            self.keff = self.total_fis_src / (self.total_fis_src_old/self.keff_old)
            diff = abs((self.keff - self.keff_old)/self.keff)

            #print(self.keff, diff)

            if(diff < self.conv_criterion):
                self.converged = True
                break

            self.keff_old = self.keff
            self.total_fis_src_old = self.total_fis_src

            self.cont.set_keff(self.keff)
        
        return (idx_outer, self.converged)


    def get_keff(self):
        return self.keff

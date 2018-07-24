import numpy as np

from node import *
from cross_section import *


class Container:
    def __init__(self, geometry, delta=1.0, albedo=0.0):
        self._setup(geometry, delta, albedo)

    def _setup(self, geometry, delta, albedo):
        self.nodes = []
        for r in geometry:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                self.nodes.append(the_node)

        self.delta = delta
        self.albedo = albedo
        self.ng = self.nodes[0].get_xs().ng()

    def get_ng(self):
        return self.ng


    def calc(self, kg, color):
        for ix in range(color, len(self.nodes), 2):
            if(ix==0):
                jin_xm = self.albedo * self.nodes[ix].get_jout(kg, XM)
            else:
                jin_xm = self.nodes[ix-1].get_jout(kg, XP)
                    
            if(ix==len(self.nodes)-1):
                jin_xp = self.albedo * self.nodes[ix].get_jout(kg, XP)
            else:
                jin_xp = self.nodes[ix+1].get_jout(kg, XM)

            self.nodes[ix].set_jin(kg, XM, jin_xm)
            self.nodes[ix].set_jin(kg, XP, jin_xp)
            self.nodes[ix].calc(kg)

    def calc_fis_src(self, kg):
        for the_node in self.nodes:
            the_node.calc_fis_src(kg)

    def calc_scat_src(self, kg):
        for the_node in self.nodes:
            the_node.calc_scat_src(kg)

    def get_total_fis_src(self):
        total_fis_src = 0.0
        for kg in range(self.ng):
            for the_node in self.nodes:
                total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()
        return total_fis_src

    def normalize_fis_src(self, factor):
        for kg in range(self.ng):
            for the_node in self.nodes:
                the_node.normalize_fis_src(kg, factor)

    def set_keff(self, keff):
        for the_node in self.nodes:
            the_node.set_keff(keff)            

    def get_flux_dist(self, kg):
        x_pos = []
        x_sum = 0.0
        flux = []
        for the_node in self.nodes:
            w = the_node.get_width()
            x_pos.append( x_sum + w/2 )        
            x_sum += w
            flux.append( the_node.get_flux(kg) )
        return [x_pos, flux]


    def debug(self):
        print("nodes: ", len(self.nodes))
        for the_node in self.nodes:
            the_node.debug()

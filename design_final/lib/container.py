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

    def calc(self, color=None):
        for ix in range(color, len(self.nodes), 2):
            if(ix==0):
                jin_xm = self.albedo * self.nodes[ix].get_jout(XM)
            else:
                jin_xm = self.nodes[ix-1].get_jout(XP)
                    
            if(ix==len(self.nodes)-1):
                jin_xp = self.albedo * self.nodes[ix].get_jout(XP)
            else:
                jin_xp = self.nodes[ix+1].get_jout(XM)

            self.nodes[ix].set_jin(XM, jin_xm)
            self.nodes[ix].set_jin(XP, jin_xp)
            self.nodes[ix].calc()


    def reaction_rates(self):
        rr = CrossSection()
        for the_node in self.nodes:
            rr = rr + the_node.get_xs() * the_node.get_flux() * the_node.get_width()
        return rr

    def set_keff(self, keff):
        for the_node in self.nodes:
            the_node.set_keff(keff)            

    def get_flux_dist(self):
        x_pos = []
        x_sum = 0.0
        flux = []
        for the_node in self.nodes:
            w = the_node.get_width()
            x_pos.append( x_sum + w/2 )            
            x_sum += w
            flux.append( the_node.get_flux() )
        return [x_pos, flux]


    def debug(self):
        print("nodes: ", len(self.nodes))
        for the_node in self.nodes:
            the_node.debug()

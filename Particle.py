import numpy as np

class Particle:

    def __init__(self, dim, v_max, v_min, edges, x0=None):
        self.v_max = v_max
        self.v_min = v_min
        self.x_min, self.x_max = edges#
        assert(len(self.x_min) == dim)
        #print("min xy (2d)", self.x_min, "max xy (2d)", self.x_max)
        self.dim = dim
        self.x = x0 if x0 is not None else np.array([ np.random.rand()*(self.x_max[d] - self.x_min[d]) + self.x_min[d] for d in range(self.dim)] ) 
        #print("X0= ", self.x)
        #self.v = np.array([ 0 for d in range(self.dim)] )
        self.v = np.array([ (np.random.rand()*((self.v_max - self.v_min)) + self.v_min) for d in range(self.dim)] )
        self.pbest = self.x
        self.gbest = self.x
        self.check_dimensions()
        
    def check_dimensions(self):
        assert(len(self.v) == self.dim)
        assert(len(self.x) == self.dim)

    def get_x(self):
        return self.x
    
    def get_v(self):
        return self.v

    def get_vmax(self):
        return self.v_max

    def get_vmin(self):
        return self.v_min

    def get_gbest(self):
        return self.gbest
    
    def get_pbest(self):
        return self.pbest

    def set_gbest(self, value):
        self.gbest = value
    
    def set_pbest(self, value):
        self.pbest = value

    def set_v(self, value):
        self.v = value
        self.v[self.v > self.v_max] = self.v_max
        self.v[self.v < self.v_min] = self.v_min
        
    def set_x(self, value):
        self.x = value
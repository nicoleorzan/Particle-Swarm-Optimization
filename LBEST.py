import Particle
import PSO as PSO
import numpy as np

class LBEST(PSO.PSO):

    def __init__(self, neighbors, n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max = 2.5, c_min = 0.5, x0=None):
        super().__init__(n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max, c_min, x0)
        self.neighbors = neighbors
        self.neighbors_indices = {}
        self.compute_nearest_neighbors()

    def compute_particle_gbest(self, p):
        for idx, l in enumerate(self.swarm):
            if idx in self.neighbors_indices[p]:
                if (self.func(l.get_pbest()) < self.func(p.get_gbest())):
                    p.set_gbest(l.get_pbest())
    
    def compute_nearest_neighbors(self):
        self.neighbors_indices = {}
        for i, l in enumerate(self.swarm):
            self.neighbors_indices[l] = [i-1, i, i+1]

    def loop(self, iterations):

        it = 0
        while it < iterations:
            for _, p in enumerate(self.swarm):
                
                #tmp = int(it/iterations*100)
                #self.neighbors = tmp if (tmp > 0 and tmp < len(self.swarm)/2) else self.neighbors
                #print(self.neighbors)
                #self.compute_nearest_neighbors()

                self.compute_particle_pbest(p)
                self.compute_particle_gbest(p)

                self.update_omega(iterations, it)
                self.update_c1_c2(it, iterations)
                
                self.update_velocity_lbest(p)
                self.update_position(p)

            self.X.append([p.get_x() for p in self.swarm])
            it +=1


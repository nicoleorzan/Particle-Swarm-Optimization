import Particle
import PSO as PSO
import numpy as np


class LBEST(PSO.PSO):

    def __init__(self, neighbors, n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max = 2.5, c_min = 0.5, x0=None):
        super().__init__(n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max, c_min, x0)
        self.neighbors = neighbors
        self.neighbors_indices = {}

    def compute_particle_gbest(self, p):
        for i, l in enumerate(self.swarm):
            if i in self.neighbors_indices[p]:
                if (self.func(l.get_pbest()) < self.func(p.get_gbest())):
                    p.set_gbest(l.get_pbest())
    
    def compute_nearest_neighbors(self, p):
        d = []
        for _, l in enumerate(self.swarm):
            d.append(np.sqrt(np.sum(np.square( p.get_x() - l.get_x() ))))
        idx = np.argpartition(np.array(d), self.neighbors*2)
        min_values = np.array(d)[idx[:self.neighbors*2+1]]
        indices = np.where(np.in1d(d, min_values))[0]
        self.neighbors_indices[p] = indices

    def loop(self, iterations):

        it = 0
        while it < iterations:
            for _, p in enumerate(self.swarm):

                self.compute_nearest_neighbors(p)
                self.compute_particle_pbest(p)
                self.compute_particle_gbest(p)

                self.update_velocity_lbest(p)
                self.update_position(p)

            self.X.append([p.get_x() for p in self.swarm])
            it +=1


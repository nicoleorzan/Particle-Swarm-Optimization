import Particle
import PSO as PSO
import numpy as np

class GBEST(PSO.PSO):
    def __init__(self, n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max = 2.5, c_min = 0.5, x0=None):
        super().__init__(n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max, c_min, x0)
        self.GBEST = self.swarm[0].get_x()

    def compute_gbest(self, p):
        if (self.func(p.get_pbest()) < self.func(self.GBEST)):
            self.GBEST = p.get_pbest()

    def loop(self, iterations):
        epsilon = 10**(-15)
        it = 0
        while it < iterations:
            for _, p in enumerate(self.swarm):

                self.compute_particle_pbest(p)
                self.compute_gbest(p)

                #self.update_c1_c2(it, iterations)
                #self.update_omega(iterations, it)
                
                self.update_velocity_gbest(p)
                self.update_position(p)

            self.X.append([p.get_x() for p in self.swarm])
            err = abs([0,0] - self.func(self.get_GBEST()))
            if (np.all(err< epsilon)):
                err = [0,0]
            self.error.append(err)

            it+=1


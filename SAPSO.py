import Particle
import PSO as PSO
import numpy as np

class SAPSO(PSO.PSO):
    def __init__(self, n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, T0 = 250, c_max = 2.5, c_min = 0.5, x0=None):
        super().__init__(n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max, c_min, x0)
        self.GBEST = self.swarm[0].get_x()
        self.T0 = T0
        self.v_max = v_max
        self.func = func

    def compute_gbest(self, p):
        if (self.func(p.get_pbest()) < self.func(self.GBEST)):
            self.GBEST = p.get_pbest()

    def compute_update_position(self, p):
        tmp = self.omega * p.get_v() + \
            self.c1 * np.random.uniform() * (p.get_pbest() - p.get_x()) + \
            self.c2 * np.random.uniform() * (self.GBEST - p.get_x())
        v_new = tmp if tmp.all() < self.v_max else self.v_max

        x_new = p.get_x() + v_new

        return x_new, v_new

    def loop(self, iterations):
        epsilon = 10**(-15)
        it = 0
        while it < iterations:

            T = self.T0 - self.T0*it/iterations  #iterations/(it+1)
            #print("T",T)
            #T = iterations/(it+1)
            #print(iterations/(it+1))
            for _, p in enumerate(self.swarm):

                self.compute_particle_pbest(p)
                self.compute_gbest(p)

                x_new, v_new = self.compute_update_position(p)
                if (self.func(x_new) < self.func(p.get_x())):
                    p.set_x(x_new)
                    p.set_v(v_new)
                else:
                    #print(x_new, np.exp(-(x_new - x)/T))
                    if (np.exp(-(x_new - p.get_x())/T).all() >= np.random.uniform()):
                        p.set_x(x_new)
                        p.set_v(v_new)
                #self.update_position(p)

            self.X.append([p.get_x() for p in self.swarm])
            err = abs([0,0] - self.func(self.get_GBEST()))
            if (np.all(err< epsilon)):
                err = [0,0]
            self.error.append(err)

            it+=1


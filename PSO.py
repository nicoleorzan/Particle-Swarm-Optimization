import Particle
import numpy as np

class PSO:
    def __init__(self, n_particles, dim, edges, v_max, v_min, omega, c1, c2, kappa, func, c_max = 2.5, c_min = 0.5, x0=None):
        self.S = n_particles
        self.dim = dim
        self.edges = edges
        self.v_max = v_max
        self.v_min = v_min
        self.omega = omega
        self.c1 = c1
        self.c2 = c2
        self.kappa = kappa
        self.phi = self.c1 + self.c2
        self.set_chi()
        self.func = func
        self.c_max = c_max
        self.c_min = c_min
        self.x0 = x0
        self.error = []
        self.omega_max = 20
        self.omega_min = 0.5

        if self.x0 != None:
            self.swarm = [Particle.Particle(self.dim, v_max = self.v_max, v_min = self.v_min, \
                                            edges = self.edges, x0 = self.x0[i]) for i in range(self.S)]
        else:
            self.swarm = [Particle.Particle(self.dim, v_max = self.v_max, v_min = self.v_min, \
                                            edges = self.edges, x0 = self.x0) for i in range(self.S)]
        self.X = [[p.get_x() for p in self.swarm]]
        self.GBEST = self.swarm[0].get_x()

    def set_chi(self):
        self.chi = np.sqrt(2 * self.kappa / (self.phi -2 + np.sqrt(self.phi**2 - 4*self.phi) ) ) if self.phi > 4 \
            else np.sqrt(self.kappa)

    def get_swarm(self):
        return self.swarm
    
    def get_X(self):
        return self.X

    def get_GBEST(self):
        return self.GBEST

    def get_error(self):
        return self.error

    def update_omega(self, iterations, it):
        self.omega = self.omega_max - it*(self.omega_max - self.omega_min)/iterations

    def update_c1_c2(self, t, iter_tot):
        self.c1 = (self.c_min - self.c_max) *t/iter_tot + self.c_max
        self.c2 = (self.c_max - self.c_min) *t/iter_tot + self.c_min

    def compute_particle_pbest(self, p):
        if (self.func(p.get_x()) < self.func(p.get_pbest()) ):
            p.set_pbest(p.get_x())

    def update_position(self, p):
        p.set_x(p.get_x() + p.get_v())

    def update_velocity_gbest(self, p):
        tmp = self.omega * p.get_v() + \
            self.c1 * np.random.uniform() * (p.get_pbest() - p.get_x()) + \
            self.c2 * np.random.uniform() * (self.GBEST - p.get_x()) # social component
        p.set_v(tmp) if tmp.all() < self.v_max else p.set_v(self.v_max)

    def update_velocity_gbest_evolved(self, p):
        p.set_v (self.chi * ( p.get_v() + self.c1 * np.random.uniform() * (p.get_pbest() - p.get_x()) + \
        self.c2 * np.random.uniform() * (self.GBEST - p.get_x()) ) )

    def update_velocity_lbest(self, p):
        tmp = self.omega * p.get_v() + \
            self.c1 * np.random.uniform() * (p.get_pbest() - p.get_x()) + \
            self.c2 * np.random.uniform() * (p.get_gbest() - p.get_x())
        p.set_v(tmp) if tmp.all() < self.v_max else p.set_v(self.v_max)

    def update_velocity_lbest_evolved(self, p):
        p.set_v(self.chi * ( p.get_v() + self.c1 * np.random.uniform() * (p.get_pbest() - p.get_x()) + \
        self.c2 * np.random.uniform() * (p.get_gbest() - p.get_x()) ) )

    def two_dim_positions(self):

        two_dim_particle_positions = []
        for i in self.X:
            tmp = []
            for j in range(len(i)):
                tmp.append([i[j][0], i[j][1]])
            two_dim_particle_positions.append(tmp)

        return two_dim_particle_positions

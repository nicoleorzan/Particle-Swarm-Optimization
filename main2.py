import LBEST
import Anim2 as Anim
import numpy as np
import functions

dim = 2
parts = 7
edge = 100
f = functions.f

np.random.seed(123)
pso = LBEST.LBEST(neighbors = 1, n_particles = parts, dim = dim, edges = (np.array([-edge, -edge]), np.array([edge, edge])),\
     v_max = 4, v_min = -4, omega = 0.5, c1 = 2.05, c2 = 2.05, kappa = 0.7, func = f)
swarm = pso.get_swarm()
pso.loop(50)

pos = pso.two_dim_positions()
ani = Anim.Anim(pos, func = f, edge = edge)
ani.show_plot()
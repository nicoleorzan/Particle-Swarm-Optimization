import LBEST
import Anim as Anim
import numpy as np
import functions

def init(edge, step):
     x0 = []
     for i in range(-(edge-2-int(step/2)), edge-2, step):
          for j in range(-(edge-2-int(step/2)), edge-2, step):
               x0.append(np.array([i,j]))
     parts = len(x0)

     return parts, x0

dim = 2
parts = 26
edge = 200
f = functions.gaus_bi
parts, x0 = init(edge=edge, step=int(edge/2))

c = 2.05
#omega = 0.5*(2*c)-1
np.random.seed(123)
pso = LBEST.LBEST(neighbors = 1, n_particles = parts, dim = dim, edges = (np.array([-edge, -edge]), np.array([edge, edge])),\
     v_max = 4, v_min = -4, omega = 0.5, c1 = c, c2 = c, kappa = 1, func = f, x0=x0)
swarm = pso.get_swarm()
pso.loop(100)

pos = pso.two_dim_positions()
ani = Anim.Anim(pos, func = f, edge = edge)
ani.show_plot()
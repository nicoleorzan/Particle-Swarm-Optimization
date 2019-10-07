import SAPSO
import Anim as Anim
import functions
import numpy as np
import matplotlib.pyplot as plt

def init(edge, step):
     x0 = []
     for i in range(-(edge-2-int(step/2)), edge-2, step):
          for j in range(-(edge-2-int(step/2)), edge-2, step):
               x0.append(np.array([i,j]))
     parts = len(x0)

     return parts, x0

def error_plot(error):
     x_err = []
     y_err = []
     for _, err in enumerate(error):
          x_err.append(err[0])
          y_err.append(err[1])
     plt.plot(x_err)
     plt.yscale('log')
     plt.ylim([10**(-15),y_err[0]])
     plt.show()

dim = 2
parts = 13
edge = 200
f = functions.gaus_bi

np.random.seed(123)
pso = SAPSO.SAPSO(n_particles = parts, dim = dim, edges = (np.array([-edge, -edge]), np.array([edge, edge])),\
     v_max = 4, v_min = -4, omega = 0.5, c1 = 2.05, c2 = 2.05, kappa = 0.7, func = f, x0=None)

pso.loop(100)
pos = pso.two_dim_positions()
error = pso.get_error()
#print(error[-1])
#error_plot(error)

ani = Anim.Anim(pos, func = f, edge = edge)
ani.show_plot()

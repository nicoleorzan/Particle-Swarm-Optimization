import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

class Anim:

    def __init__(self, positions, func, edge):
        self.func = func
        self.edge = edge
        self.x = []
        self.y = []
        for i in positions[1]:
            self.x.append(i[0])
            self.y.append(i[1])

        self.positions = positions
        self.fig = plt.figure()

    def update_plot(self, i, fig, scat):
        scat.set_offsets((self.positions[i]))
        self.t1.set_text(i)
        if (i>0 & i<1): self.anim.event_source.interval = 170
        return scat

    def show_plot(self):

        x = np.linspace(-self.edge, self.edge, self.edge)
        y = np.linspace(-self.edge, self.edge, self.edge)
        fun_map = np.empty((x.size, y.size))
        for i in range(x.size):
            for j in range(y.size):
                fun_map[i,j] = self.func([y[j], x[i]]) #([x[i], y[j]])

        s = self.fig.add_subplot(1, 1, 1, xlabel='$x$', ylabel='$y$')
        im = s.imshow(
            fun_map,
            extent=(x[0], x[-1], y[0], y[-1]),
            origin='lower',
            alpha=0.8)
        self.fig.colorbar(im)

        scat = plt.scatter(self.x, self.y, c = self.x, edgecolors='black', linewidth = 0.4)
        plt.grid(True, linestyle = '-', color = 'black', linewidth=0.4, alpha = 0.8)
        self.t1 = plt.text(x=self.edge, y=self.edge+0.7, s = 0, fontsize=19)
        plt.text(x =-self.edge, y = self.edge+0.7, s = str(len(self.x)) + " Particles", fontsize=13)
        self.anim = animation.FuncAnimation(self.fig, self.update_plot, fargs = (self.fig, scat),
                                       frames = len(self.positions), interval = 700, repeat=False) 

        #plt.show(self.anim)
        #self.anim.save(str(time.time())+'gaus.gif', writer='imagemagick', fps=5)
        self.anim.save('SAPSO_omega_changing_ordered_gaus.gif', writer='imagemagick', fps=5)
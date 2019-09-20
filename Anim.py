import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Anim:

    def __init__(self, positions):
        self.x = []
        self.y = []
        for i in positions[1]:
            self.x.append(i[0])
            self.y.append(i[1])

        self.positions = positions
        self.fig = plt.figure()

    def update_plot(self, i, fig, scat):
        scat.set_offsets((self.positions[i]))
        return scat

    def show_plot(self):

        ax = self.fig.add_subplot(111)
        ax.grid(True, linestyle = '-', color = '0.75')
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])

        scat = plt.scatter(self.x, self.y, c = self.x, cmap = "hsv")
        scat.set_alpha(0.8)
        anim = animation.FuncAnimation(self.fig, self.update_plot, fargs = (self.fig, scat),
                                       frames = len(self.positions), interval = 150) 

        plt.show(anim)
        #anim.save('animation.gif', writer='imagemagick', fps=5)
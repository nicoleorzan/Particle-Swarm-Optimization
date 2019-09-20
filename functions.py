import numpy as np

def parabola(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total

def noise(x):
    total = np.random.normal(0, 1, 1)
    #print(total)
    for i in range(len(x)):
        total+=x[i]**2
    return total

def gaussian_bimodal(x, x0 = -40, y0 = -40, x1 = 50, y1 = 50, sx = 4, sy = 5, rho = 0.3):
    x0 = 60
    x1 = 70
    y0 = 70
    y1 = 20
    rho = 0
    s1 = 2
    s2 = 2
    Qsquared = 1/(1-rho**2) * ( (x[0]-x0)**2/(s1**2) - 2*rho*(x[0]-x0)*(x[1]-y0)/(s1*s2) + (x[1]-y0)**2/(s2**2) )
    f = 1/(2*np.pi*s1*s2*np.sqrt(1-rho**2)) * np.exp(-Qsquared/2)
    return -f
    #Qsquared = 1/(1-rho**2) * ( (x[0]-x0)**2/(sx**2) - 2*rho*(x[0]-x0)*(x[1]-y0)/(sx*sy) + (x[1]-y0)**2/(sy**2) )
    #return 1/(2*np.pi*sx*sy*np.sqrt(1-rho**2)) * np.exp(-Qsquared/2)

def f(x):
    x0 = 50
    x1 = -20
    y0 = 50
    y1 = -20
    #rho = 0
    s1 = 10
    s2 = 12
    return ( 2* (1/(2*np.pi*s1*s2)) * np.exp( - (x[0]-x0)**2/(2*s1**2) - (x[1]-y0)**2/(2*s2**2)) + \
         (1/(2*np.pi*2*s1*s2)) * np.exp( - (x[0]-x1**2/(2*s1**2) - (x[1]-y1)**2/(2*s2**2))))

def rastrigin(x):
    n = len(x)
    A = 10
    total = A*n
    for i in range(len(x)):
        total += (x[i]**2 - A*np.cos(2-np.pi*x[i]))
    return total


"""
def func_2d(x):
    #Qsquared = 1/(1-rho**2) * ( (x-x0)**2/(s1**2) - 2*rho*(x-x0)*(y-y0)/(s1*s2) + (y-y0)**2/(s2**2) )
    #f = 1/(2*np.pi*s1*s2*np.sqrt(1-rho**2)) * np.exp(-Qsquared/2)
    return -  ( 2* (1/(2*np.pi*s1*s2)) * np.exp( - (x[0]-x0)**2/(2*s1**2) - (x[1]-y0)**2/(2*s2**2)) + \
         (1/(2*np.pi*2*s1*s2)) * np.exp( - (x[0]-(-70))**2/(2*s1**2) - (x[1]-(-30))**2/(2*s2**2))+\
         (1/(2*np.pi*s1*s2)) * np.exp( - (x[0]-60)**2/(2*s1**2) - (x[1]-10)**2/(2*s2**2))+\
         (1/(2*np.pi*6*s1*s2)) * np.exp( - (x[0]-45)**2/(2*s1**2) - (x[1]-70)**2/(2*s2**2)))
"""
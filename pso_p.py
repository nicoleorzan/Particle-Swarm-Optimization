import GBEST
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)



n_particles = 80
a_min = -1
a_max = 1
x_max = a_max
x_min = a_min
v_min = -0.07 #-0.1*(x_max - x_min)
v_max = 0.07 #0.1*(x_max - x_min)
dim = 100
T = dim


itera = 150
w = 0.7298
c1 = 1.49618
c2 = 1.49618
s0 = (-np.pi/6, 0.0)
q = 0.05
gamma = q**(1/(dim-1))

def landscape(S):
    f = np.sin(3*S)
    return f

def update_system_state(S, a):
    pos, vel = S
    vel = vel + 0.001*a - 0.0025*np.cos(3*pos)
    pos = pos + vel
    S = (pos, vel)
    return S

def real_system(S, a):
    S = update_system_state(S, a)
    pos, _ = S
    R = np.sin(3*pos)-1
    return S, R

def update_particle_velocity(v, x, y_pbest, y_gbest):
    v = w*v + c1*np.random.uniform()*(y_pbest - x) + c2*np.random.uniform()*(y_gbest - x)
    #print("v update,  ", v)
    if v.all() > v_max: v = v_max
    elif v.all() < v_min: v = v_min
    return v

def update_particle_position(x, v):
    x = x + v
    #print("x update,  ", x)
    """if (x.all() < 0.3 and x.all() > -0.3):
        x = 0
    elif (x.all() > 0.3):
        x = 1
    elif (x.all() < -0.3):
        x = -1"""
    if x.all() > x_max: x = x_max
    elif x.all() < x_min: x = x_min
    return x

def model_system(S, a):
    S = update_system_state(S, a)
    pos, _  = S
    R = np.sin(3*pos)-1
    return S, R

def model_based_computation(S, x):
    R = 0
    s = S
    k = 0
    while k < dim:
        a = x[k]
        s, r = model_system(s,a) # stato = pos e velocita
        R = R + gamma**k * r
        k = k + 1
    return R

def PSO_P(S, P):
    X = np.array([np.random.random_integers(x_min, x_max, dim) for p in range(n_particles)])
    V = np.array([[np.random.rand()*(v_max - v_min) + v_min for d in range(dim)] for p in range(n_particles)])
    #print("X[0]=",X[0])
    #print("V[0]=",V[0])
    Pbest = X
    #Gbest = X
    Gbest = X[0]
    #print("Gbest= ",Gbest)

    for i in range(0, n_particles):
        p = 0
        #print("particle ", i)
        while p < P:
            #print("X[i]", X[i])
            if model_based_computation(S, X[i]) > model_based_computation(S, Pbest[i]):
                Pbest[i] = X[i]
            #print("Pbest[", i, "]=", Pbest[i])

            #compute_particle_Gbest(S, i, Pbest, Gbest)
            if model_based_computation(S, Pbest[i]) > model_based_computation(S, Gbest):
                Gbest = Pbest[i]
            #print("Gbest", Gbest)

            V[i] = update_particle_velocity(V[i], X[i], Pbest[i], Gbest)
            X[i] = update_particle_position(X[i], V[i])
            p = p + 1   
    #print("final Gbest",Gbest ) 
    return Gbest

def compute_particle_Gbest(S, i, Pbest, Gbest):
    for j in range(-i, i):
        if model_based_computation(S, Pbest[j]) >  model_based_computation(S, Gbest[i]):
            Gbest[i] = Pbest[j]
    
    
def policy(s0, iterations):
    reached = 0
    states = []
    s = s0
    f = open("file3.txt", "w") 
    f.write("t        x       y \n")
    print(s0, "\n starting iterations:")
    for i in range(1, iterations):
        print("it = ", i)
        best_sequence = PSO_P(s, i)
        #print("selecting a= ")
        a = best_sequence[0]
        #print(a)
        s, r = real_system(s, a)
        pos, _ =s
        f.write(str(i) + "   " + str(pos) + "   " + str(landscape(pos)) + "\n")
        if (pos >= np.pi/6):
            reached = 1
            print("reached", reached)
            break
        #print(pos)
        states.append(pos)
    
    f.close()
    return states, s, r


states, s, r = policy(s0, itera)
#print("states", states)
landscape_v = np.vectorize(landscape)
#print("landscape",landscape_v(states))
plt.plot(states, landscape_v(states))
plt.savefig('foo.png')
plt.show()
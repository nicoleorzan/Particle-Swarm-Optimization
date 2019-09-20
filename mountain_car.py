import GBEST
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

def reward(rho):
    #reward = 0
    #if (rho >= 0.5): reward = 1
    #return reward
    if (rho >= np.pi/6):
        return 1
    return np.sin(3*rho)-1

actions = [-1, 0, 1]

rho0 = np.random.uniform(-0.6, -0.4) #-np.pi/6
rho = rho0
rho_prim0 = 0.
rho_prim = rho_prim0
print(rho, rho_prim)
edge = np.pi
rho_finale = np.pi/6
state = (rho, rho_prim)
parts = 4
dim = 1

def rho_update(rho_old, rho_prim):
    x = rho_old + rho_prim
    if (x < -1.2): x = -1.2
    if (x > 0.5): x = 0.5
    return x

def rho_prim_update(rho, rho_prim, action):
    v = rho_prim + 0.001*action - 0.0025*np.cos(3*rho)
    if (rho == -1.2): v = 0
    if (v < -0.07): v = -0.07
    if (v > 0.07): v = 0.07
    return v

def landscape(rho):
    return np.sin(3*rho)

N_particles = 100
N_actions_sequence = 200

particles_positions = []
for i in range(N_particles):
    particles_positions.append(np.random.random_integers(-1, 1, N_actions_sequence ))


pbest = []
gbest = None
rho = rho0
rho_prim = rho_prim0

for j in range(0,N_particles):
    rew_tmp = 0
    rho_tmp = rho
    rho_prim_tmp = rho_prim

    for i in range(0,N_actions_sequence):
        action = particles_positions[j][i]
        rho_tmp = rho_update(rho_tmp, rho_prim)
        rho_prim_tmp = rho_prim_update(rho_tmp, rho_prim_tmp, action)
        rew_tmp = rew_tmp + reward(rho_tmp)
        
    print("reward of particle ", j, ": ", rew)
    if gbest == None:
        gbest = rew_tmp
        best_actions = particles_positions[j]
    else:
        if gbest < rew_tmp:
            gbest = rew_tmp
            best_actions = particles_positions[j]
    print("gbest ",gbest)
    
    next_action = best_actions[0]
    rho = rho_update(rho, rho_prim)
    rho_prim = rho_prim_update(rho, rho_prim, next_action)
    rew = reward(rho)

    #v_particle = 
        #pso.loop(20)
        #pos = pso.get_X() # found action sequance
        #print(pos[0])

        #apply action sequence and find next state (rho1, rho_prim1)
        #rho, rho_prim = (rho1, rho_prim1)


#plt.plot(np.linspace(0, N_actions_sequence, N_actions_sequence), rhos)
#plt.show()
from euler_cromer import simulate
import numpy as np
from matplotlib import pyplot as plt

k = 0.5 # fjäderkonstant
r = 1   # dämpningskonstant
m = 1

def undamped(p, v, t):
    return (-k*p) / m
def damped(p, v, t):
    return (-k*p - r*v) / m
def driven_damped(p, v, t):
    def F(t):
        F0 = 0.1
        w = np.sqrt(k/m)
        return F0 * np.sin(w*t)
    return (-k*p - r*v - F(t)) / m

y0, v0 = 0, -10
initial = [y0, v0]
dt, max_time = 0.001, 30
pos, vel, acc = simulate(undamped, initial, dt, max_time, title='Odämpad svängning')
simulate(damped, initial, dt, max_time, title='Dämpad svängning')
simulate(driven_damped, initial, dt, max_time, title='Påtvingad svängning')

# Extrauppgift
pos, vel = np.array(pos), np.array(vel)
E_tot = 0.5*m*vel**2 + 0.5*k*pos**2

time = np.arange(0, max_time, dt)
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True, constrained_layout=True)
ax1.plot(time, E_tot)
ax1.set_title('E_tot')
ax1.set_xlabel('tid [s]')
ax2.plot(time, pos)
ax2.set_title('delta_y')
ax2.set_xlabel('tid [s]')
plt.show()
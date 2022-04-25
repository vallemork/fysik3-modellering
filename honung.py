from euler_cromer import simulate
from matplotlib import pyplot as plt
import numpy as np

m = 0.5
g = 9.82
rho = 2000 # honung densitet
r = 0.05   # radie
V = (4/3)*np.pi * r**3
b = 50 * r # dämpningskonstant

def f(y, v, t):
    # negativ riktning neråt, honungen är vid y <= 0
    h = np.clip(r-y, 0, 2*r)
    V_under_surface = (1/3)*np.pi * h**2 * (3*r - h)
    F_lyft = rho * V_under_surface * g
    F_d = b*-v * (r-y > 0) # dämpande kraft finns bara när kulan är i honungen
    F_g = -m*g
    return (F_g + F_lyft + F_d) / m

y0, v0 = 0, 3
simulate(f, [y0, v0], dt=0.001, to_time=10)
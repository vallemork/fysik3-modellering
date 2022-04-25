from euler_cromer import simulate
from matplotlib import pyplot as plt
import numpy as np

# Det som kastas
human = {'m': 70, 'C_d': 1.2, 'A': np.pi*0.35**2}
ball = {'m': 0.5, 'C_d': 0.47, 'A': np.pi*0.1**2}
bullet = {'m': 0.02, 'C_d': 0.295, 'A': np.pi*0.01**2}

thing = bullet

# Konstanter
m = thing['m'] # massa
C_d = thing['C_d'] # luftmotsåndskoefficient
A = thing['A'] # area
rho = 1.2  # luftens densitet
g = 9.82  # gravitation
k_d = 0.5 * C_d * rho * A

# Begynnelsevilkor
alpha = np.radians(35)
speed = 40
v0 = [speed*np.cos(alpha), speed*np.sin(alpha)]
y0 = [2, 0]
initial = [y0, v0]

dt, max_time = 0.01, 15

# Acceleration
def f_drag(y, v, t):
    speed = np.linalg.norm(v) # fart |v|
    Fd = -v * k_d * speed # riktning: -v, magnitud: k_d*|v|^2
    Fg = np.array([0, -m*g]) # gravitationskraft
    return (Fd + Fg) / m
def f_no_drag(y, v, t):
    return np.array([0, -g])

# simulate(f_drag, initial, dt, max_time, title='Människa, 500m fall')

# simulate(f_no_drag, initial, dt, max_time, title='Pistolkula, inget luftmotstånd')

# def freefall_solution(t):
#     # från https://en.wikipedia.org/wiki/Free_fall
#     vel_terminal = np.sqrt((2*m*g) / (rho*C_d*A))
#     y = y0[1] - (vel_terminal**2 / g) * \
#              np.log(np.cosh((g*res['t'])/vel_terminal))
#     return y

# res = simulate(f_drag, initial, dt, max_time, plot=False)
# y_true = freefall_solution(res['t'])
# plt.plot(res['t'], res['y'], label='model')
# plt.plot(res['t'], y_true, label="solution")
# plt.legend()
# plt.show()

for dt in [5, 1, 0.1, 0.01, 0.001]:
    res = simulate(f_no_drag, initial, dt, to_time=10, plot=False)
    print(res['t'][0], res['t'][-1])
    plt.plot(res['x'], res['y'], label=f'dt={dt}')
plt.title('y(x) för olika dt, utan luftmotstånd')
plt.legend()
plt.show()
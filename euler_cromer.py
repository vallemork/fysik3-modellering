import numpy as np
from matplotlib import pyplot as plt
from utils.colorline import colorline

def simulate(f, initial, dt=0.01, from_time=0, to_time=5, plot=True, title=''):
    '''
    Löser en 2:a ordningens differentialekvation med Euler-cromer metoden 
    och plottar resultatet.

    f: f(y, y', t) = y''
    initial: [y_0, y'_0]
    '''
    y, y_prime = map(np.array, initial.copy())
    ys, y_primes, y_2primes = [y],[y_prime],[f(y, y_prime, from_time)]
    time = np.arange(from_time, to_time, dt)
    # euler-cromer
    for t in time[1:]:
        y_2prime = f(y, y_prime, t)
        y_prime = y_prime + y_2prime*dt
        y = y + y_prime*dt
        ys.append(y); y_primes.append(y_prime); y_2primes.append(y_2prime)

    mode = '2D' if type(initial[0]) in (list, np.array) else '1D' # ifall rörelsen är tvådimensionell
    if plot:
        plt.style.use('seaborn-darkgrid')
        fig = plt.figure(constrained_layout=True, figsize=(6, 6))
        fig.suptitle(title)
        if mode == '2D':
            plots = fig.subplot_mosaic([['pt', 'p'], ['v', 'a']])
            speed = np.linalg.norm(y_primes, axis=1)
            a_speed = np.linalg.norm(y_2primes, axis=1)
        else: 
            plots = fig.subplot_mosaic([['pt', 'pv'], ['v', 'a']])
            speed, a_speed = y_primes, y_2primes
        
        plots['a'].set_title("y''(t) (acceleration)")
        plots['a'].set_xlabel("tid [s]")
        plots['pt'].set_title("y(t) (position)")
        plots['pt'].set_xlabel("tid [s]")
        plots['pt'].axhline(0, color='k', linestyle='--')
        plots['v'].set_title("y'(t) (hastighet)")
        plots['v'].set_xlabel("tid [s]")

        if mode == '2D':
            plots['p'].set_title('y(x)')
            plots['p'].plot(*np.array(ys).T)
            plots['p'].axhline(0, color='k', linestyle='--')
            plots['p'].set_xlabel('x')
            plots['p'].set_ylabel('y')

            plots['a'].plot(time, y_2primes, label=['ax', 'ay'])
            plots['a'].plot(time, a_speed, label='|a|')
            plots['a'].legend()
            plots['pt'].plot(time, ys, label=['px', 'py'])
            plots['pt'].legend()
            plots['v'].plot(time, y_primes, label=['vx', 'vy'])
            plots['v'].plot(time, speed, label='|v|')
            plots['v'].legend()
        else:
            plots['pv'].set_title("y(y')")
            plots['pv'].set_xlabel('y(t)')
            plots['pv'].set_ylabel("y'(t)")
            colorline(x=ys, y=y_primes, z=time, ax=plots['pv'], norm=None, cmap='copper')
            plots['pv'].scatter(ys[0], y_primes[0], color='r', alpha=0.5)

            plots['a'].plot(time, a_speed)
            plots['pt'].plot(time, ys)
            plots['v'].plot(time, y_primes)
        
        # extra info
        py = np.array(ys)[:,1] if mode == '2D' else np.array(ys)
        speed = np.array(speed)
        print(title)
        print(f'maxhöjd: {np.max(py):.3f}m efter {time[np.argmax(py)]:.3f}s')
        if len(py[py<0]):
            print(f'tid till y=0: {time[np.where(py<0)[0][0]]:.3f}s')
        print(f'maxfart: {np.max(speed):.3f}m/s efter {time[np.argmax(speed)]:.3f}s')
        print(f'sista fart: {speed[-1]:.3f}m/s')
        print('\n')
        plt.show()

    return {
        'x': np.array(ys)[:, 0] if mode == '2D' else None,
        'y': np.array(ys)[:, 1] if mode == '2D' else np.array(ys),
        'y_prime': np.array(y_primes),
        'y_2prime': np.array(y_2primes),
        't': np.array(time)
    }
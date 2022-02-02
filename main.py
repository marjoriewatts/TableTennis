import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from classes import TableTennis


def main():
    new = TableTennis("1", 0.0027, 0.04, 4)  # New ball

    
    # solving the ODE to find velocity
    t = np.linspace(0, 10, 1000)


    vx_new = odeint(new.x_acceleration, new.xspeed, t)
    vy_new = odeint(new.y_acceleration, new.yspeed, t)


    plt.subplot(1, 2, 1)
    plt.title(f'Velocity of {new.version} in x')
    plt.plot(t, vx_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(1, 2, 2)
    plt.title(f'Velocity of {new.version} in y')
    plt.plot(t, vy_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

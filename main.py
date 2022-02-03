import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from classes import TableTennis


def main():
    new = TableTennis("NEW", 0.0027, 0.04, 4, 30)  # New ball
    old = TableTennis("OLD", 0.0027, 0.038, 4, 30)  # Old ball

    # solving the ODE to find velocity
    t = np.linspace(0, 10, 1000)

    vx_new = odeint(new.x_acceleration, new.xspeed, t)
    vy_new = odeint(new.y_acceleration, new.yspeed, t)

    vx_old = odeint(old.x_acceleration, old.xspeed, t)
    vy_old = odeint(old.y_acceleration, old.yspeed, t)

    plt.subplot(2, 2, 1)
    plt.title(f'Velocity of {new.version} in x')
    plt.plot(t, vx_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Velocity of {new.version} in y')
    plt.plot(t, vy_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Velocity of {old.version} in x')
    plt.plot(t, vx_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Velocity of {old.version} in y')
    plt.plot(t, vy_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

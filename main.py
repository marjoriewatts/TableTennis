import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from velocity import TableTennis
from position import Position


def main():
    new_vel = TableTennis("NEW", 0.0027, 0.04, 4, 0)  # New ball
    old_vel = TableTennis("OLD", 0.0027, 0.038, 4, 0)  # Old ball

    # solving the ODE to find velocity -----------------------------------------------------------------
    t = np.linspace(0, 10, 1000)

    vx_new = odeint(new_vel.x_acceleration, new_vel.x_speed, t)
    vy_new = odeint(new_vel.y_acceleration, new_vel.y_speed, t)

    vx_old = odeint(old_vel.x_acceleration, old_vel.x_speed, t)
    vy_old = odeint(old_vel.y_acceleration, old_vel.y_speed, t)

    plt.subplot(2, 2, 1)
    plt.title(f'Velocity of {new_vel.version} version in x direction')
    plt.plot(t, vx_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Velocity of {new_vel.version} version in y direction')
    plt.plot(t, vy_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Velocity of {old_vel.version} version in x direction')
    plt.plot(t, vx_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Velocity of {old_vel.version} version in y direction')
    plt.plot(t, vy_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()

    # solving the ODE to find position -----------------------------------------------------------------
    new_pos = Position("NEW", 0.0027, 0.04, 4, 0)  # New ball
    old_pos = Position("OLD", 0.0027, 0.038, 4, 0)  # Old ball

    ts = np.linspace(1, 10, 200)

    x0 = [0, 4]
    y0 = [0, 0]

    x_new = odeint(new_pos.x_acceleration, x0, ts)
    xs_new = x_new[:, 0]
    y_new = odeint(new_pos.y_acceleration, y0, ts)
    ys_new = y_new[:, 0]

    x_old = odeint(old_pos.x_acceleration, x0, ts)
    xs_old = x_new[:, 0]
    y_old = odeint(old_pos.y_acceleration, y0, ts)
    ys_old = y_new[:, 0]

    plt.subplot(2, 2, 1)
    plt.title(f'Position of {new_pos.version} version in x direction')
    plt.plot(ts, xs_new, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')

    plt.subplot(2, 2, 2)
    plt.title(f'Position of {new_pos.version} version in x direction')
    plt.plot(ts, ys_new, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')

    plt.subplot(2, 2, 3)
    plt.title(f'Position of {old_pos.version} version in x direction')
    plt.plot(ts, xs_old, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')

    plt.subplot(2, 2, 4)
    plt.title(f'Position of {old_pos.version} version in x direction')
    plt.plot(ts, ys_old, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

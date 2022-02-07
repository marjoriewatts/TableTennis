import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from velocity import TableTennis
from position import Position


def main():
    # Solving the ODE for position and velocity
    new_pos = Position("NEW", 0.0027, 0.04, 4, 0)  # New ball
    old_pos = Position("OLD", 0.0027, 0.038, 4, 0)  # Old ball

    t = np.linspace(1, 10, 200)

    x0 = [0, 4]
    y0 = [0, 0]  # Initial x and y conditions in the form [position, velocity]

    x_new = odeint(new_pos.x_acceleration, x0, t)
    xs_new = x_new[:, 0]  # x position
    vx_new = x_new[:, 1]  # x velocity
    y_new = odeint(new_pos.y_acceleration, y0, t)
    ys_new = y_new[:, 0]  # y position
    vy_new = y_new[:, 1]  # y velocity

    x_old = odeint(old_pos.x_acceleration, x0, t)
    xs_old = x_old[:, 0]
    vx_old = x_old[:, 1]
    y_old = odeint(old_pos.y_acceleration, y0, t)
    ys_old = y_old[:, 0]
    vy_old = y_old[:, 1]

    # Plotting velocity ------------------------------------------------------------------------------------------------
    plt.subplot(2, 2, 1)
    plt.title(f'Velocity of {new_pos.version} version in x direction')
    plt.plot(t, vx_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Velocity of {new_pos.version} version in y direction')
    plt.plot(t, vy_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Velocity of {old_pos.version} version in x direction')
    plt.plot(t, vx_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Velocity of {old_pos.version} version in y direction')
    plt.plot(t, vy_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()

    # Plotting position ------------------------------------------------------------------------------------------------
    plt.subplot(2, 2, 1)
    plt.title(f'Position of {new_pos.version} version in x direction')
    plt.plot(t, xs_new, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Position of {new_pos.version} version in y direction')
    plt.plot(t, ys_new, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Position of {old_pos.version} version in x direction')
    plt.plot(t, xs_old, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Position of {old_pos.version} version in y direction')
    plt.plot(t, ys_old, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()

    # Plotting x position against y position --------------------------------------------------------------------------

    plt.subplot(2, 1, 1)
    plt.title(f'Position of {new_pos.version} version')
    plt.plot(xs_new, ys_new, 'r')
    plt.ylabel('y position')
    plt.xlabel('x position')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 1, 2)
    plt.title(f'Position of {old_pos.version} version')
    plt.plot(xs_old, ys_old, 'r')
    plt.ylabel('y position')
    plt.xlabel('x position')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

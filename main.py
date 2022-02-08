import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

from classes import TableTennis


def main():
    # Solving the ODE for position and velocity
    NEW = TableTennis("NEW", 0.0029, 0.04)  # New ball
    OLD = TableTennis("OLD", 0.0027, 0.038)  # Old ball

    t = np.linspace(1, 10, 200)

    initial_state = [0, 0, 4, 0]

    new_sols = odeint(NEW.system, initial_state, t)
    xs_new = new_sols[:, 0]
    ys_new = new_sols[:, 1]
    vx_new = new_sols[:, 2]
    vy_new = new_sols[:, 3]

    old_sols = odeint(OLD.system, initial_state, t)
    xs_old = old_sols[:, 0]
    ys_old = old_sols[:, 1]
    vx_old = old_sols[:, 2]
    vy_old = old_sols[:, 3]

    # Plotting velocity ------------------------------------------------------------------------------------------------
    plt.subplot(2, 2, 1)
    plt.title(f'Velocity of {NEW.version} version in x direction')
    plt.plot(t, vx_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Velocity of {NEW.version} version in y direction')
    plt.plot(t, vy_new)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Velocity of {OLD.version} version in x direction')
    plt.plot(t, vx_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Velocity of {OLD.version} version in y direction')
    plt.plot(t, vy_old)
    plt.xlabel('Time $t$ [s]')
    plt.ylabel('Velocity $v$ [mph]')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()

    # Plotting position ------------------------------------------------------------------------------------------------
    plt.subplot(2, 2, 1)
    plt.title(f'Position of {NEW.version} version in x direction')
    plt.plot(t, xs_new, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 2)
    plt.title(f'Position of {NEW.version} version in y direction')
    plt.plot(t, ys_new, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 3)
    plt.title(f'Position of {OLD.version} version in x direction')
    plt.plot(t, xs_old, 'r')
    plt.ylabel('x position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 2, 4)
    plt.title(f'Position of {OLD.version} version in y direction')
    plt.plot(t, ys_old, 'r')
    plt.ylabel('y position')
    plt.xlabel('time')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()

    # Plotting x position against y position --------------------------------------------------------------------------

    plt.subplot(2, 1, 1)
    plt.title(f'Position of {NEW.version} version')
    plt.plot(xs_new, ys_new, 'r')
    plt.ylabel('y position')
    plt.xlabel('x position')
    plt.grid(True, linestyle='dotted')

    plt.subplot(2, 1, 2)
    plt.title(f'Position of {OLD.version} version')
    plt.plot(xs_old, ys_old, 'r')
    plt.ylabel('y position')
    plt.xlabel('x position')
    plt.grid(True, linestyle='dotted')

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

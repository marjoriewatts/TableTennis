from math import sin, cos, pi, atan


class TableTennis:

    def __init__(self, version, mass, radius):
        self.version = version
        self.mass = mass
        self.radius = radius

        self.Cd = 0.47  # Drag coefficient numbers? Re = 10^5
        self.spin = 3  # assumed constant in the magnus equation
        # Clockwise angular velocity (e.g. positive value corresponds to topspin)

        self.g = -9.81
        self.air_density = 1

    def magnus(self, v):  # Assume angular velocity is constant for now
        Cl = 0.01357
        rho = self.air_density
        A = pi * self.radius ** 2

        return 0.5 * Cl * A * rho * (v ** 2)

    def weight(self):
        m = self.mass
        g = self.g
        return m * g

    def drag(self, v):
        Cd = self.Cd
        A = pi * self.radius ** 2
        rho = self.air_density
        return 0.5 * Cd * A * rho * (v ** 2)

    def system(self, current_state, t):
        x, y, vx, vy = current_state

        Mx = self.magnus(vx)
        My = self.magnus(vy)
        Dx = self.drag(vx)
        Dy = self.drag(vy)

        W = self.weight()
        m = self.mass
        theta = atan(vy/vx)

        ax = ((Mx * -sin(theta)) - Dx) / m
        ay = ((My * cos(theta)) + W + Dy) / m

        return [vx, vy, ax, ay]

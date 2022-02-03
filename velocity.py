from math import cos, sin, pi


class TableTennis:

    def __init__(self, version, mass, radius, x_speed, y_speed):
        self.version = version
        self.mass = mass
        self.radius = radius
        self.x_speed = x_speed
        self.y_speed = y_speed

        self.Cd = 0.1  # Drag coefficient numbers?
        self.spin = 3  # assumed constant in the magnus equation
        # Clockwise angular velocity (e.g. positive value corresponds to topspin)

        self.g = -9.81
        self.air_density = 1

    def magnus(self, v):  # Assume angular velocity is constant for now
        Cl = 0.01357
        rho = self.air_density
        A = pi * self.radius ** 2

        return 0.5 * Cl * A * rho * v ** 2  # figure out how to get direction involved

    def weight(self):
        m = self.mass
        g = self.g
        return m * g

    def drag(self, v):
        Cd = self.Cd
        A = pi * self.radius ** 2
        rho = self.air_density
        return 0.5 * Cd * A * rho * v ** 2

    def x_acceleration(self, xv, t):
        D = self.drag(xv)
        M = self.magnus(xv)
        m = self.mass

        a = (M - D) / m

        return a

    def y_acceleration(self, yv, t):
        M = self.magnus(yv)
        W = self.weight()
        m = self.mass

        a = (M + W) / m

        return a

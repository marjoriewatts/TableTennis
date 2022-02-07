from math import pi


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

    def magnus(self, u):  # Assume angular velocity is constant for now
        Cl = 0.01357
        rho = self.air_density
        A = pi * self.radius ** 2

        return 0.5 * Cl * A * rho * (u[1] ** 2)

    def weight(self):
        m = self.mass
        g = self.g
        return m * g

    def drag(self, u):
        Cd = self.Cd
        A = pi * self.radius ** 2
        rho = self.air_density
        return 0.5 * Cd * A * rho * (u[1] ** 2)

    def x_acceleration(self, ux, t):
        D = self.drag(ux)
        M = self.magnus(ux)
        m = self.mass

        a = (M - D) / m

        return ux[1], a

    def y_acceleration(self, uy, t):
        M = self.magnus(uy)
        W = self.weight()
        D = self.drag(uy)
        m = self.mass

        a = (M + W + D) / m

        return uy[1], a

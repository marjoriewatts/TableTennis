from math import cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt


class TableTennis:

    def __init__(self, version, mass, radius, speed, direction):
        self.version = version
        self.mass = mass
        self.radius = radius
        self.speed = speed
        self.direction = direction

        self.Cd = 0.1  # Drag coefficient numbers?
        self.spin = 3  # assumed constant in the magnus equation
        # Clockwise angular velocity (e.g. positive value corresponds to topspin)

        self.g = -9.81
        self.air_density = 1

        self.xspeed = speed * cos(direction)  # x speed
        self.yspeed = -(speed * sin(direction))  # y speed

    def magnus(self, v):  # Assume angular velocity is constant for now
        Cl = 0.1
        rho = self.air_density
        A = pi * self.radius ** 2

        return 0.5 * Cl * A * rho * v ** 2 * -1  # figure out how to get direction involved

    def weight(self):
        m = self.mass
        g = self.g
        return m * g

    def drag(self, v):
        Cd = self.Cd
        A = pi * self.radius ** 2
        rho = self.air_density
        return 0.5 * Cd * A * rho * v ** 2

    def x_acceleration(self, v, t):
        D = self.drag(v)
        m = self.mass

        a = - D / m

        return a

    def y_acceleration(self, v, t):
        M = self.magnus(v)
        W = self.weight()
        m = self.mass

        a = -(M - W) / m

        return a

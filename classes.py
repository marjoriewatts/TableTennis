from math import cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt


class TableTennis:

    def __init__(self, version, mass, radius):
        
        self.version = version
        self.mass = mass
        self.radius = radius
        

        self.Cd = 0.1  # Drag coefficient numbers?

        
        self.g = -9.81
        self.air_density = 1
        
        self.xspeed = 1  # initial x speed
        self.yspeed = 0  # initial y speed



    def magnus(self, v):
        M = 50
        return M

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

        a = (M + W) / m

        return a


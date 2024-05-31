import matplotlib.pyplot as plt

class Um1D:
    def __init__(self, x0, dt, vx0, ttot):                     # class constructor
        self.x0 = x0                                            # initial x position
        self.dt = dt                                            # time increment
        self.vx0 = vx0                                          # x velocity
        self.ttot = ttot                                        # total time
        self.steps = int(ttot / dt)                             # total number steps

    def x(self, t):                                             # x position at time t
        return self.x0 + self.vx0 * t

    def scenario(self, tmin, tmax, title, xlabel, ylabel, xmax, xmin, ymax, ymin):
        times = [tmin + i * self.dt for i in range(self.steps)]
        positions = [self.x(t) for t in times]
        plt.plot(times, positions)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.axis([xmin, xmax, ymin, ymax])
        plt.show()

    def archive(self):                                          # produce file, plot 1D x motion
        with open('um1d_trajectory.txt', 'w') as f:
            for i in range(self.steps):
                t = i * self.dt
                x = self.x(t)
                f.write(f"{t}, {x}\n")

class Um2D(Um1D):
    def __init__(self, x0, dt, vx0, ttot, y0, vy0):            # Um2D subclass of Um1D
        super().__init__(x0, dt, vx0, ttot)                    # to construct Um1D
        self.y0 = y0                                           # initializes y position
        self.vy0 = vy0                                         # initializes y velocity

    def y(self, t):                                            # produces y at time t
        return self.y0 + self.vy0 * t

    def scenario(self, tmin, tmax, title, xlabel, ylabel, xmax, xmin, ymax, ymin):
        times = [tmin + i * self.dt for i in range(self.steps)]
        x_positions = [self.x(t) for t in times]
        y_positions = [self.y(t) for t in times]
        plt.plot(x_positions, y_positions)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.axis([xmin, xmax, ymin, ymax])
        plt.show()

    def archive(self):
        with open('um2d_trajectory.txt', 'w') as f:
            for i in range(self.steps):
                t = i * self.dt
                x = self.x(t)
                y = self.y(t)
                f.write(f"{t}, {x}, {y}\n")

class Accm2D(Um2D):
    def __init__(self, x0, dt, vx0, ttot, y0, vy0, ax0, ay0):   # Daughter of Um2D
        super().__init__(x0, dt, vx0, ttot, y0, vy0)            # Um2D constructor
        self.ax0 = ax0                                         # adds accelerations
        self.ay0 = ay0                                         # to this class

    def ax(self, t):
        return self.ax0

    def ay(self, t):
        return self.ay0

    def x(self, t):
        return self.x0 + self.vx0 * t + 0.5 * self.ax0 * t**2

    def y(self, t):
        return self.y0 + self.vy0 * t + 0.5 * self.ay0 * t**2

    def scenario(self, tmin, tmax, title, xlabel, ylabel, xmax, xmin, ymax, ymin):
        times = [tmin + i * self.dt for i in range(self.steps)]
        x_positions = [self.x(t) for t in times]
        y_positions = [self.y(t) for t in times]
        plt.plot(x_positions, y_positions)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.axis([xmin, xmax, ymin, ymax])
        plt.show()

    def archive(self):
        with open('accm2d_trajectory.txt', 'w') as f:
            for i in range(self.steps):
                t = i * self.dt
                x = self.x(t)
                y = self.y(t)
                f.write(f"{t}, {x}, {y}\n")

# Example usage
unmd = Um1D(0.0, 0.1, 2.0, 4.0)
unmd.scenario(0, 4.0, 'Uniform motion in 1D', 'Time', 'Position', 4.0, 0, 10.0, 0)
unmd.archive()

um2d = Um2D(0.0, 0.1, 2.0, 4.0, 0.0, 5.0)
um2d.scenario(0, 4.0, 'Uniform motion in 2D', 'X', 'Y', 10.0, 0, 25.0, 0)
um2d.archive()

myAcc = Accm2D(0.0, 0.1, 14.0, 4.0, 0.0, 14.0, 0.0, -9.8)
myAcc.scenario(0, 4.0, 'Accelerated motion in 2D', 'X', 'Y', 55, 0, 5, -100.)
myAcc.archive()

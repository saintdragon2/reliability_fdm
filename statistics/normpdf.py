__author__ = 'SungYong'
import math
import scipy.stats
import numpy

class NormPdf:
    def __init__(self, mean=0, std=1, xs=[], pds=[], bins=201, dx=1):

        self.mean = None
        self.std = None
        self.xs = []
        self.pds = []

        if len(xs) > 0:
            self.xs = xs
            self.pds = pds
            idx = self.pds.index(max(self.pds))
            self.mean = self.xs[idx]
            self.dx = self.xs[1] - self.xs[0]

            ex = 0
            for i in range(0, len(self.xs)):
                x = self.xs[i]
                fx = self.pds[i]

                ex += x * fx * self.dx

            var = 0
            for i in range(0, len(self.xs)):
                x = self.xs[i]
                fx = self.pds[i]
                var += math.pow(x - ex, 2) * fx

            self.std = math.sqrt(var)

        else:
            self.mean = mean
            self.std = std

            x0 = mean - int(bins/2)*dx

            norm_dist = scipy.stats.norm(self.mean, self.std)

            for i in range(0, bins):
                x = x0 + dx * i
                self.xs.append(x)
                self.pds.append(norm_dist.pdf(x))


        #
        # x0 = mean - int(bins/2)*dx
        #
        # norm_dist = scipy.stats.norm(self.mean, self.std)
        #
        # for i in range(0, bins):
        #     x = x0 + dx * i
        #     self.xs.append(x)
        #     self.pds.append( norm_dist.pdf(x))

    def mult(self, other, bins=2001, dx=1):
        mean = self.mean * other.mean

        x0 = min([self.xs[0], other.xs[0]])
        x_max = max([self.xs[-1], other.xs[-1]])
        x_bins = int((x_max - x0)/dx)
        z0 = mean - int(bins/2) * dx

        std_x = self.std
        std_y = other.std
        mean_x = self.mean
        mean_y = other.mean

        zs = []
        z_pds = []

        for i in range(0, bins):
            z = z0 + dx * i
            integrate_x = 0
            for j in range(0, x_bins):
                x = x0 + j*dx
                if x != 0:
                    xy = 1/(std_x * std_y * 2 * math.pi) * math.exp(-math.pow(x-mean_x, 2)/(2*math.pow(std_x,2))-math.pow(z/x-mean_y,2)/(2*math.pow(std_y, 2)))
                    integrate_x +=  xy/numpy.abs(x)

            zs.append(z)
            z_pds.append(integrate_x)

        return NormPdf(xs=zs, pds=z_pds)



    def fx(self, x):
        return scipy.stats.norm(self.mean, self.std).pdf(x)


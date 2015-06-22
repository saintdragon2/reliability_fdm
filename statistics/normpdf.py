__author__ = 'SungYong'
import math
import scipy.stats
import numpy

class NormPdf:
    def __init__(self, mean=0, std=1, xs=None, pds=None, bins=6001, delta=0.01):

        self.mean = None
        self.std = None
        self.delta = None
        self.xs = []
        self.pds = []

        if xs != None:
            self.xs = xs
            self.pds = pds
            idx = self.pds.index(max(self.pds))
            self.mean = self.xs[idx]
            self.delta = delta

            ex = 0
            for i in range(0, len(self.xs)):
                x = self.xs[i]
                fx = self.pds[i]

                ex += x * fx * self.delta

            var = 0
            for i in range(0, len(self.xs)):
                x = self.xs[i]
                fx = self.pds[i]
                var += math.pow(x - self.mean, 2) * fx

            self.std = math.sqrt(var)

        else:
            self.mean = mean
            self.std = std
            self.delta = delta

            x0 = mean - int(bins/2)*delta

            norm_dist = scipy.stats.norm(self.mean, self.std)

            for i in range(0, bins):

                x = x0 + self.delta * i
                self.xs.append(x)
                self.pds.append(norm_dist.pdf(x) * self.delta)

        self.pack()
        # x0 = mean - int(bins/2)*dx
        #
        # norm_dist = scipy.stats.norm(self.mean, self.std)
        #
        # for i in range(0, bins):
        #     x = x0 + dx * i
        #     self.xs.append(x)
        #     self.pds.append( norm_dist.pdf(x))

    def mult(self, other, bins=2001, delta=1):
        mean = self.mean * other.mean

        x0 = min([self.xs[0], other.xs[0]])
        x_max = max([self.xs[-1], other.xs[-1]])
        x_bins = int((x_max - x0)/delta)
        z0 = mean - int(bins/2) * delta

        std_x = self.std
        std_y = other.std
        mean_x = self.mean
        mean_y = other.mean

        zs = []
        z_pds = []

        for i in range(0, bins):
            z = z0 + delta * i
            integrate_x = 0
            for j in range(0, x_bins):
                x = x0 + j*delta
                if x != 0:
                    xy = 1/(std_x * std_y * 2 * math.pi) * math.exp(-math.pow(x-mean_x, 2)/(2*math.pow(std_x,2))-math.pow(z/x-mean_y,2)/(2*math.pow(std_y, 2)))
                    integrate_x +=  xy/numpy.abs(x)

            zs.append(z)
            z_pds.append(integrate_x)

        return NormPdf(xs=zs, pds=z_pds)

    def is_valid_pdf(self):
        return abs(1 - sum(self.pds)) < 1e-10


    def fx(self, x):
        return scipy.stats.norm(self.mean, self.std).pdf(x)

    def pack(self, almost_zero=1e-25):

        if len(self.xs) > 20:
            first_non_zero_idx = next((self.pds.index(n) for n in self.pds if n > almost_zero), len(self.pds))

            self.pds = self.pds[first_non_zero_idx:]
            self.xs = self.xs[first_non_zero_idx:]

            if (len(self.xs)>20):
                after_pack_first_zero_idx = next((self.pds.index(n) for n in self.pds if n < almost_zero), len(self.pds))

                self.pds = self.pds[:after_pack_first_zero_idx]
                self.xs = self.xs[:after_pack_first_zero_idx]




    def convolve(self, other):

        # self.pack()
        # other.pack()


        if self.delta != other.delta:
            print('Different dx ' + str(self.dx) + '\t' + str(other.dx))
            return None
        if len(self.pds) == 0:
            raise EmptyPdfError('Empty Pdf')
            return None

        c_pds = numpy.convolve(self.pds, other.pds)
        c_min = self.xs[0] + other.xs[0]

        c_xs = []
        for i in range(0, len(c_pds)):
            c_xs.append( c_min  + i * self.delta)

        c_pdf = NormPdf(xs=c_xs, pds=c_pds.tolist())
        c_pdf.pack()

        return c_pdf

    def scale(self, f):
        sc_pdf = NormPdf(mean=self.mean * f, std=self.std * f, delta=self.delta)

        if not sc_pdf.is_valid_pdf():
            sc_pdf = NormPdf(mean=self.mean * f, std=self.std*f, delta=self.delta, bins=len(sc_pdf.xs)*2)
        sc_pdf.pack()

        return sc_pdf


    def __add__(self, other):
        return self.convolve(other)


class EmptyPdfError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)
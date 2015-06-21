__author__ = 'SungYong'
import numpy
import scipy.stats
import matplotlib.pyplot as pyplot

print('hello')

# runs = 1e7
#
# xs = numpy.random.normal(40, 2, runs)
# ys = numpy.random.normal(50, 3, runs)
#
# xys = []
# z_x = []
#
# for x in xs:
#     z_x.append(2000/x)
#
# print(numpy.average(z_x))
# print(numpy.std(z_x))


pdf_x = scipy.stats.norm(40, 2)

print(pdf_x.pdf(38))
print(pdf_x.pdf(40))
print(pdf_x.pdf(42))

# for x in xs:
#     for y in ys:
#         xys.append(x*y)
#         z_x.append(y)
#
# print(numpy.average(xys))
# print(numpy.std(xys))



# pyplot.hist(xs, 100)
# pyplot.show()
#
# pyplot.hist(ys, 100)
# pyplot.show()
#
# pyplot.hist(xys, 100)
# pyplot.show()
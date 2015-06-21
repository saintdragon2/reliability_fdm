__author__ = 'SungYong'

import numpy as np
import scipy.stats

from statistics.normpdf import NormPdf



a = scipy.stats.norm(50, 3)
b = scipy.stats.norm(40, 2)

ax = []
a_pdf = []

bx = []
b_pdf = []

for x in range(20, 80):
    ax.append(x)
    a_pdf.append( a.pdf(x) )

for x in range(15, 65):
    bx.append(x)
    b_pdf.append( b.pdf(x))

print(ax)
print(a_pdf)
print(bx)
print(b_pdf)

c_pdf = np.convolve(a_pdf, b_pdf)
cx = []

print(len(c_pdf))

min_c = ax[0] + bx[0]
for x in range( min_c, min_c + len(c_pdf)):
    cx.append(x)

print(cx)
print(c_pdf.argmax())
print(cx[c_pdf.argmax()])





aa = NormPdf(50, 3)
print(len(aa.xs))
print(aa.pds[0])
__author__ = 'saintdragon2'

from statistics.normpdf import NormPdf
import numpy

pdf_a = NormPdf(100, 3, bins=2001)

print(pdf_a.mean)
print(pdf_a.std)
print(pdf_a.delta)
print(len(pdf_a.xs))
print(pdf_a.xs)
print(pdf_a.pds)
print(sum(pdf_a.pds))
print(pdf_a.is_valid_pdf(delta=1e-3))

pdf_b = NormPdf(15, 2, bins=2001)

print(pdf_b.pds)
print(sum(pdf_b.pds))

pdf_ab = pdf_a + pdf_b

print(pdf_ab.mean)
print(pdf_ab.std)
print(sum(pdf_ab.pds))

scaled = pdf_ab.scale(0.5)

print(scaled.mean)
print(scaled.std)

print('--------')

runs = 100000
random_a = numpy.random.normal(100, 3, runs)
random_b = numpy.random.normal(15, 2, runs)

# print(random_a.get(0))

sum_ab = []
for i in range(0, runs):
    sum_ab.append(random_a[i] + random_b[i])

print(numpy.mean(sum_ab))
print(numpy.std(sum_ab))

scaled_mcs = []
for i in range(0, runs):
    scaled_mcs.append(sum_ab[i] /2)

print(numpy.mean(scaled_mcs))
print(numpy.std(scaled_mcs))
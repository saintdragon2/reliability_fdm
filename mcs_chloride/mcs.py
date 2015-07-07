__author__ = 'SungYong'

from mcs_chloride.mcs_cl_fdm import ReliabilityClFdm


runs = 1000

file_name = 'src294.csv'

for i in range(0, runs):
    r_fdm = ReliabilityClFdm()
    r_fdm.read_file(file_name)
    r_fdm.calculate(900)

    tracking = open(file_name[:-3] + 'track_' + str(i), 'w')
    r_fdm.write_traking_elements(tracking, [5020, 5260])
    tracking.close()

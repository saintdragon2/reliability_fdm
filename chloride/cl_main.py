__author__ = 'SungYong'
from chloride.cl_fdm import ClFdm

cl_fdm = ClFdm()
file_name = '500.csv'
cl_fdm.read_file(file_name)

cl_fdm.calculate(2000)

# cl_fdm.print_snapshots([0, 1, 2, 3])

f = open(file_name[:-3] + 'out', 'w')
cl_fdm.write_file_snapshots(f)
f.close()

tracking = open(file_name[:-3] + 'track', 'w')
cl_fdm.write_traking_elements(tracking, [5020, 5260])
tracking.close()
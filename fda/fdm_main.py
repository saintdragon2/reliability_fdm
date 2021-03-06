__author__ = 'SungYong'
from fda.fdm import Fdm

fdm = Fdm()
file_name = 'fdm00.csv'
fdm.read_file(file_name)

fdm.calculate(200)

fdm.print_snapshots([0, 1, 2, 3])

f = open(file_name[:-3] + 'out', 'w')
fdm.write_file_snapshots(f)
f.close()

tracking = open(file_name[:-3] + 'track', 'w')
fdm.write_traking_elements(tracking, [42, 150])
tracking.close()
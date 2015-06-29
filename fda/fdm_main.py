__author__ = 'SungYong'
from fda.fdm import Fdm

fdm = Fdm()
file_name = 'fdm00.csv'
fdm.read_file(file_name)

fdm.calculate(2000)

fdm.print_snapshots([0, 1, 2, 3])

f = open(file_name[:-3] + 'out', 'w')
fdm.write_file_snapshots(f)
f.close()
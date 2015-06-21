__author__ = 'SungYong'
from fda.fdm import Fdm

fdm = Fdm()
fdm.read_file('fdm00.csv')

fdm.calculate(10)

fdm.print_snapshots([0, 1])

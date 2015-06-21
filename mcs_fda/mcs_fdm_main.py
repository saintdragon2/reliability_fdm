__author__ = 'SungYong'

from mcs_fda.mcs_fdm import McsFdm

mcs_fdm = McsFdm()
mcs_fdm.read_file('mcs_fdm.csv')

mcs_fdm.calculate(10)

# mcs_fdm.fdms[0].print_snapshots([0, 1, 2, 3, 4, 5])

mcs_fdm.print_snapshots([0,1,2,3,4,5])
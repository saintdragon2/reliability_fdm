__author__ = 'SungYong'

from mcs_fda.mcs_fdm import McsFdm

mcs_fdm = McsFdm()
# file_name = 'mcs_fdm_1e6.csv'
file_name = 'mcs_fdm_05_bigger_std_bc.csv'
mcs_fdm.read_file(file_name)

mcs_fdm.calculate(50)

# mcs_fdm.fdms[0].print_snapshots([0, 1, 2, 3, 4, 5])

#mcs_fdm.print_snapshots([0,1,2,3,4,5])
f = open(file_name[:-3] + 'out', 'w')
mcs_fdm.write_snapshots(f)
f.close()
__author__ = 'SungYong'

from mcs_fda.mcs_fdm import McsFdm

mcs_fdm = McsFdm()
# file_name = 'mcs_fdm_1e6.csv'
file_name = 'mcs_fdm_05_bigger_std_bc_0630.csv'
# file_name = 'mcs_fdm_05_bigger_std_bc_0701_run30000.csv'
#file_name = 'mcs_fdm_05_bigger_std_bc_0701_run1000.csv'

mcs_fdm.read_file(file_name)

mcs_fdm.calculate(200)

# mcs_fdm.fdms[0].print_snapshots([0, 1, 2, 3, 4, 5])

# mcs_fdm.print_snapshots([0,1,2,3,4,5])
f = open(file_name[:-3] + 'out', 'w')
mcs_fdm.write_snapshots(f)
f.close()


traking = open(file_name[:-3] + 'track', 'w')
mcs_fdm.write_traking_elements(traking, [42, 150])
traking.close()

pdfs_file = open(file_name[:-3] + 'pdfs', 'w')
mcs_fdm.write_traking_elements_pdf(pdfs_file, [42, 150], 100)
pdfs_file.close()
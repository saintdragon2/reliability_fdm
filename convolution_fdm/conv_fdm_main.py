__author__ = 'saintdragon2'

from convolution_fdm.conv_fdm import ConvFdm
conv_fdm = ConvFdm()

# file_name = 'conv_fdm_0_5.csv'
file_name = 'conv_fdm_0_5_bigger_std.csv'

conv_fdm.read_file(file_name)

conv_fdm.calculate(50)

# conv_fdm.print_snapshots([0,1,2,3,4,5,6,7,8,9,10, 20, 30, 39])

f = open(file_name[:-3] + 'out', 'w')
conv_fdm.write_file_snapshots(f)
f.close()
__author__ = 'saintdragon2'

from convolution_fdm.conv_fdm import ConvFdm
conv_fdm = ConvFdm()
conv_fdm.read_file('conv_fdm_0_5.csv')

conv_fdm.calculate(10)

conv_fdm.print_snapshots([0,1,2,3,4,5,6,7,8,9])

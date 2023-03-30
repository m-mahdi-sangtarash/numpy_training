import numpy_financial as np_f

pmt = -100
nper = 120
rate = 0.05 / 12
fv = 15692.93

pv = np_f.pv(rate, nper, pmt, fv)
print("pv: ", pv)
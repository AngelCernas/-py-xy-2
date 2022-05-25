import random as rm
import matplotlib.pyplot as mpp

rms = rm.gauss(500, 80.10)
print('La distribucion de Gaus:', rms)
mpp.figure(figsize=(9, 6))
mpp.hist([rm.gauss(500, 80.10) for i in range(500)], bins = 1100)
mpp.show()

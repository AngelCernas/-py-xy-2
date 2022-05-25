import numpy

import matplotlib.pyplot 

MeValor = 170
MoValor = numpy.sqrt(2/numpy.pi) * MeValor
Solucion = numpy.random.rayleigh(MoValor,1000000)
Res = 100.*sum(Solucion > 180)/1000000.
print('El porcentaje que supera la estatura media es: ', Res)
matplotlib.pyplot.figure(figsize=(9, 6))
matplotlib.pyplot.hist([numpy.random.rayleigh(180, 1000000)], bins=200, density=True)
matplotlib.pyplot.show()


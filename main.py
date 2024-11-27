import numpy as np
import matplotlib.pyplot as mpl

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

domain = np.arange(-10, 10)

range_quadrilateral = a * (domain ** 2) + b * domain + c
range_logarithmic = np.log2(domain)

mpl.plot(domain, range_quadrilateral, marker='o')
mpl.plot(domain, range_logarithmic, marker='o')
mpl.show()





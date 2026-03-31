import scipy.integrate as integrate
import numpy as np
import math
from math import sqrt

GdL = 1
alpha = 0.05

upsilon = 3.841

gamma = math.gamma(GdL/2)

P = (1/2)**(GdL/2)*(1/gamma)*(integrate.quad( lambda u : u**(GdL/2 -1)*np.exp(-u/2) , 0, upsilon))[0]
# P = integrate.quad( lambda u : u^(GdL/2 -1) , 0, upsilon)

print(P)

###

T = 200
E11 = T*50/T*55/T
E10 = T *50/T*145/T
E01 = T*150/T*55/T
E00 = T* 150/T * 145/T

ji2 = (25 -E11)**2/E11 + (25-E10)**2/E10 + (30 - E01)**2/E01 + (120 - E00)**2/E00

print(E11, E10, E01, E00)
print(ji2)
import numpy as np
from polyFit import *
import matplotlib.pyplot as plt
from plotPoly import *

xData = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
yData = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

m = 1
coeff = polyFit(xData, yData, m)

print("Coefficients are: \n", coeff)
print("Std. deviation =", stdDev(coeff,xData,yData))

plotPoly(xData, yData, coeff)
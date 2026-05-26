import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

xData = np.array([1.0, 2.0, 5.0])
yData = np.array([1.0, 4.0, 3.0])

# Now let us turn the (one-dimensional numpy) array xData
# into a matrix (a two-dimensional numpy array)
# with 5 rows and 1 column 
xData = xData.reshape((3,1))

ourModel = LinearRegression()
ourModel.fit(xData, yData)

alpha =  ourModel.intercept_
beta = ourModel.coef_[0]

print(f'alpha={alpha:.2f}, beta={beta:.2f}')

# optimal values found were alpha=1.85 and beta=0.31
# Next, choose some range around beta=0.31. For example, B that goes from -1 to +1
B_start = -1
B_end = +1
n_points = 1000
B_values = np.linspace (B_start, B_end, n_points)

def f_aux_B(B):
    return (1-alpha-B)**2 + (4-alpha-2*B)**2 + (3-alpha-5*B)**2

f_aux_B_values = f_aux_B(B_values)

plt.plot(B_values, f_aux_B_values)
plt.show()
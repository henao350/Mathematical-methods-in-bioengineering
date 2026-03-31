import numpy as np
from sklearn.linear_model import LinearRegression

xData = np.array([0.0, 1.0, 2.0, 2.5, 3.0])
price = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

# Now let us turn the (one-dimensional numpy) array xData
# into a matrix (a two-dimensional numpy array)
# with 5 rows and 1 column 
xData = xData.reshape((5,1))

ourModel = LinearRegression()
ourModel.fit(xData, price)

print(ourModel.coef_[0], ourModel.intercept_)
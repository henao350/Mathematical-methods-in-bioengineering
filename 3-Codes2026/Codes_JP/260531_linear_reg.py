#Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Define set of values to linear regress
# Easy to read/edit lists
raw_x = [1.0, 2.0, 3.0]
raw_y = [2.0, 4.0, 6.0]

# Convert and reshape in one clean line
ind_var = np.array(raw_x).reshape(-1, 1) #The -1,1 makes sure there is exactly 1 column
dep_var = np.array(raw_y)

#Defines the class as a callable object
Linreg = LinearRegression()

#Applies and saves slope, intercept and R2 as variables
Linreg.fit(ind_var, dep_var)
intercept =  Linreg.intercept_
slope = Linreg.coef_[0] #The first element of the list
R2 = Linreg.score(ind_var, dep_var)

print(f'Intercept={intercept:.2f}, Slope={slope:.2f}, R2={R2:.4f}')

# Calculate error
for i in range(len(raw_y)):
    x_val = raw_x[i]
    y_val = raw_y[i]
    print(f"Point {i} is ({x_val}, {y_val}) with an error of _____")
    #a

#Plot the 
ind_var_continuous = np.linspace(ind_var.min(),ind_var.max(),100)
funCorrosion = lambda t: intercept + slope*t
label_text = f'y = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {R2:.4f}'

plt.figure()
gfx = plt.subplot()
gfx.scatter(ind_var, dep_var)
gfx.plot(ind_var_continuous, funCorrosion(ind_var_continuous))
gfx.text(1.2, 5.5, label_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
plt.show()


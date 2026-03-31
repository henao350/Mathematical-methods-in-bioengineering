import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


###
# def f(x,y):
#     exponential_number = np.exp(1)
#     return exponential_number**(-x*y)
def f(x,y):
    return x*y
#
x = np.arange(-3, 3, 0.5)
y = np.arange(-3, 3, 0.5)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)
#
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap=plt.cm.viridis, edgecolor='none')
ax.plot_wireframe(X, Y, Z)
###

theta = np.linspace(-np.pi, np.pi, 45)
xg = np.sqrt(8)*np.cos(theta)
yg = np.sqrt(8)*np.sin(theta)
zg = -8 + 0*theta
ax.scatter(xg, yg, zg)
#
zg = f(xg, yg)
ax.scatter(xg, yg, zg, color='red', s=30)
#
plt.show()
plt.savefig('Lagrange2.png')


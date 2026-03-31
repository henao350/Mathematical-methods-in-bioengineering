import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2 +1
Z_tangent = 1 + Z*0
# Z_tangent = np.zeros((17,50))
# Z_tangent += 1
# Z_tangent = 1
# print(Z_tangent)
# print(Z.shape)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.viridis, edgecolor='none')
ax.plot_surface(X, Y, Z_tangent, cmap=plt.cm.viridis, edgecolor='none')
plt.show()

Z_tangent = -2*X + 6*Y - 9
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.viridis, edgecolor='none')
ax.plot_surface(X, Y, Z_tangent, cmap=plt.cm.viridis, edgecolor='none')
ax.scatter([-1], [3], [11], color='red',  marker='o', s=10)
z_values = np.linspace(-60,11,20)
ax.scatter([-1 + 0*z_values], [3 + 0*z_values], z_values)
plt.show()


# # Prepare data
# x = np.arange(-5, 5.1, 0.2)
# y = np.arange(-5, 5.1, 0.2)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(X) * np.cos(Y)

# # Create 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.viridis, edgecolor='none')

# # Add labels and colorbar
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# fig.colorbar(surf, shrink=0.5, aspect=5)

# # Show the plot
# plt.title('3D Surface Plot of sin(X) * cos(Y)')
# plt.show()